"""Build a public-only gazetteer; names are facts, descriptors are generated variants."""
from pathlib import Path
import csv
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.rules import BRAND, CATS

# Independently curated public business identities, without private-data consultation.
CURATED = {
 'Food_Dining': "Al Baik|Al Mallah|Al Reef Lebanese Bakery|Arabian Tea House|Automatic Restaurant|Bait Al Mandi|Barbeque Nation|Bateel|Bikanervala|Bosporus|Buffalo Wild Wings|Burger King|Caffe Nero|Caribou Coffee|Chili's|Costa Coffee|Denny's|Dunkin|Five Guys|Gazebo|Hardee's|Jollibee|Karak House|Krispy Kreme|Little Caesars|Nando's|Operation Falafel|Papa John's|Paul Bakery|P.F. Chang's|Pickl|Popeyes|Raising Cane's|Ravi Restaurant|Saddle|Shake Shack|Starbucks|Subway|Texas Chicken|The Cheesecake Factory|Tim Hortons|Wagamama|Zaatar w Zeit",
 'Groceries': 'Al Maya|Aswaaq|Baqer Mohebi|Choithrams|Geant|Grandiose|Kibsons|Lulu|Nesto|Organic Foods and Cafe|Spinneys|Union Coop|Viva|Waitrose|Waterfront Market|West Zone|Zoom',
 'Transport_Auto': 'ADNOC|ENOC|Emarat|CAFU|Careem Ride|Dubai Taxi|Ekar|Udrive|Salik|Parkin|RTA NOL|Darb|Mawaqif|Hertz|Avis|Budget Rent a Car|Europcar|Thrifty|Tasjeel|Shamil|AutoPro|Fasttrack',
 'Shopping_Retail': 'Amazon.ae|Noon|Namshi|Shein|IKEA|Home Centre|Home Box|Pan Emirates|Danube Home|ACE Hardware|Sharaf DG|Jumbo Electronics|Emax|Virgin Megastore|Apple Store|Samsung Store|Decathlon|Sun and Sand Sports|Nike|Adidas|Puma|Skechers|Zara|H&M|Uniqlo|Max Fashion|Centrepoint|Splash|Babyshop|Shoemart|Brands For Less|Daiso|Mumzworld|FirstCry|Trendyol|Temu|Ounass|Bloomingdales|Level Shoes|Chalhoub|Cartier|Tiffany|Joyalukkas|Malabar Gold|Damas|Pure Gold|Magrudy|Kinokuniya',
 'Utilities_Telecom': 'DEWA|SEWA|ADDC|FEWA|Etihad Water and Electricity|TAQA Distribution|Etisalat|du|Virgin Mobile UAE|Empower|Emicool|Tabreed|Lootah Gas|Mai Dubai|Al Ain Water|Masafi',
 'Health_Wellness': 'Aster Pharmacy|Aster Hospital|Life Pharmacy|Boots Pharmacy|BinSina Pharmacy|Super Care Pharmacy|Medicina Pharmacy|Thumbay Hospital|NMC Hospital|Mediclinic|Medcare|Saudi German Hospital|American Hospital Dubai|Zulekha Hospital|Burjeel Hospital|Cleveland Clinic Abu Dhabi|Moorfields Eye Hospital Dubai|Al Zahra Hospital|HealthHub|Prime Medical Center|Fitness First|GymNation|Warehouse Gym|Fitness Time|Tips and Toes|NStyle|Sephora|Faces|Bath and Body Works',
 'Travel': 'Emirates Airline|Etihad Airways|flydubai|Air Arabia|Wizz Air|Saudia|Qatar Airways|Gulf Air|Oman Air|Kuwait Airways|Jazeera Airways|Flynas|Booking.com|Agoda|Airbnb|Expedia|Trip.com|Cleartrip|Musafir|Dnata Travel|Rayna Tours|Marriott|Hilton|Hyatt|Jumeirah|Rove Hotels|Rotana|Atlantis The Palm|Accor',
 'Entertainment': 'VOX Cinemas|Reel Cinemas|Roxy Cinemas|Novo Cinemas|Cinema City|IMG Worlds of Adventure|Dubai Parks and Resorts|Motiongate|Legoland Dubai|Ski Dubai|Aquaventure|Wild Wadi|Ferrari World|Warner Bros World|Yas Waterworld|SeaWorld Abu Dhabi|Louvre Abu Dhabi|Museum of the Future|Dubai Frame|Dubai Opera|Platinumlist|Ticketmaster|Steam|PlayStation|Xbox|Nintendo|Topgolf Dubai|Dubai Safari Park',
 'Government_Fees': 'Dubai Police|Abu Dhabi Police|Sharjah Police|ICP|GDRFA|Dubai Municipality|Sharjah Municipality|TAMM|Dubai Economy and Tourism|Ministry of Foreign Affairs|Ministry of Human Resources and Emiratisation|Tasheel|Tawjeeh|Amer Center|VFS Global|Dubai Courts|Federal Tax Authority',
 'Housing_Education': 'Emaar Community Management|Nakheel Community Management|Dubai Properties|Damac|Wasl|Ejari|GEMS Education|Taaleem|Nord Anglia International School Dubai|Repton Dubai|Dubai College|Jumeirah College|University of Wollongong in Dubai|American University of Sharjah|American University in Dubai|Heriot-Watt University Dubai|Middlesex University Dubai|University of Dubai|Zayed University|Khalifa University|United Arab Emirates University|British Council|Coursera|Udemy|Justlife|Urban Company',
 'Digital_Subscriptions': 'Netflix|Spotify|OSN+|Shahid|Disney+|Amazon Prime|Apple iCloud|Apple Music|YouTube Premium|Google One|Microsoft 365|Adobe|Canva|ChatGPT|Claude|Notion|Dropbox|Zoom|GitHub|LinkedIn Premium|Snapchat+|Patreon|Noon One|Careem Plus|Anghami|STARZPLAY|beIN CONNECT|TOD',
 'Others': 'Emirates Post|DHL|FedEx|Aramex|UPS|Tawuniya|Sukoon Insurance|Orient Insurance|Dubai Insurance|GIG Gulf|National Takaful|Emirates Red Crescent|Dubai Cares|Beit Al Khair|Washmen|Laundryheap|Champion Cleaners'
}

