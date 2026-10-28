import re

CATEGORIES = {
    'Food_Dining':           'Restaurants, cafes, fast food, bakeries, juice and dessert shops, and food delivery apps (Talabat, Keeta, Deliveroo, Noon Food, Careem Food).',
    'Groceries':             'Supermarkets, hypermarkets, minimarts/baqalas, quick-commerce grocery (Noon Minutes, Instashop), butchers, fruit and veg.',
    'Transport_Auto':        'Fuel, ride-hailing and taxis, RTA/metro/nol, Salik, parking, car rental, car service, repairs and vehicle registration.',
    'Shopping_Retail':       'Retail and e-commerce (Amazon, Noon), clothing, electronics, furniture and home goods, gifts, flowers, books, BNPL instalments (Tabby/Tamara).',
    'Utilities_Telecom':     'Electricity and water (DEWA, SEWA, FEWA, ADDC), drinking-water delivery, district cooling, gas, mobile and home internet (du, Etisalat/e&).',
    'Health_Wellness':       'Pharmacies, clinics, hospitals, dental, opticians, health insurance, gyms, salons and barbers, cosmetics and perfume, vets.',
    'Travel':                'Airlines, hotels and resorts, booking sites (Booking.com, Agoda, Airbnb), travel agencies and tours, airport services.',
    'Entertainment':         'Cinemas, video games and game stores, events and tickets, attractions and theme parks, museums, sports and leisure activities.',
    'Government_Fees':       'Government services and fines: visas and residency (ICP/ICA, GDRFA, VFS, UKVI), traffic fines, police, courts, ministries, municipality, typing and document-clearing centres, embassies.',
    'Housing_Education':     'Rent and property (real estate agents, Ejari, community fees), home cleaning and maintenance, building materials and landscaping, schools, nurseries/day care, universities, courses and exams.',
    'Digital_Subscriptions': 'Recurring and digital services: streaming, music, software, cloud and AI tools, app stores, in-app purchases, Snapchat, Patreon, hosting.',
    'Others':                'Everything else: insurance (non-health), courier and post, tailoring, laundry, printing and photos, charity, advertising (Facebook/TikTok ads), freelance and payment services, unclear merchants.',
}
CATS = list(CATEGORIES)

# Exact canonical brand names (from the pipeline's merchant_clean) -> category
BRAND = {
    'Talabat': 'Food_Dining', 'Keeta': 'Food_Dining', 'Noon Food': 'Food_Dining', 'Zomato': 'Food_Dining',
    'Deliveroo': 'Food_Dining', 'Instashop': 'Groceries', 'Noon Minutes': 'Groceries', 'Noon Daily': 'Groceries',
    'Noon': 'Shopping_Retail', 'Noon One': 'Digital_Subscriptions', 'Amazon': 'Shopping_Retail',
    'Careem': 'Transport_Auto', 'Uber': 'Transport_Auto', 'Bolt': 'Transport_Auto', 'RTA': 'Transport_Auto', 'ADNOC': 'Transport_Auto',
    'ENOC': 'Transport_Auto', 'Emarat': 'Transport_Auto',
    'Snapchat': 'Digital_Subscriptions', 'Google': 'Digital_Subscriptions', 'Apple': 'Digital_Subscriptions',
    'Spotify': 'Digital_Subscriptions', 'Netflix': 'Digital_Subscriptions', 'Patreon': 'Digital_Subscriptions',
    'Google (temporary hold)': 'Digital_Subscriptions',
    'Steam': 'Entertainment', 'PlayStation': 'Entertainment', 'VOX Cinemas': 'Entertainment',
    'Carrefour': 'Groceries', 'Lulu': 'Groceries', 'Viva': 'Groceries', 'Spinneys': 'Groceries', 'Union Coop': 'Groceries',
    'City Farms': 'Groceries', 'Souq Extra': 'Groceries',
    'DEWA': 'Utilities_Telecom', 'SEWA': 'Utilities_Telecom', 'FEWA': 'Utilities_Telecom', 'Etisalat': 'Utilities_Telecom',
    'du': 'Utilities_Telecom',
    "McDonald's": 'Food_Dining', 'KFC': 'Food_Dining', 'Pizza Hut': 'Food_Dining', "Domino's": 'Food_Dining',
    'Burger King': 'Food_Dining', 'Starbucks': 'Food_Dining', 'Americana': 'Food_Dining',
    'Choithrams': 'Groceries', 'Facebook Ads': 'Others', 'TikTok': 'Others',
    'Tabby': 'Shopping_Retail', 'Tamara': 'Shopping_Retail', 'Dubai Government': 'Government_Fees', 'Upwork': 'Others',
    'PayPal': 'Shopping_Retail', 'Ziina': 'Others',
}
# Brands whose category genuinely varies by purchase -> lower confidence, flag for review
AMBIGUOUS = {'Amazon', 'Noon', 'Tabby', 'Tamara', 'PayPal', 'Careem', 'Ziina', 'Google', 'Carrefour', 'Lulu'}

