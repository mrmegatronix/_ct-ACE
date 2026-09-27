import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

new_jackpot = """
            // Fetch Jackpot 
            const storedJackpot = localStorage.getItem('cta_jackpot') || localStorage.getItem('cta_jackpot_backup');
            if (isPaused) {
                document.getElementById('display-jackpot').innerText = "$0.00";
            } else if (storedJackpot) {
                document.getElementById('display-jackpot').innerText = new Intl.NumberFormat('en-NZ', { style: 'currency', currency: 'NZD' }).format(storedJackpot);
            }
"""
preview = re.sub(
    r"// Fetch Jackpot\s*const storedJackpot = localStorage\.getItem\('cta_jackpot'\) \|\| localStorage\.getItem\('cta_jackpot_backup'\);\s*if \(storedJackpot\) \{\s*document\.getElementById\('display-jackpot'\)\.innerText = new Intl\.NumberFormat\('en-US', \{ style: 'currency', currency: 'NZD' \}\)\.format\(storedJackpot\);\s*\}",
    new_jackpot.strip(),
    preview,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)
