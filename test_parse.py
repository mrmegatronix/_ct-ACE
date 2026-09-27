import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'function parseSignageCsv.*?return \{ jackpot, remaining, flipped, labelA2, labelB2 \};\s*\}', text, re.DOTALL)
if match:
    print(match.group(0))
