import re

CSS_FIX = """
/* RESTORE BEBAS NEUE AND FIX GLOWS */
.font-headline, .unified-title {
    font-family: 'Bebas Neue', 'Outfit', sans-serif !important;
}

#text-main-title {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 260px !important; 
    line-height: 0.9 !important;
}

.unified-title {
    font-size: 150px !important;
    letter-spacing: 4px !important;
}

/* Make glows continuous regardless of active state for the preview */
@keyframes pulseGlowGoldStatic {
    0%, 100% { box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(212, 175, 55, 0.3); }
    50% { box-shadow: 0 35px 80px rgba(0, 0, 0, 0.9), 0 0 80px rgba(212, 175, 55, 0.6); }
}
@keyframes pulseGlowAmberStatic {
    0%, 100% { box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(245, 158, 11, 0.3); }
    50% { box-shadow: 0 35px 80px rgba(0, 0, 0, 0.9), 0 0 80px rgba(245, 158, 11, 0.6); }
}

.signage-card-gold {
    animation: pulseGlowGoldStatic 4s ease-in-out infinite alternate !important;
}
.signage-card-amber {
    animation: pulseGlowAmberStatic 4s ease-in-out infinite alternate !important;
}

/* Dynamic Entrance animations strictly for the active slide container */
@keyframes slideInUp {
    0% { opacity: 0; transform: translateY(50px) scale(0.98); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}
.slide.active > div {
    animation: slideInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards !important;
}
"""

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + CSS_FIX)

def add_bebas_to_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace the Google fonts link with one that includes Bebas Neue
    html = re.sub(
        r'href="https://fonts.googleapis.com/css2\?family=Playfair\+Display:wght@400;700;900&family=Inter:wght@300;400;600&family=Roboto:wght@400;700&display=swap"',
        r'href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;600&family=Roboto:wght@400;700&family=Bebas+Neue&family=Outfit:wght@400;500;600;700;800;900&display=swap"',
        html
    )
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

add_bebas_to_html('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html')
add_bebas_to_html('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html')