def build():
    entries = {}
    for category, names in CURATED.items():
        for name in names.split('|'):
            entries[name.casefold()] = dict(brand=name, category=category, country='AE', emirate='',
                 confidence='curated_category;descriptor_unverified', source='project:independently_curated_public_business_facts', license='project-authored', descriptor_status='generated_unverified')
    for name, category in BRAND.items():
        if name.casefold() not in entries:
            entries[name.casefold()] = dict(brand=name,category=category,country='AE',emirate='',confidence='project_category;descriptor_unverified',source='project:scripts/rules.py',license='project-owned',descriptor_status='generated_unverified')
    bindings = json.loads((ROOT/'research/wikidata_businesses.json').read_text(encoding='utf-8'))['results']['bindings']
    countries = {'United Arab Emirates':'AE','Saudi Arabia':'SA','Qatar':'QA','Kuwait':'KW','Bahrain':'BH','Oman':'OM'}
    for record in bindings:
        name, kind = record['itemLabel']['value'], record['typeLabel']['value']
        if re.fullmatch(r'Q\d+',name) or kind in ('cave','railway station','residential building'):
            continue
        # Generic businesses include industrial/financial firms; retain facts for reference,
        # but exclude uncertain identities/categories from synthetic training by default.
        mapping = {'university':'Housing_Education','public university':'Housing_Education','school':'Housing_Education',
                   'hospital':'Health_Wellness','restaurant':'Food_Dining','hotel':'Travel','airline':'Travel','shopping center':'Shopping_Retail'}
        category = mapping.get(kind,'Others')
        key = name.casefold()
        if key not in entries:
            entries[key] = dict(brand=name,category=category,country=countries[record['countryLabel']['value']],emirate='',
                confidence='type_mapped' if kind in mapping else 'unreviewed_business_excluded',
                source=record['item']['value'],license='CC0-1.0',descriptor_status='generated_unverified')
    path = ROOT/'synth/gazetteer/merchants.csv'
    path.parent.mkdir(exist_ok=True)
    with path.open('w',encoding='utf-8',newline='') as stream:
        writer = csv.DictWriter(stream,fieldnames=['descriptor','brand','category','country','emirate','confidence','source','license','descriptor_status','training_eligible'])
        writer.writeheader()
        for entry in sorted(entries.values(),key=lambda x:(x['country'],x['brand'])):
            writer.writerow(dict(descriptor=entry['brand'].upper(),training_eligible='false' if entry['confidence']=='unreviewed_business_excluded' else 'true',**entry))
    print('Public business identities:',len(entries),'; training eligible:',sum(x['confidence']!='unreviewed_business_excluded' for x in entries.values()))

if __name__ == '__main__':
    build()
