import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Update updateCountdown JS
index = re.sub(r"document\.getElementById\('cd-d'\)\.innerText = '00';", "document.getElementById('cd-d').innerHTML = '♠♠';", index)
index = re.sub(r"document\.getElementById\('cd-h'\)\.innerText = '00';", "document.getElementById('cd-h').innerHTML = '♠♠';", index)
index = re.sub(r"document\.getElementById\('cd-m'\)\.innerText = '00';", "document.getElementById('cd-m').innerHTML = '♠♠';", index)
index = re.sub(r"document\.getElementById\('cd-s'\)\.innerText = '00';", "document.getElementById('cd-s').innerHTML = '♠♠';", index)

# Update updateNextDrawTimer JS
index = re.sub(r"document\.getElementById\('nd-d'\)\.innerText = '00';", "document.getElementById('nd-d').innerHTML = '♠♠';", index)
index = re.sub(r"document\.getElementById\('nd-h'\)\.innerText = '00';", "document.getElementById('nd-h').innerHTML = '♠♠';", index)
index = re.sub(r"document\.getElementById\('nd-m'\)\.innerText = '00';", "document.getElementById('nd-m').innerHTML = '♠♠';", index)
index = re.sub(r"document\.getElementById\('nd-s'\)\.innerText = '00';", "document.getElementById('nd-s').innerHTML = '♠♠';", index)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

# Update preview static HTML
preview = re.sub(r'<span id="cd-d">00</span>', '<span id="cd-d">♠♠</span>', preview)
preview = re.sub(r'<span id="cd-h">00</span>', '<span id="cd-h">♠♠</span>', preview)
preview = re.sub(r'<span id="cd-m">00</span>', '<span id="cd-m">♠♠</span>', preview)
preview = re.sub(r'<span id="cd-s">00</span>', '<span id="cd-s">♠♠</span>', preview)

preview = re.sub(r'<span id="nd-d">00</span>', '<span id="nd-d">♠♠</span>', preview)
preview = re.sub(r'<span id="nd-h">00</span>', '<span id="nd-h">♠♠</span>', preview)
preview = re.sub(r'<span id="nd-m">00</span>', '<span id="nd-m">♠♠</span>', preview)
preview = re.sub(r'<span id="nd-s">00</span>', '<span id="nd-s">♠♠</span>', preview)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

