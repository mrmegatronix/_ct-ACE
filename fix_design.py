import re

CSS_ADDITIONS = """
/* --- UNIFIED DESIGN & ANIMATIONS --- */
.unified-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 130px !important;
    line-height: 0.95 !important;
    letter-spacing: 2px !important;
    color: #ffffff !important;
    text-transform: uppercase !important;
    margin: 0 !important;
    white-space: nowrap !important;
}

.unified-subtitle {
    font-family: 'Inter', sans-serif !important;
    font-size: 44px !important;
    font-weight: 800 !important;
    color: #d4af37 !important;
    letter-spacing: 5px !important;
    text-transform: uppercase !important;
    margin-top: 10px !important;
    white-space: nowrap !important;
}

.unified-subtitle-amber {
    color: #f59e0b !important;
}

/* Animations */
@keyframes slideUpFadeIn {
    0% { opacity: 0; transform: translateY(40px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes pulseGlowGold {
    0%, 100% { box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(212, 175, 55, 0.15); }
    50% { box-shadow: 0 35px 70px rgba(0, 0, 0, 0.9), 0 0 60px rgba(212, 175, 55, 0.4); }
}

@keyframes pulseGlowAmber {
    0%, 100% { box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(245, 158, 11, 0.15); }
    50% { box-shadow: 0 35px 70px rgba(0, 0, 0, 0.9), 0 0 60px rgba(245, 158, 11, 0.4); }
}

.slide.active .signage-card-gold {
    animation: slideUpFadeIn 0.7s cubic-bezier(0.2, 0.8, 0.2, 1) forwards, pulseGlowGold 6s ease-in-out infinite alternate !important;
}

.slide.active .signage-card-amber {
    animation: slideUpFadeIn 0.7s cubic-bezier(0.2, 0.8, 0.2, 1) forwards, pulseGlowAmber 6s ease-in-out infinite alternate !important;
}

/* Specific Scale-ups */
#text-main-title { font-size: 190px !important; }
#text-main-subtitle { font-size: 52px !important; line-height: 1.3 !important; font-family: 'Playfair Display', serif !important; }
#slide-winner h2 { font-size: 160px !important; }
#display-winner-ticket { font-size: 160px !important; }
#display-winner-name { font-size: 130px !important; }
#display-jackpot { font-size: 280px !important; }
#timer-display { font-size: 220px !important; }

/* Scale up the rule rows and prevent wrapping */
.signage-row {
    padding: 24px 30px !important;
    gap: 25px !important;
    white-space: nowrap !important;
    background: rgba(6, 8, 13, 0.6) !important;
    border: 2px solid rgba(255,255,255,0.1) !important;
}
.signage-row span {
    font-size: 48px !important;
}
.signage-row .material-symbols-outlined {
    font-size: 64px !important;
}
.signage-row * {
    white-space: nowrap !important;
}
"""

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
if '/* --- UNIFIED DESIGN & ANIMATIONS --- */' not in css:
    with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + CSS_ADDITIONS)

def replace_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Unified Titles
    html = re.sub(
        r'class="font-headline"\s+style="font-size:\s*(?:104|98|90)px[^"]*"',
        'class="unified-title"',
        html
    )

    # Unified Subtitles (Gold)
    html = re.sub(
        r'style="font-size: 28px; font-weight: 800; color: #d4af37; letter-spacing: 4px; text-transform: uppercase; margin-top: 6px;"',
        'class="unified-subtitle"',
        html
    )
    
    # Unified Subtitles (Amber)
    html = re.sub(
        r'style="font-size: 28px; font-weight: 800; color: #f59e0b; letter-spacing: 4px; text-transform: uppercase; margin-top: 6px;"',
        'class="unified-subtitle unified-subtitle-amber"',
        html
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

replace_in_file('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html')
replace_in_file('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html')
