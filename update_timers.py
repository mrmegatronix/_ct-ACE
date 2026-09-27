import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_shouldShow = """
        function shouldShowSlide(slide) {
            const now = new Date();
            const nzTimeStr = now.toLocaleString("en-US", { timeZone: "Pacific/Auckland" });
            const nzDate = new Date(nzTimeStr);

            const slideId = slide.id;

            if (isGameplayPaused) {
                // Show main, jackpot, next-draw, winner, and hall of winners. Skip "countdown-slide" (draw starts in) because there is no draw imminent.
                return slideId === 'slide-main' || slideId === 'slide-jackpot' || slideId === 'next-draw-slide' || slideId === 'slide-winner' || slideId === 'slide-hall-of-winners';
            }

            // Normal rotation: hide the winner announcement slide
            if (slideId === 'slide-winner') return false;

            // Countdown vs Next Draw logic
            if (slideId === 'countdown-slide' && !isCountdownActive) return false;
            if (slideId === 'next-draw-slide' && isCountdownActive) return false;

            return true;
        }
"""
content = re.sub(
    r'function shouldShowSlide.*?return true;\s*\}',
    new_shouldShow.strip(),
    content,
    flags=re.DOTALL
)

new_countdown_logic = """
        // --- Countdown Logic (NZ Time) ---
        function updateCountdown() {
            if (isGameplayPaused) {
                isCountdownActive = false;
                document.getElementById('cd-d').innerText = '00';
                document.getElementById('cd-h').innerText = '00';
                document.getElementById('cd-m').innerText = '00';
                document.getElementById('cd-s').innerText = '00';
                return;
            }

            const now = new Date();
            // Create date object based on NZ time
"""
content = re.sub(
    r'// --- Countdown Logic \(NZ Time\) ---\s*function updateCountdown\(\) \{\s*const now = new Date\(\);\s*// Create date object based on NZ time',
    new_countdown_logic.strip(),
    content,
    flags=re.DOTALL
)

new_nextdraw_logic = """
        // --- Global Next Draw Countdown Logic ---
        function updateNextDrawTimer() {
            const pad = (n) => n < 10 ? '0' + n : n;
            
            if (isGameplayPaused) {
                document.getElementById('nd-d').innerText = '00';
                document.getElementById('nd-h').innerText = '00';
                document.getElementById('nd-m').innerText = '00';
                document.getElementById('nd-s').innerText = '00';
                document.getElementById('next-draw-label').innerText = "PAUSED UNTIL JACKPOT HITS $500";
                return;
            }

            const now = new Date();
            const nzTimeStr = now.toLocaleString("en-US", { timeZone: "Pacific/Auckland" });
            const nzDate = new Date(nzTimeStr);
"""
content = re.sub(
    r'// --- Global Next Draw Countdown Logic ---\s*function updateNextDrawTimer\(\) \{\s*const now = new Date\(\);\s*const nzTimeStr = now\.toLocaleString\("en-US", \{ timeZone: "Pacific/Auckland" \}\);\s*const nzDate = new Date\(nzTimeStr\);',
    new_nextdraw_logic.strip(),
    content,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