# Keyword rules on the merchant text, checked in order (first match wins)
KEYWORDS = [
    ('Food_Dining', r'TALABAT|DELIVERY HERO|KEETA|DELIVEROO|ZOMATO|CAREEM ?FOOD|HUNGERSTATION|JAHEZ|THE EASIEST DELIVERY|NOW ?NOW'),
    # Government before Transport so 'TRAFFIC FINES' / 'RTA FINES' are fees, not transport
    ('Government_Fees', r'GOVERNMENT|GOVERMENT|GOVT|GOV\b|GOVE\b|POLICE|TRAFFIC FINE|\bFINES?\b|MOI\b|MINISTRY|\bMOFA|\bICP\b|\bICA\b|SMART SERVIC|'
                        r'TAMM\b|\bAMER\b|TASHEEL|TAS-?HEEL|TYPING|\bVISA\b|VFS|UKVI|IMMIGRATION|EMIRATES ID|NOTARY|COURT|JUSTICE|'
                        r'MUNICIPAL|MUNCIPAL|DUBAI EGOV|SMART DUBAI|DUBAIPAY|\bDED\b|ECONOM|FINANCE DEPART|CONSULATE|EMBASSY|'
                        r'DOCS? (?:SERV|CLEAR)|DOCUMENTS? CLEAR|TAKHLEES|FTA |CREDIT BUREAU|AECB|INVOLUNTARY LOSS|\bRDC\b|DCCA'),
    ('Transport_Auto', r'PETROL|FUEL|\bADNOC|\bENOC|EPPCO|EMARAT|\bTAXI|CABS?\b|CAREEM|UBER|\bBOLT\b|\bRTA\b|SALIK|NOL\b|METRO|PARKING|PARKIN\b|'
                  r'CAR ?RENT|RENT ?A ?CAR|UDRIVE|EKAR|YANGO|INVYGO|CAR WASH|AUTO SPARE|AUTO ?SERVICE|\bAUTO\b|TYRE|GARAGE|MOTORS?\b|CAFU|'
                  r'MAWAQIF|\bDARB\b|\bITC\b|INTEGRATED TRANSPORT|TRANSPORT|LPG\b|ADNOC WALLET|ROAD &|TOLL|EMIRATES DRIVING|DRIVING|'
                  r'CAR ?PARK|CARF PARK|PRKN|Q PARK|TIER .*RIDE|VEHICLE|TASJEEL|TAJDEED|HEATHROW EXPRESS|GWR\b'),
    ('Groceries', r'SUPERMARKET|SUPERMAR|HYPERMARKET|HYPER ?MARKET|HYPMK|HPMKT|MINI ?MART|MINIMARKET|GROCER|BAQALA|BAKALA|FOODSTUFF|'
                  r'FOOD STUFF|CO-?OP|COOP\b|SPINNEYS|WAITROSE|CARREFOUR|LULU|GRANDIOSE|CHOITHRAMS|ALMAYA|AL MAYA|NESTO|WEST ZONE|'
                  r'GEANT|KIBSONS|BUTCHER|FRUITS?\b|VEGETABLE|ROASTERY|\bNUTS\b|\bDATES\b|SOUQ PLANET|SAVEWAY|DAY TO DAY|'
                  r'SPMKT?|SUPMKT|SUPERMA|SUPER ?MARKE|HELLO MART|ADVANTAGE MINI|PASONS|THOMSUN|TROLLEY|GMG CONSUMER|REFRESHMENT'),
    # Travel before Food so hotel names are not caught by LOUNGE/DINING
    ('Travel', r'HOTEL|RESORT|\bINN\b|HOSTEL|BOOKING\.COM|HOTEL (?:AT|ON) BOO|\bBKG\b|AIRBNB|AGODA|EXPEDIA|TRIP\.COM|MAKEMYTRIP|TAJAWAL|REHLAT|'
               r'TRAVEL|TRAVL|\bTRAV\b|TOURISM|TOURS?\b|ETRAVELI|AEROBILET|AIRLINE|AIRWAYS|\bAIR ?(?:ARABIA|BLUE|INDIA)|AIRBLUE|FLYDUBAI|'
               r'EMIRATES AIRLINE|ETIHAD AIR|FLYNAS|WIZZAIR|SAUDIA|NATIONAL AIR SERV|PAKISTAN INTERNATIONAL|AIRPORT|AVIATION|RAYNA|\bHOTE\b|RITZ|HILTON|\bIBIS\b|MARRIOTT|SHERATON|NOVOTEL|RADISSON|HYATT|ATLANTIS THE PALM|'
               r'ADDRESS (?:GRAND|DOWNTOWN|SKY|BEACH|MARINA|DUBAI)|ROVE (?:AT|DOWNTOWN|CITY)|MALAHINI|TRAVEAZY'),
    ('Food_Dining', r'RESTAURANT|RESTAURAN|RESTAU|RESTURANT|REST\b|CAFE|CAFETERIA|CAFETERI|COFFEE|KITCHEN|GRILL|SHAWARMA|SHAWERMA|'
                      r'BURGER|PIZZA|BAKERY|BAKERIES|PATISSERIE|PATIS|SWEETS|ICE CREAM|GELATO|JUICE|DONUT|KRISPY|DINER|BISTRO|'
                      r'FALAFEL|KARAK|TEA\b|CHAI|BIRYANI|DARBAR|TANDOOR|NOODLE|SUSHI|STEAK|BBQ|BARBECUE|CHICKEN|FRIED|WINGS|'
                      r'SUBWAY|HARDEES|POPEYES|SHAKE ?SHACK|FIVE GUYS|TIM HORTONS|COSTA|CARIBOU|DUNKIN|BASKIN|PAUL\b|'
                      r'MANOUSHE|MANAKEESH|FOOD\b|FOODS\b|EATERY|DINING|BUFFET|LOUNGE|CATERING|ARABIAN TEA|TEA HOUSE|BAY BITES|'
                      r'MAESTRO|PAPA JOHN|LITTLE CAESAR|NANDO|TEXAS|DENNY|FUDDRUCKERS|PEPPERMILL|JOLLIBEE|CHILI|APPLEBEE|'
                      r'SHAKE|YOGURT|YOGO|DESSERT|CHOCOLATE|CAKE|PASTRY|BREAD|SANDWICH|MANDI|KEBAB|KABAB|TIKKA|HALWA'),
    ('Health_Wellness', r'PHARMAC|PHARMA\b|MEDICINA|CLINIC|MEDICAL|HOSPITAL|DENTAL|DENTIST|LAB\b|LABORATOR|HEALTH|'
                               r'SALON|BARBER|GENTS|LADIES|BEAUTY|SPA\b|GYM|FITNESS|GYMNATION|WELLNESS|DAMAN|'
                               r'DERMA|PHYSIO|VET\b|VETERINARY|PAWS|\bASTER\b|LIFE PHY|BOOTS|HAIR|'
                               r'\bPHY\b|PHAR\b|PHAR |\bPH\b|PRIMARY HE|MEDCARE|MEDICA\b|WATSON|ASTERONLINE|PSYCH'),
    ('Utilities_Telecom', r'DEWA|SEWA|FEWA|ADDC|ELECTRICITY|WATER AUTH|ETISALAT|\bE&|\bDU\b|GSM SERVICE|TELEPHONE|VIRGIN MOBILE|'
                          r'INTERNET|EMPOWER|TABREED|SMART GAS|PURE WATER|WATER PURIF|MOBILY|\bZAIN\b|\bZONG\b|UFONE|JAWWY'),
    ('Housing_Education', r'REAL ESTATE|PROPERTIES|PROPERTY|EJARI|HOUSING|CLEANING|CLEAN SER|MAIDS|URBAN COMPANY|JUSTLIFE|TADBEER|'
                          r'UNIVERSITY|COLLEGE|SCHOOL|ACADEMY|INSTITUTE|EDUCATION|DAY ?CARE|BRITISH COUNCIL|SAVE MY EXAMS|COURSERA|'
                          r'UDEMY|EXAM|ADMISSION|REGISTRATION SVCS|TUITION|TRAINING|SKILLS'),
    ('Digital_Subscriptions', r'NETFLIX|SPOTIFY|ANGHAMI|SHAHID|OSN|DISNEY|YOUTUBE|GOOGLE|APPLE\.COM|ITUNES|MICROSOFT|ADOBE|'
                                r'OPENAI|CHATGPT|ANTHROPIC|CLAUDE|CANVA|NOTION|DROPBOX|ICLOUD|AMAZON PRIME|PRIME VIDEO|'
                                r'SNAPCHAT|DISCORD|PATREON|TWITCH|HOSTINGER|GODADDY|NAMECHEAP|DIGITALOCEAN|AWS|GITHUB|'
                                r'NORD|VPN|EPIDEMIC SOUND|POLIIGON|UNITY|ASUS ?CLOUD|MUSIXMATCH|RUNWAY|HIGGSFIELD|MUMU LABS|GUMROAD|HOTMART|PRIVATEINTERNET|'
                                r'AI CATCH|SUBS|ORACLE|WETRANSFER|LINKEDIN|DUOLINGO|MEDIUM|SUBSTACK|MIDJOURNEY|ELEVENLABS'),
    ('Entertainment', r'CINEMA|VOX\b|REEL|NOVO|ROXY|STEAM|PLAYSTATION|XBOX|NINTENDO|EPIC GAMES|SUPERCELL|OCULUS|META QUEST|'
                               r'RIOT|BLIZZARD|ROBLOX|GAMES?\b|GAMING|ARCADE|BOWLING|MAGIC PLANET|FUN CITY|PLAYTIME|TRAMPOLINE|'
                               r'GLOBAL VILLAGE|SKI DUBAI|WATERPARK|AQUAVENTURE|WILD WADI|LEGOLAND|AMUSEMENT|LEISURE|FUN FAIR|'
                               r'MOTIONGATE|FERRARI WORLD|YAS WATERWORLD|ZOO|MUSEUM|PLATINUMLIST|TICKETMASTER|TICKET|EVENTS?\b|ARENA\b|'
                               r'BADMINTON|PADEL|SPORTS?\b|CLUB\b|SHOOTING|GOLF|KARTING|KARTS|BOAT|YACHT|ESCAPE|ADVENTUR|PAVILION|'
                               r'COMENPLAY|ARENANET|DUBAI PARKS|EXPO|SEAWORLD|SKYDIVE|BURJ KHALIFA|AT THE TOP|DUBAI FRAME|PLAYGROUND'),
    ('Others', r'INSURANCE|\bINS\b|TAKAFUL|SUKOON|AXA|AIG |CHARITY|CHARITA|RED CRESCENT|DUBAI CARES|DONATION|'
               r'POST\b|EMIRATES POST|ARAMEX|DHL|FEDEX|FEDERAL EXPRESS|\bUPS\b|COURIER|SHIPPING|LAUNDRY|DRY ?CLEAN|'
               r'LEGAL|LAWYER|CONSULT|ACCOUNTING|UPWORK|FIVERR|PRINT|COPY CENT|PHOTO|STUDIO|TAILOR|FACEBOOK ADS|TIKTOK|BUSINESS SETUP'),
    ('Shopping_Retail', r'AMAZON|NOON|NAMSHI|SHEIN|TEMU|ALIEXPRESS|EBAY|IKEA|ACE\b|HOME ?CENTRE|HOME ?BOX|PAN EMIRATES|DANUBE|'
                 r'SHARAF|JUMBO|EMAX|VIRGIN MEGA|APPLE STORE|SAMSUNG|ELECTRONIC|MOBILE|PHONES?\b|COMPUTER|TECHMASH|'
                 r'CENTREPOINT|CENTERPOINT|MAX\b|SPLASH|LIFESTYLE|BRAND BAZAAR|MINISO|DAISO|DRAGON MART|LANDMARK|'
                 r'H ?& ?M|ZARA|UNIQLO|NIKE|ADIDAS|DECATHLON|SKECHERS|SHOES|FASHION|GARMENT|TEXTILE|CLOTH|ABAYA|'
                 r'JEWEL|WATCH|GOLD\b|PERFUMES?\b|FLOWER|GIFT|TOYS?\b|BOOKS?\b|KINOKUNIYA|MAGRUDY|STATIONERY|'
                 r'PAPER|HARDWARE|FURNITURE|MALL\b|DEPARTMENT|OUTLET|STORE|SHOP|BOUTIQUE|DBRAND|MARKET\b|'
                 r'TABBY|TAMARA|POSTPAY|DFTBA|BLACKBIRD|BLENDJET|TOOLMART|TUFTING|TRADING|TRADI\b|TRD\b|TRDG|GENERAL T|'
                 r'HANDICRAFT|LINEN|DEBENHAMS|PRIMARK|GIORDANO|KHAADI|HIJAB|'
                 # Danish's audit (27 Oct 2026): beauty/perfume/eyewear shops and garden/building supplies are retail
                 r'PERFUME|COSMETIC|SEPHORA|FACES|BATH ?& ?BODY|VICTORIA|LOCCITANE|KIKO|NYX|MAKEUP|OPTIC|EYEWA|EYEZONE|\bEYES?\b|MAGRABI|'
                 r'BUILDING|BLDG|BLD\.? ?MAT|CERAMIC|PAINTS|AGR\b|AGRICU|AGRRICUL|PLANT NURSERY|NURSERY LLC|LANDSC|GARDEN|SEEDS|TURF|CONSTRUC'),
]
KEYWORDS = [(c, re.compile(p, re.I)) for c, p in KEYWORDS]

