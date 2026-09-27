import re

# Update index.html
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# 1. Add slide-vault to shouldShowSlide
index = re.sub(
    r"return slideId === 'slide-main' \|\| slideId === 'slide-jackpot' \|\| slideId === 'next-draw-slide' \|\| slideId === 'slide-winner' \|\| slideId === 'slide-hall-of-winners';",
    "return slideId === 'slide-main' || slideId === 'slide-jackpot' || slideId === 'next-draw-slide' || slideId === 'slide-winner' || slideId === 'slide-hall-of-winners' || slideId === 'slide-vault';",
    index
)

# 2. Update updateCardCountdown in index.html
new_vault_logic = """
        function updateCardCountdown() {
            const total = 52;
            const stored = localStorage.getItem('cta_cards_remaining') || 36;
            let remaining = Math.max(1, Math.min(total, parseInt(stored) || 36));
            let flipped = total - remaining;

            if (isGameplayPaused) {
                remaining = 0;
                flipped = 0;
            }

            const remainingEl = document.getElementById('vault-remaining-num');
            const flippedEl = document.getElementById('vault-flipped-num');
            const oddsEl = document.getElementById('vault-odds-display');
            const fannedTop = document.getElementById('card-fanned-flipped-top');
            const fannedBot = document.getElementById('card-fanned-flipped-bot');

            if (remainingEl) remainingEl.innerText = remaining;
            if (flippedEl) flippedEl.innerText = isGameplayPaused ? '0 CARDS' : `${flipped} CARDS`;
            if (oddsEl) oddsEl.innerText = isGameplayPaused ? 'PAUSED' : `1 IN ${remaining}`;
            if (fannedTop) fannedTop.innerText = isGameplayPaused ? '-' : `#${flipped}`;
            if (fannedBot) fannedBot.innerText = isGameplayPaused ? '-' : `#${flipped}`;
        }
"""
index = re.sub(
    r"function updateCardCountdown\(\) \{.*?if \(fannedBot\) fannedBot\.innerText = `#\$\{flipped\}`;.*?\}",
    new_vault_logic.strip(),
    index,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

# Update preview.html
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

new_preview_vault_logic = """
            // Sync Safe Vault Card Deck Countdown
            const totalCards = 52;
            const storedCards = localStorage.getItem('cta_cards_remaining') || 36;
            let remaining = Math.max(1, Math.min(totalCards, parseInt(storedCards) || 36));
            let flipped = totalCards - remaining;

            if (isPaused) {
                remaining = 0;
                flipped = 0;
            }

            const remainingEl = document.getElementById('vault-remaining-num');
            const flippedEl = document.getElementById('vault-flipped-num');
            const oddsEl = document.getElementById('vault-odds-display');
            const fannedTop = document.getElementById('card-fanned-flipped-top');
            const fannedBot = document.getElementById('card-fanned-flipped-bot');

            if (remainingEl) remainingEl.innerText = remaining;
            if (flippedEl) flippedEl.innerText = isPaused ? '0 CARDS' : `${flipped} CARDS`;
            if (oddsEl) oddsEl.innerText = isPaused ? 'PAUSED' : `1 IN ${remaining}`;
            if (fannedTop) fannedTop.innerText = isPaused ? '-' : `#${flipped}`;
            if (fannedBot) fannedBot.innerText = isPaused ? '-' : `#${flipped}`;
"""
preview = re.sub(
    r"// Sync Safe Vault Card Deck Countdown.*?if \(fannedBot\) fannedBot\.innerText = `#\$\{flipped\}`;",
    new_preview_vault_logic.strip(),
    preview,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

