import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

preview = preview.replace(
    'subtitleEl.innerText = "GAMEPLAY TEMPORARILY ON HOLD";',
    'subtitleEl.innerHTML = "GAME PLAY IS CURRENTLY PAUSED AND WILL RESET IN A FEW WEEKS<br>BUILDING BACK TO $500!";'
)

preview = preview.replace(
    'const content = storedContent ? JSON.parse(storedContent) : null;\n                    subtitleEl.innerText =',
    'const content = storedContent ? JSON.parse(storedContent) : null;\n                    subtitleEl.innerHTML ='
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

