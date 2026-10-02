with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the aggressive global overrides from the first attempt
css = css.replace("""/* 1. Global Font Consistency & Anti-Clipping */
.slide h2, .slide h3, .slide .font-headline {
    font-family: 'Playfair Display', serif !important;
    white-space: nowrap !important;
}""", "")

css = css.replace(""".slide-fullscreen [style*="letter-spacing: 4px"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 44px !important;
    white-space: nowrap !important;
    line-height: 1.2 !important;
    font-weight: 800 !important;
}""", "")

# Add Playfair strictly to .unified-title and .font-headline in the unified section if it's missing
# (It's already in .unified-title)
if ".font-headline {" not in css:
    css = css.replace(".unified-title {", ".font-headline, .unified-title {\n    font-family: 'Playfair Display', serif !important;")

# Ensure text-main-subtitle and next-draw-label explicitly use Inter
css += """
#text-main-subtitle, #next-draw-label, .unified-subtitle {
    font-family: 'Inter', sans-serif !important;
}
"""

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
