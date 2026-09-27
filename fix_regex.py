with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('split(/?\\n/)', 'split(/\\r?\\n/)')
text = text.replace('split(/?\n/)', 'split(/\\r?\\n/)')
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
