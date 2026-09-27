import re
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
# Replace the second const pad definition
text = re.sub(r'// Update DOM\s*const pad = \(n\) => n < 10 \? \'0\' \+ n : n;\s*', r'// Update DOM\n            ', text)
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
