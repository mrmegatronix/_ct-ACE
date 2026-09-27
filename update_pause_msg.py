import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update shouldShowSlide to include slide-jackpot
new_shouldShow = """
        function shouldShowSlide(slide) {
            const now = new Date();
            const nzTimeStr = now.toLocaleString("en-US", { timeZone: "Pacific/Auckland" });
            const nzDate = new Date(nzTimeStr);

            const slideId = slide.id;

            if (isGameplayPaused) {
                // When gameplay is paused, show main, jackpot, winner, and hall of winners
                return slideId === 'slide-main' || slideId === 'slide-jackpot' || slideId === 'slide-winner' || slideId === 'slide-hall-of-winners';
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

# 2. Update the main slide subtitle and jackpot slide footer when paused
new_pause_state = """
        function updatePausedState() {
            let paused = localStorage.getItem('cta_paused') === 'true';
            
            // Auto pause for the $2700 win
            const pauseEndDate = new Date('2026-10-13T00:00:00').getTime();
            if (Date.now() < pauseEndDate) {
                paused = true;
            }

            if (paused !== isGameplayPaused) {
                isGameplayPaused = paused;
                // Force transition to a valid slide if the current slide is no longer allowed
                if (!shouldShowSlide(slides[currentSlide])) {
                    nextSlide();
                    resetInterval();
                }
            }

            // Dynamically adjust main subtitle text and jackpot text
            const subtitleEl = document.getElementById('text-main-subtitle');
            const jackpotFooter = document.getElementById('text-jackpot-footer');
            
            if (subtitleEl) {
                if (!originalMainSubtitle) {
                    originalMainSubtitle = subtitleEl.innerHTML;
                }
                if (isGameplayPaused) {
                    subtitleEl.innerHTML = "GAME PLAY IS CURRENTLY PAUSED AND WILL RESET IN A FEW WEEKS<br>BUILDING BACK TO $500!";
                } else {
                    const storedContent = localStorage.getItem('cta_slide_content');
                    const content = storedContent ? JSON.parse(storedContent) : null;
                    subtitleEl.innerHTML = (content && content['main-subtitle']) ? content['main-subtitle'] : originalMainSubtitle;
                }
            }
            
            if (jackpotFooter) {
                if (isGameplayPaused) {
                    jackpotFooter.innerHTML = "GAME PLAY IS CURRENTLY PAUSED AND WILL RESET IN A FEW WEEKS<br>RESUMES WHEN JACKPOT HITS $500!";
                    jackpotFooter.style.color = "#f59e0b"; // Highlight in amber when paused
                } else {
                    jackpotFooter.innerHTML = "Jackpot increases by $100 after every draw!";
                    jackpotFooter.style.color = "#94a3b8";
                }
            }
        }
"""
content = re.sub(
    r'function updatePausedState\(\) \{.*?\}\s*updatePausedState\(\);',
    new_pause_state.strip() + "\n        updatePausedState();",
    content,
    flags=re.DOTALL
)

# 3. Update the Winner Slide text to explicitly use the exact message as well
new_winner = """
        <!-- Slide: Winner Announcement (Paused) -->
        <div class="slide slide-fullscreen" id="slide-winner">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center;">
                <h2 class="font-headline glow-gold" style="font-size: 140px; color: #d4af37; text-transform: uppercase; margin: 0; line-height: 1;">CONGRATULATIONS</h2>
                <div style="font-size: 40px; font-weight: 800; color: #ffffff; letter-spacing: 4px; text-transform: uppercase; margin-top: 10px;">TO OUR RECENT WINNER</div>
                
                <div class="winner-box" style="margin-top: 60px; padding: 60px 80px; max-width: 1400px; background: rgba(20, 20, 20, 0.7); backdrop-filter: blur(15px); border: 2px solid #d4af37; border-top: 6px solid #d4af37; border-bottom: 6px solid #d4af37; border-radius: 30px; box-shadow: 0 20px 50px rgba(212, 175, 55, 0.15), 0 15px 40px rgba(0, 0, 0, 0.8);">
                    <p style="font-size: 56px; font-weight: 600; color: #cbd5e1; margin: 0; line-height: 1.5;">
                        They successfully found the Ace of Spades and took home the<br>
                        <strong style="font-size: 96px; color: #f59e0b; display: block; margin: 30px 0;">$2700 JACKPOT!</strong>
                    </p>
                    <p style="font-size: 32px; font-weight: 700; color: #94a3b8; margin-top: 40px; text-transform: uppercase; letter-spacing: 2px;">
                        Game play is currently paused and will reset in a few weeks.<br>
                        Resuming October 13th when the Jackpot reaches $500!
                    </p>
                </div>
            </div>
        </div>
"""
content = re.sub(
    r'<!-- Slide: Winner Announcement \(Paused\) -->.*?<!-- Slide: Hall of Winners -->',
    new_winner.strip() + "\n\n        <!-- Slide: Hall of Winners -->",
    content,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
