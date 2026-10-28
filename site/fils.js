// Fils the owl: original SVG mascot (named after the fils, the smallest UAE coin).
// Banker look: navy coat, red bow tie, gold spectacles, top hat, ledger tucked under his wing.
// fils(opts) returns an SVG string. opts: {size, mood:'happy'|'wave'|'think'}
window.fils = function (o = {}) {
  const s = o.size || 200, m = o.mood || 'happy';
  const body = '#8B5E3C', dark = '#6E4A2F', face = '#F1E2C6', belly = '#E8D3B0',
        coat = '#1F3A5F', lapel = '#2E5283', gold = '#D4A72C', tie = '#B23A48',
        beak = '#E9A23B', ink = '#2B1D14', hat = '#22222B', hatEdge = '#4A4A5A',
        book = '#7A2E2E', paper = '#FBF6EA';
  const px = m === 'think' ? 5 : 0, py = m === 'think' ? -6 : 0;

  const leftWing = m === 'wave'
    ? `<path d="M70,196 C46,176 36,140 44,106 C47,96 58,96 60,106 C62,138 74,164 92,182 Z" fill="${dark}"/>
       <path d="M48,104 l-6,-10 M56,100 l0,-12 M64,104 l6,-10" stroke="${dark}" stroke-width="6" stroke-linecap="round"/>`
    : m === 'think'
    ? `<ellipse cx="104" cy="172" rx="15" ry="30" fill="${dark}" transform="rotate(38 104 172)"/>`
    : `<ellipse cx="84" cy="230" rx="16" ry="28" fill="${dark}"/>`;

  return `<svg width="${s}" height="${s}" viewBox="0 0 200 200" aria-hidden="true">
  <ellipse cx="100" cy="194" rx="52" ry="5" fill="rgba(0,0,0,.18)"/>
  <g transform="translate(16 18.8) scale(0.6)">
  <ellipse cx="140" cy="195" rx="86" ry="95" fill="${body}"/>
  <ellipse cx="140" cy="112" rx="80" ry="68" fill="${body}"/>
  <path d="M72,70 L66,30 L104,56Z" fill="${dark}"/><path d="M208,70 L214,30 L176,56Z" fill="${dark}"/>
  <path d="M140,170 Q100,180 104,282 L176,282 Q180,180 140,170Z" fill="${belly}"/>
  <path d="M58,165 Q48,250 86,285 L122,285 L116,175 Q88,152 58,165Z" fill="${coat}"/>
  <path d="M222,165 Q232,250 194,285 L158,285 L164,175 Q192,152 222,165Z" fill="${coat}"/>
  <path d="M116,175 L128,200 L120,206Z" fill="${lapel}"/><path d="M164,175 L152,200 L160,206Z" fill="${lapel}"/>
  <circle cx="124" cy="226" r="3.5" fill="${gold}"/><circle cx="124" cy="246" r="3.5" fill="${gold}"/><circle cx="124" cy="266" r="3.5" fill="${gold}"/>
  <path d="M140,176 L124,166 L124,186 Z M140,176 L156,166 L156,186 Z" fill="${tie}"/><circle cx="140" cy="176" r="5" fill="${tie}"/>
  <circle cx="112" cy="110" r="30" fill="${face}"/><circle cx="168" cy="110" r="30" fill="${face}"/>
  <circle cx="112" cy="110" r="17" fill="#fff"/><circle cx="168" cy="110" r="17" fill="#fff"/>
  <circle cx="${112 + px}" cy="${111 + py}" r="11" fill="${ink}"/><circle cx="${168 + px}" cy="${111 + py}" r="11" fill="${ink}"/>
  <circle cx="${116 + px}" cy="${106 + py}" r="4" fill="#fff"/><circle cx="${172 + px}" cy="${106 + py}" r="4" fill="#fff"/>
  <circle cx="112" cy="110" r="24" fill="none" stroke="${gold}" stroke-width="3.5"/><circle cx="168" cy="110" r="24" fill="none" stroke="${gold}" stroke-width="3.5"/>
  <line x1="136" y1="108" x2="144" y2="108" stroke="${gold}" stroke-width="3.5"/>
  <path d="M132,132 L148,132 L140,148Z" fill="${beak}"/>
  <g transform="rotate(-8 175 234)">
    <rect x="150" y="196" width="50" height="76" rx="3" fill="${book}"/>
    <rect x="156" y="204" width="38" height="8" fill="${gold}"/>
    <rect x="196" y="200" width="5" height="70" fill="${paper}"/>
  </g>
  <ellipse cx="198" cy="236" rx="16" ry="28" fill="${dark}"/>
  ${leftWing}
  <ellipse cx="120" cy="288" rx="14" ry="6" fill="${beak}"/><ellipse cx="160" cy="288" rx="14" ry="6" fill="${beak}"/>
  <g transform="rotate(-6 140 50)">
    <rect x="100" y="-24" width="80" height="74" rx="3" fill="${hat}" stroke="${hatEdge}" stroke-width="2.5"/>
    <rect x="108" y="-18" width="9" height="44" rx="3" fill="${hatEdge}" opacity=".7"/>
    <rect x="100" y="30" width="80" height="12" fill="${book}"/>
    <ellipse cx="140" cy="52" rx="62" ry="10" fill="${hat}" stroke="${hatEdge}" stroke-width="2.5"/>
  </g>
  </g>
</svg>`;
};
