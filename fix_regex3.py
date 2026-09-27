import re
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'split\(\/.*?\/\)\.map', 'split(/\\\\r?\\\\n/).map', text, flags=re.DOTALL)
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
