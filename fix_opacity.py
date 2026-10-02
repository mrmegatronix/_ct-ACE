import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix signage-card-gold
css = re.sub(
    r"\.signage-card-gold \{\s*background: rgba\(14, 17, 24, 0\.94\);\s*backdrop-filter: blur\(24px\);\s*-webkit-backdrop-filter: blur\(24px\);",
    ".signage-card-gold {\n    background: rgba(14, 17, 24, 0.45);\n    backdrop-filter: blur(8px);\n    -webkit-backdrop-filter: blur(8px);",
    css
)

# Fix signage-card-amber
css = re.sub(
    r"\.signage-card-amber \{\s*background: rgba\(14, 17, 24, 0\.94\);\s*backdrop-filter: blur\(24px\);\s*-webkit-backdrop-filter: blur\(24px\);",
    ".signage-card-amber {\n    background: rgba(14, 17, 24, 0.45);\n    backdrop-filter: blur(8px);\n    -webkit-backdrop-filter: blur(8px);",
    css
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

