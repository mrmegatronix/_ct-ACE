import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

index = re.sub(
    r"localStorage\.setItem\('cta_cards_flipped', parsed\.flipped\);\s*\}",
    "localStorage.setItem('cta_cards_flipped', parsed.flipped);\n                            localStorage.setItem('cta_winning_chance', parsed.chance);\n                        }",
    index
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(index)
