import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_csv_logic = """
        function parseSignageCsv(text) {
            if (!text) return null;
            const lines = text.trim().split(/\\r?\\n/).map(line => line.split(','));
            if (lines.length < 3) return null;

            let jackpot = 500;
            let flipped = 0;
            let remaining = 52;
            let labelA2 = '';
            let labelB2 = '';

            // Find Jackpot Total (usually at bottom)
            for (let i = lines.length - 1; i >= 0; i--) {
                const row = lines[i];
                if (row.length > 6 && typeof row[5] === 'string' && row[5].includes('JACKPOT TOTAL:')) {
                    const rawJackpot = row[6] ? row[6].replace(/[^0-9.]/g, '') : '';
                    if (rawJackpot) jackpot = parseFloat(rawJackpot);
                    break;
                }
            }

            // Find max/current cards flipped by looking for the last COMPLETED row
            // A row is considered completed if the 'WINNING TICKET NUMBER' (col 7) or 'NAME OF WINNER' (col 8) is filled
            let lastCompletedRow = null;

            for (let i = 2; i < lines.length; i++) {
                const row = lines[i];
                if (row.length < 4) continue;
                
                // Col 7 is Ticket Number, Col 8 is Name, Col 9 is Card Drawn
                const ticketNum = row[7] ? row[7].trim() : '';
                const winnerName = row[8] ? row[8].trim() : '';
                const cardDrawn = (row.length > 9 && row[9]) ? row[9].trim() : '';
                
                if (ticketNum !== '' || winnerName !== '' || cardDrawn !== '') {
                    lastCompletedRow = row;
                }
            }

            if (lastCompletedRow) {
                const rawFlipped = lastCompletedRow[3] ? lastCompletedRow[3].replace(/[^0-9]/g, '') : '';
                flipped = rawFlipped !== '' ? parseInt(rawFlipped, 10) : 0;
            }

            flipped = Math.max(0, Math.min(52, flipped));
            remaining = 52 - flipped;

            return { jackpot, remaining, flipped, labelA2, labelB2 };
        }
"""

content = re.sub(
    r'function parseSignageCsv.*?return \{ jackpot, remaining, flipped, labelA2, labelB2 \};\s*\}',
    new_csv_logic.strip(),
    content,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