# Hand corrections for cases the keyword rules get wrong
OVERRIDES = {
    'SUITS SHIRTS GENTS': 'Shopping_Retail', 'DIYANNA LADIES GARME': 'Shopping_Retail', 'HANANI FLOWERS N CAKES': 'Shopping_Retail',
    'HANANI FLOWERS N': 'Shopping_Retail', 'EMIRATES PALACE': 'Travel', 'INDIA PALACE MUSHRIF': 'Food_Dining',
    'SUN AND SAND SPORTS': 'Shopping_Retail', 'SUN AND SAND SPORTS LL': 'Shopping_Retail', 'HUBBERS SPORTS EQUIPMENT': 'Shopping_Retail',
    'REHLAT INTERNET AND MU': 'Travel', 'COMICAVE TOYS & GAMES': 'Shopping_Retail', 'SP LTT STORE': 'Shopping_Retail',
    'SP LTTSTORE GLOBAL': 'Shopping_Retail', 'EXPO OFCL STORE': 'Shopping_Retail',
    'RADISSON RED HOTEL FNB': 'Food_Dining', 'SERV QUEST RES EXPO202': 'Food_Dining', 'KEFI BOOKS COFFEE S': 'Food_Dining',
    'KEFI BOOKS COFFEE SHO': 'Food_Dining', 'TASTY GARDEN RESTAURANT': 'Food_Dining', 'WAITROSE FINE FARE': 'Groceries',
    'LIBRO.FM AUDIOBOOKS': 'Digital_Subscriptions', 'FAKEEH UNIVERSITY HOSP': 'Health_Wellness', 'KINGS COLLEGE HOSPITAL': 'Health_Wellness',
    'AMERICAN EAGLE': 'Shopping_Retail', '% ARABICA': 'Food_Dining', 'LIWA TRDG ENT(LOVISA)': 'Shopping_Retail',
    'MUMUSO GENERAL TRD': 'Shopping_Retail', 'MINISO GENERAL TRADING5': 'Shopping_Retail', 'MINISO GENERAL TRADING2': 'Shopping_Retail',
    'HOUSE OF DONUTS': 'Food_Dining', 'KARACHI DARBAR KITCH': 'Food_Dining', 'TICKETMASTER': 'Entertainment',
    'MASTER CONV': 'Others', 'DUNES HOSPITALITY': 'Food_Dining', 'DASH HOSPITALITY GROUP': 'Food_Dining',
    'IRON WAVES BOAT RENT': 'Entertainment', 'IRON WAVES BOAT': 'Entertainment',
    'PRIVATEINTERNETACCESS': 'Digital_Subscriptions', 'PRIVATEINTERNETACCES': 'Digital_Subscriptions',
    'WISEWAY (TOOLZU.COM)': 'Digital_Subscriptions',
    'ETIHAD CREDIT BUREAU': 'Government_Fees', 'AL ETIHAD CREDIT BUR': 'Government_Fees', 'HOMEELIFE': 'Utilities_Telecom', 'HOMEDEWA': 'Utilities_Telecom',
    'EMIRATES': 'Travel', 'EMIRATES-AED': 'Travel', 'AIR BLUE': 'Travel', 'TELEPHONE': 'Utilities_Telecom',
    'TFL UNPAID FARES TFL.GOV.UK CP': 'Government_Fees', 'SMART CENTER': 'Government_Fees', 'NOQ RDC DEPOSITS': 'Government_Fees',
    'DISTRICT ONE FZ': 'Housing_Education', 'MEYDAN GROUP LLC': 'Housing_Education', 'SILICON OASIS HO': 'Housing_Education',
    'AL AIN SCIENCE AND TEC': 'Housing_Education', 'ADVANCED CNT DAY': 'Housing_Education', 'TLR AMERICANCENTERUAE': 'Housing_Education',
    'MEETNTRAIN': 'Housing_Education', 'FIXIT INV LLC-JEBEL AL': 'Housing_Education', 'BUBBLE CARE EXPR': 'Housing_Education',
    'WHITE AND SHINY CLEA': 'Housing_Education', 'SMART DUBAI - DP': 'Government_Fees',
    'SAAED FOR TRAFFIC SYST AB U DHABI': 'Government_Fees', 'DUBAI': 'Travel',
    'TRUST IT SKILLS - FZ': 'Shopping_Retail', 'SPADES APP FZ LLC': 'Food_Dining',
    'AREEJ': 'Shopping_Retail', 'SWISS ARABIAN-AB': 'Shopping_Retail', 'THE NATURE BEAUTY FLOW': 'Shopping_Retail',
    'THE NATURE BEAUTY FLOWE': 'Shopping_Retail', 'THE NATURE BEAUTY': 'Shopping_Retail', 'SADAQA LADIES WEARS TA': 'Shopping_Retail',
    'FINE CITY LANDSCAPE LL': 'Shopping_Retail', 'AL GHOUB NURSERY': 'Shopping_Retail', 'NEW SALAH ALDIN': 'Health_Wellness', 'NEW SALAHALDIN': 'Health_Wellness', 'ODD': 'Health_Wellness',
}
CITY = re.compile(r'\b(?:DU ?BAI|AB ?U ?DHABI|ABU ?DHABI|ABUDHABI|SHARJAH|SHJ|AJMAN|AUH|DXB|UAE|AE)\b', re.I)

def suggest(merchant_clean, raw=''):
    if merchant_clean in OVERRIDES:
        return OVERRIDES[merchant_clean], 'manual', 'high'
    if merchant_clean == 'UNKNOWN MERCHANT':
        return 'Others', 'rule', 'low'
    if merchant_clean in BRAND:
        return BRAND[merchant_clean], 'brand', 'medium' if merchant_clean in AMBIGUOUS else 'high'
    text = CITY.sub(' ', f'{merchant_clean} {raw}')
    for cat, rx in KEYWORDS:
        if rx.search(text):
            return cat, 'keyword', 'medium'
    return None, None, None
