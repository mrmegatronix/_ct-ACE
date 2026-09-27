import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

new_logic = """
            // Dynamically adjust main subtitle text based on paused state
            let isPaused = localStorage.getItem('cta_paused') === 'true';
            const pauseEndDate = new Date('2026-10-13T00:00:00').getTime();
            if (Date.now() < pauseEndDate) {
                isPaused = true;
            }
"""

preview = re.sub(
    r"// Dynamically adjust main subtitle text based on paused state\s*const isPaused = localStorage\.getItem\('cta_paused'\) === 'true';",
    new_logic.strip(),
    preview,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

