import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

def get_slide(slide_id):
    pattern = r'(<div class="slide[^"]*" id="' + slide_id + r'".*?)(?:\n\s*<!-- Slide|\n\s*</div>\s*<!-- Progress Bar)'
    match = re.search(pattern, index, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

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

# I will replace each slide wrapper body entirely
for slide_id, html in slides.items():
    # Find the wrapper in preview.html and replace its contents
    # Pattern: <div class="slide[^"]*" id="slide_id"> ... until the end of the slide wrapper
    # In preview.html, the slide is inside <div class="slide-wrapper">
    preview = re.sub(
        r'(<div class="slide-wrapper">\s*)<div class="slide[^"]*" id="' + slide_id + r'".*?(?=\s*</div>\s*</div>\s*<!-- Slide|</div>\s*</div>\s*<!-- Navigation)',
        r'\1' + html.replace('\\', '\\\\'),
        preview,
        flags=re.DOTALL
    )

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

