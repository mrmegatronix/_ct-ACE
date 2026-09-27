import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

def get_slide(slide_id):
    match = re.search(r'(<div class="slide[^"]*" id="' + slide_id + r'".*?</div>\s*</div>)', index, re.DOTALL)
    if not match:
        # Some slides don't have double nested closing divs, but all of our redesigned ones do (because of signage-card-gold)
        # Actually, let's just use a more robust extractor: match until the next `<!-- Slide` or `</div>\s*</div>\s*<!-- Progress Bar`
        pattern = r'(<div class="slide[^"]*" id="' + slide_id + r'".*?)(?:\n\s*<!-- Slide|\n\s*</div>\s*<!-- Progress Bar)'
        match = re.search(pattern, index, re.DOTALL)
        if match:
            # Need to close the outermost div that was omitted by the lookahead
            return match.group(1).strip()
        else:
            return ""
    return match.group(1).strip()

slides = {
    'slide-main': get_slide('slide-main'),
    'slide-jackpot': get_slide('slide-jackpot'),
    'countdown-slide': get_slide('countdown-slide'),
    'next-draw-slide': get_slide('next-draw-slide'),
    'slide-winner': get_slide('slide-winner'),
    'slide-hall-of-winners': get_slide('slide-hall-of-winners')
}

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

# Replace slide-main
preview = re.sub(r'<div class="slide" id="slide-main">.*?</h2>\s*</div>', slides['slide-main'], preview, flags=re.DOTALL)

# Replace slide-jackpot
preview = re.sub(r'<div class="slide" id="slide-jackpot">.*?</div>\s*</div>', slides['slide-jackpot'], preview, flags=re.DOTALL)

# Replace countdown-slide
preview = re.sub(r'<div class="slide" id="countdown-slide">.*?</div>\s*</div>', slides['countdown-slide'], preview, flags=re.DOTALL)

# Replace next-draw-slide
preview = re.sub(r'<div class="slide" id="next-draw-slide">.*?</h2>\s*</div>', slides['next-draw-slide'], preview, flags=re.DOTALL)

# Replace slide-winner
preview = re.sub(r'<div class="slide" id="slide-winner">.*?</div>\s*</div>', slides['slide-winner'], preview, flags=re.DOTALL)

# Insert slide-hall-of-winners after slide-winner if not present
if 'id="slide-hall-of-winners"' not in preview:
    hall_of_winners_block = f"""
        </div>

        <!-- Slide 9 -->
        <div>
            <div class="slide-title-bar">Hall of Winners</div>
            <div class="slide-wrapper">
                {slides['slide-hall-of-winners']}
            </div>
"""
    preview = preview.replace('<!-- Navigation Hub', hall_of_winners_block + '\n    </div>\n\n    <!-- Navigation Hub')

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

