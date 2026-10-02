import re

def scale_font(match):
    size = int(match.group(1))
    
    # Scale up small fonts for TV
    if size == 20: size = 32
    elif size == 24: size = 36
    elif size == 26: size = 40
    elif size == 28: size = 44
    elif size == 30: size = 46
    elif size == 32: size = 48
    elif size == 40: size = 52
    elif size == 42: size = 54
    elif size == 46: size = 58
    elif size == 50: size = 62
    elif size == 52: size = 66
    elif size == 54: size = 68
    elif size == 56: size = 72
    elif size == 58: size = 76
    elif size == 64: size = 80
    elif size == 68: size = 86
    elif size == 76: size = 94
    elif size == 80: size = 96
    
    return f"font-size: {size}px"

for filename in ['/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', '/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Scale all explicitly defined font sizes
    html = re.sub(r'font-size:\s*([0-9]+)px', scale_font, html)

    # Standardize fonts by ensuring Playfair Display (font-headline) is used for subtitles that look out of place in Inter
    html = html.replace('font-weight: 800; color: #d4af37; letter-spacing: 4px; text-transform: uppercase;', 'font-weight: 800; color: #d4af37; letter-spacing: 4px; text-transform: uppercase; font-family: \'Playfair Display\', serif;')
    
    # Ensure "COASTERS TAVERN WEEKLY EVENT" uses Playfair
    html = html.replace('>COASTERS TAVERN WEEKLY EVENT<', ' class="font-headline">COASTERS TAVERN WEEKLY EVENT<')
    html = html.replace('>YOUR PATHWAY TO THE JACKPOT<', ' class="font-headline">YOUR PATHWAY TO THE JACKPOT<')
    html = html.replace('>LIVE REAL-TIME CARD DECK INVENTORY<', ' class="font-headline">LIVE REAL-TIME CARD DECK INVENTORY<')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
