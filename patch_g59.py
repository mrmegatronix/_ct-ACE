import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_logic = """
            // Read Jackpot Total specifically from G59 (row index 58, col index 6)
            if (lines.length > 58 && lines[58].length > 6) {
                const rawJackpot = lines[58][6] ? lines[58][6].replace(/[^0-9.]/g, '') : '';
                if (rawJackpot) jackpot = parseFloat(rawJackpot);
            } else {
                // Fallback scan
                for (let i = lines.length - 1; i >= 0; i--) {
                    const row = lines[i];
                    if (row.length > 6 && typeof row[5] === 'string' && row[5].includes('JACKPOT TOTAL:')) {
                        const rawJackpot = row[6] ? row[6].replace(/[^0-9.]/g, '') : '';
                        if (rawJackpot) jackpot = parseFloat(rawJackpot);
                        break;
                    }
                }
            }
"""

content = re.sub(
    r'// Find Jackpot Total \(usually at bottom\).*?break;\s*\}\s*\}',
    new_logic.strip(),
    content,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

