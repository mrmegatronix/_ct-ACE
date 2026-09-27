import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Change hardcoded main slide subtitle
index = index.replace(
    'JOIN US FOR OUR TWO WEEKLY DRAWS: TUESDAYS & SATURDAYS',
    'GAME PLAY IS CURRENTLY PAUSED AND WILL RESET IN A FEW WEEKS<br>BUILDING BACK TO $500!'
)

# Force jackpot to 0 if paused, and flipped to 0
new_vault_logic = """
            if (isGameplayPaused) {
                remaining = 0;
                flipped = 0;
                chance = '0.00%';
            }
"""
index = re.sub(
    r"if \(isGameplayPaused\) \{\s*remaining = 0;\s*// Rely on the CSV's \"flipped\" \(0\) and \"chance\" \(0\.00%\) for the paused state\s*\}",
    new_vault_logic.strip(),
    index,
    flags=re.DOTALL
)

# Force jackpot to $0.00 if paused
new_jackpot_logic = """
                if (isGameplayPaused) {
                    displayEl.innerText = "$0.00";
                } else {
                    const storedAmount = localStorage.getItem('cta_jackpot') || localStorage.getItem('cta_jackpot_backup');
                    if (storedAmount) displayEl.innerText = new Intl.NumberFormat('en-NZ', { style: 'currency', currency: 'NZD' }).format(storedAmount);
                    else if (displayEl.innerText === "$0.00") displayEl.innerText = "$500.00";
                }
"""
index = re.sub(
    r"const storedAmount = localStorage\.getItem\('cta_jackpot'\) \|\| localStorage\.getItem\('cta_jackpot_backup'\);\s*if \(storedAmount\) displayEl\.innerText = new Intl\.NumberFormat\('en-US', \{ style: 'currency', currency: 'NZD' \}\)\.format\(storedAmount\);\s*else if \(displayEl\.innerText === \"\$0\.00\"\) displayEl\.innerText = \"\$500\.00\";",
    new_jackpot_logic.strip(),
    index,
    flags=re.DOTALL
)

# Also fix the fetch success block to override jackpot if paused
new_fetch_jackpot = """
                    const parsed = parseSignageCsv(text);
                    if (parsed) {
                        if (!isNaN(parsed.jackpot) && parsed.jackpot >= 0) {
                            if (isGameplayPaused) {
                                displayEl.innerText = "$0.00";
                            } else {
                                displayEl.innerText = new Intl.NumberFormat('en-NZ', { style: 'currency', currency: 'NZD' }).format(parsed.jackpot);
                            }
"""
index = re.sub(
    r"const parsed = parseSignageCsv\(text\);\s*if \(parsed\) \{\s*if \(\!isNaN\(parsed\.jackpot\) && parsed\.jackpot > 0\) \{\s*displayEl\.innerText = new Intl\.NumberFormat\('en-NZ', \{ style: 'currency', currency: 'NZD' \}\)\.format\(parsed\.jackpot\);",
    new_fetch_jackpot.strip(),
    index,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

# Change hardcoded main slide subtitle in preview.html
preview = preview.replace(
    'JOIN US FOR OUR TWO WEEKLY DRAWS: TUESDAYS & SATURDAYS',
    'GAME PLAY IS CURRENTLY PAUSED AND WILL RESET IN A FEW WEEKS<br>BUILDING BACK TO $500!'
)

# Force vault zeroing in preview.html
new_preview_vault_logic = """
            if (isPaused) {
                remaining = 0;
                flipped = 0;
                chance = '0.00%';
            }
"""
preview = re.sub(
    r"if \(isPaused\) \{\s*remaining = 0;\s*\}",
    new_preview_vault_logic.strip(),
    preview,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

