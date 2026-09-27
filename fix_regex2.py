import re
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'split\(\/\n\/\)', r'split(/\\r?\\n/)', text)
text = re.sub(r'split\(\/\r\n\/\)', r'split(/\\r?\\n/)', text)
text = re.sub(r'split\(\/\?\n\/\)', r'split(/\\r?\\n/)', text)
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
