import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

new_parse = """
        function parseSignageCsv(text) {
            if (!text) return null;
            const lines = text.trim().split(/\\r?\\n/).map(line => line.split(','));
            if (lines.length < 3) return null;

            let jackpot = 500;
            let flipped = 0;
            let remaining = 52;
            let chance = '1.92%';

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

            let lastCompletedRow = null;

            for (let i = 2; i < lines.length; i++) {
                const row = lines[i];
                if (row.length < 4) continue;
                
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
                chance = lastCompletedRow[4] ? lastCompletedRow[4].trim() : '1.92%';
            }

            flipped = Math.max(0, Math.min(52, flipped));
            remaining = 52 - flipped;

            return { jackpot, remaining, flipped, chance };
        }
"""
index = re.sub(
    r'function parseSignageCsv.*?return \{ jackpot, remaining, flipped, labelA2, labelB2 \};\s*\}',
    new_parse.strip(),
    index,
    flags=re.DOTALL
)

# Update fetch block
new_fetch = """
                    const parsed = parseSignageCsv(text);
                    if (parsed) {
                        localStorage.setItem('cta_jackpot', parsed.jackpot);
                        localStorage.setItem('cta_cards_remaining', parsed.remaining);
                        localStorage.setItem('cta_cards_flipped', parsed.flipped);
                        localStorage.setItem('cta_winning_chance', parsed.chance);
                    }
"""
index = re.sub(
    r'const parsed = parseSignageCsv\(text\);\s*if \(parsed\) \{\s*localStorage\.setItem\(\'cta_jackpot\', parsed\.jackpot\);\s*localStorage\.setItem\(\'cta_cards_remaining\', parsed\.remaining\);\s*localStorage\.setItem\(\'cta_cards_flipped\', parsed\.flipped\);\s*\}',
    new_fetch.strip(),
    index,
    flags=re.DOTALL
)

# Update updateCardCountdown in index.html
new_vault = """
        function updateCardCountdown() {
            const storedRemaining = localStorage.getItem('cta_cards_remaining');
            const storedFlipped = localStorage.getItem('cta_cards_flipped');
            const storedChance = localStorage.getItem('cta_winning_chance') || '1.92%';
            
            let remaining = storedRemaining !== null ? parseInt(storedRemaining) : 36;
            let flipped = storedFlipped !== null ? parseInt(storedFlipped) : 16;
            let chance = storedChance;

            if (isGameplayPaused) {
                remaining = 0;
                // Rely on the CSV's "flipped" (0) and "chance" (0.00%) for the paused state
            }

            const remainingEl = document.getElementById('vault-remaining-num');
            const flippedEl = document.getElementById('vault-flipped-num');
            const oddsEl = document.getElementById('vault-odds-display');
            const fannedTop = document.getElementById('card-fanned-flipped-top');
            const fannedBot = document.getElementById('card-fanned-flipped-bot');

            if (remainingEl) remainingEl.innerText = remaining;
            if (flippedEl) flippedEl.innerText = `${flipped} CARDS`;
            if (oddsEl) oddsEl.innerText = chance === '0.00%' ? '0.00%' : chance;
            if (fannedTop) fannedTop.innerText = isGameplayPaused ? '-' : `#${flipped}`;
            if (fannedBot) fannedBot.innerText = isGameplayPaused ? '-' : `#${flipped}`;
        }
"""
index = re.sub(
    r'function updateCardCountdown\(\) \{.*?if \(fannedBot\) fannedBot\.innerText = isGameplayPaused \? \'-\' : `#\$\{flipped\}`;.*?\}',
    new_vault.strip(),
    index,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

new_preview_vault = """
            // Sync Safe Vault Card Deck Countdown
            const storedRemaining = localStorage.getItem('cta_cards_remaining');
            const storedFlipped = localStorage.getItem('cta_cards_flipped');
            const storedChance = localStorage.getItem('cta_winning_chance') || '1.92%';
            
            let remaining = storedRemaining !== null ? parseInt(storedRemaining) : 36;
            let flipped = storedFlipped !== null ? parseInt(storedFlipped) : 16;
            let chance = storedChance;

            if (isPaused) {
                remaining = 0;
            }

            const remainingEl = document.getElementById('vault-remaining-num');
            const flippedEl = document.getElementById('vault-flipped-num');
            const oddsEl = document.getElementById('vault-odds-display');
            const fannedTop = document.getElementById('card-fanned-flipped-top');
            const fannedBot = document.getElementById('card-fanned-flipped-bot');

            if (remainingEl) remainingEl.innerText = remaining;
            if (flippedEl) flippedEl.innerText = `${flipped} CARDS`;
            if (oddsEl) oddsEl.innerText = chance === '0.00%' ? '0.00%' : chance;
            if (fannedTop) fannedTop.innerText = isPaused ? '-' : `#${flipped}`;
            if (fannedBot) fannedBot.innerText = isPaused ? '-' : `#${flipped}`;
"""
preview = re.sub(
    r'// Sync Safe Vault Card Deck Countdown.*?if \(fannedBot\) fannedBot\.innerText = isPaused \? \'-\' : `#\$\{flipped\}`;',
    new_preview_vault.strip(),
    preview,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

