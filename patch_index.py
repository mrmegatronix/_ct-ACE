import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update fetchCsvData & parseSignageCsv
new_js_logic = """
        // --- Jackpot & Live CSV Sync Logic ---
        const googleSheetUrl = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQDwqNaCeNn7Q6WSgc5gN8aOS08Ltkxu2v9QBSVuaKrJFX61PZ1Nuninkqh_F62wQ5t47usf2e19dxx/pub?output=csv";
        const localCsvUrl = "./data.csv";

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

            // Find max/current cards flipped by date
            const now = new Date();
            const nzTimeStr = now.toLocaleString("en-US", { timeZone: "Pacific/Auckland" });
            const nzDate = new Date(nzTimeStr);
            
            let maxPastRow = null;
            let maxPastDate = new Date(0);

            for (let i = 2; i < lines.length; i++) {
                const row = lines[i];
                if (row.length < 4) continue;
                
                const dateStr = row[1]; // DD/MM/YYYY
                if (!dateStr || !dateStr.includes('/')) continue;
                
                const parts = dateStr.split('/');
                if (parts.length === 3) {
                    const rowDate = new Date(`${parts[2]}-${parts[1]}-${parts[0]}T23:59:59`);
                    if (rowDate <= nzDate) {
                        if (rowDate > maxPastDate) {
                            maxPastDate = rowDate;
                            maxPastRow = row;
                        }
                    }
                }
            }

            if (maxPastRow) {
                const rawFlipped = maxPastRow[3] ? maxPastRow[3].replace(/[^0-9]/g, '') : '';
                flipped = rawFlipped !== '' ? parseInt(rawFlipped, 10) : 0;
            }

            flipped = Math.max(0, Math.min(52, flipped));
            remaining = 52 - flipped;

            return { jackpot, remaining, flipped, labelA2, labelB2 };
        }
"""
content = re.sub(
    r'// --- Jackpot & Live CSV Sync Logic ---.*?function parseSignageCsv.*?return \{ jackpot, remaining, flipped, labelA2, labelB2 \};\s*\}', 
    new_js_logic, 
    content, 
    flags=re.DOTALL
)

# 2. Add Auto Pause logic
new_pause_logic = """
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

            // Dynamically adjust main subtitle text
            const subtitleEl = document.getElementById('text-main-subtitle');
            if (subtitleEl) {
                if (!originalMainSubtitle) {
                    originalMainSubtitle = subtitleEl.innerHTML;
                }
                if (isGameplayPaused) {
                    subtitleEl.innerHTML = "GAMEPLAY TEMPORARILY ON HOLD<br>RESUMES OCT 13TH";
                } else {
                    const storedContent = localStorage.getItem('cta_slide_content');
                    const content = storedContent ? JSON.parse(storedContent) : null;
                    subtitleEl.innerHTML = (content && content['main-subtitle']) ? content['main-subtitle'] : originalMainSubtitle;
                }
            }
        }
"""
content = re.sub(
    r'function updatePausedState\(\) \{.*?\}\s*updatePausedState\(\);',
    new_pause_logic + "\n        updatePausedState();",
    content,
    flags=re.DOTALL
)

# 3. Modify shouldShowSlide to include Hall of Winners and not just main/winner during pause
new_shouldShow = """
        function shouldShowSlide(slide) {
            const now = new Date();
            const nzTimeStr = now.toLocaleString("en-US", { timeZone: "Pacific/Auckland" });
            const nzDate = new Date(nzTimeStr);

            const slideId = slide.id;

            if (isGameplayPaused) {
                // When gameplay is paused
                return slideId === 'slide-main' || slideId === 'slide-winner' || slideId === 'slide-hall-of-winners';
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
    new_shouldShow,
    content,
    flags=re.DOTALL
)

# 4. Replace Slide 1, 2, countdown, next-draw, and winner
slides_html = """
        <!-- Slide 1: Main Title & Logo -->
        <div class="slide slide-fullscreen active" id="slide-main">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center; gap: 40px;">
                <img src="logo.png" alt="Venue Logo" class="venue-logo" style="width: 250px; height: auto; filter: drop-shadow(0 0 20px rgba(212, 175, 55, 0.4));" onerror="this.style.display='none'">
                <h1 id="text-main-title" class="font-headline glow-gold" style="font-size: 160px; line-height: 0.9; color: #ffffff; margin: 0; letter-spacing: 2px; text-transform: uppercase;">
                    CHASE THE<br><span class="title-spade" style="color: #d4af37;">♠</span>ACE<span class="title-spade" style="color: #d4af37;">♠</span>
                </h1>
                <img src="ace-of-spades.png" alt="Ace of Spades" class="ace-logo" style="height: 280px; filter: drop-shadow(0 0 30px rgba(245, 158, 11, 0.3));" onerror="this.style.display='none'">
                <h2 id="text-main-subtitle" style="font-size: 40px; font-weight: 800; color: #d4af37; letter-spacing: 4px; text-transform: uppercase; margin-top: 20px; white-space: pre-line;">JOIN US FOR OUR TWO WEEKLY DRAWS:&#10;TUESDAYS &amp; SATURDAYS</h2>
            </div>
        </div>

        <!-- Slide 2: Current Jackpot -->
        <div class="slide slide-fullscreen" id="slide-jackpot">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center;">
                <div style="width: 140px; height: 140px; border-radius: 30px; background: rgba(212, 175, 55, 0.15); border: 3px solid rgba(212, 175, 55, 0.45); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 35px rgba(212, 175, 55, 0.2); margin-bottom: 40px;">
                    <span class="material-symbols-outlined" style="font-size: 80px; color: #d4af37;">attach_money</span>
                </div>
                <h2 class="font-headline" style="font-size: 90px; color: #ffffff; text-transform: uppercase; letter-spacing: 3px; margin: 0;">CURRENT JACKPOT</h2>
                <div class="jackpot-amount glow-gold" id="display-jackpot" style="font-family: 'Playfair Display', serif; font-size: 260px; font-weight: 900; color: #d4af37; line-height: 1; margin: 20px 0;">
                    $0.00
                </div>
                <div class="countdown-label" id="text-jackpot-footer" style="font-size: 42px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 2px; margin-top: 40px;">
                    Jackpot increases by $100 after every draw!
                </div>
            </div>
        </div>

        <!-- Slide: Countdown -->
        <div class="slide slide-fullscreen" id="countdown-slide">
            <div class="signage-card-amber box-glow-amber" style="align-items: center; justify-content: center; text-align: center;">
                <h2 class="font-headline" style="font-size: 90px; color: #ffffff; text-transform: uppercase; letter-spacing: 3px; margin: 0;">DRAW STARTS IN</h2>
                <div class="countdown-timer glow-amber" id="timer-display" style="display: flex; gap: 20px; font-family: 'Playfair Display', serif; font-size: 200px; font-weight: 900; color: #f59e0b; margin: 40px 0; align-items: baseline; justify-content: center;">
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-d">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">DAYS</small></div>
                    <span class="blink-colon">:</span>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-h">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">HOURS</small></div>
                    <span class="blink-colon">:</span>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-m">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">MINUTES</small></div>
                    <span class="blink-colon">:</span>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-s">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">SECONDS</small></div>
                </div>
                <div class="countdown-label" style="background: rgba(245, 158, 11, 0.18); border: 3px solid #f59e0b; color: #f59e0b; font-size: 52px; font-weight: 900; padding: 20px 50px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 2px; margin-top: 40px;">
                    GET YOUR TICKETS NOW!
                </div>
            </div>
        </div>

        <!-- Slide: Next Draw General Countdown -->
        <div class="slide slide-fullscreen" id="next-draw-slide">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center;">
                <h2 class="font-headline" style="font-size: 90px; color: #ffffff; text-transform: uppercase; letter-spacing: 3px; margin: 0;">NEXT DRAW</h2>
                <div class="countdown-timer glow-gold" id="next-draw-timer" style="display: flex; gap: 20px; font-family: 'Playfair Display', serif; font-size: 200px; font-weight: 900; color: #d4af37; margin: 40px 0; align-items: baseline; justify-content: center;">
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-d">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">DAYS</small></div>
                    <span class="blink-colon">:</span>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-h">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">HOURS</small></div>
                    <span class="blink-colon">:</span>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-m">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">MINUTES</small></div>
                    <span class="blink-colon">:</span>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-s">00</span><small style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 700; letter-spacing: 3px; color: #94a3b8; margin-top: 10px;">SECONDS</small></div>
                </div>
                <h2 id="next-draw-label" style="font-size: 42px; font-weight: 700; color: #cbd5e1; text-transform: uppercase; letter-spacing: 2px; margin-top: 40px;">
                    LOADING...
                </h2>
            </div>
        </div>
"""

content = re.sub(
    r'<!-- Slide 1: Main Title & Logo -->.*?<!-- Slide 3: Tuesday Draw -->',
    slides_html + "\n        <!-- Slide 3: Tuesday Draw -->",
    content,
    flags=re.DOTALL
)

winner_and_hall_html = """
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
                        Chase the Ace gameplay is now paused.<br>
                        We will resume and reset the vault on Tuesday, October 13th!
                    </p>
                </div>
            </div>
        </div>

        <!-- Slide: Hall of Winners -->
        <div class="slide slide-fullscreen" id="slide-hall-of-winners">
            <div class="signage-card-gold box-glow-gold">
                <div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent, #d4af37, #f59e0b, #d4af37, transparent);"></div>
                <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid rgba(212, 175, 55, 0.25); padding-bottom: 26px;">
                    <div style="display: flex; align-items: center; gap: 26px;">
                        <div style="width: 104px; height: 104px; border-radius: 24px; background: rgba(212, 175, 55, 0.15); border: 2.5px solid rgba(212, 175, 55, 0.45); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 25px rgba(212, 175, 55, 0.2);">
                            <span class="material-symbols-outlined" style="font-size: 68px; color: #d4af37;">workspace_premium</span>
                        </div>
                        <div>
                            <h2 class="font-headline" style="font-size: 104px; line-height: 0.95; letter-spacing: 2px; color: #ffffff; text-transform: uppercase; margin: 0;">HALL OF WINNERS</h2>
                            <div style="font-size: 28px; font-weight: 800; color: #d4af37; letter-spacing: 4px; text-transform: uppercase; margin-top: 6px;">CELEBRATING OUR JACKPOT CHAMPIONS</div>
                        </div>
                    </div>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 24px; margin: auto 0; padding: 30px 0;">
                    <!-- Winner 1 -->
                    <div class="signage-row" style="justify-content: space-between; padding: 20px 40px;">
                        <div style="display: flex; align-items: center; gap: 32px;">
                            <div style="width: 72px; height: 72px; border-radius: 50%; background: linear-gradient(135deg, #d4af37, #f59e0b); display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900; color: #11141d; box-shadow: 0 0 20px rgba(212, 175, 55, 0.5);">1</div>
                            <div>
                                <div style="font-size: 42px; font-weight: 800; color: #ffffff; letter-spacing: 1px;">Lucky Winner</div>
                                <div style="font-size: 24px; font-weight: 700; color: #94a3b8; letter-spacing: 2px; text-transform: uppercase; margin-top: 4px;">September 26, 2026</div>
                            </div>
                        </div>
                        <div class="font-headline glow-gold" style="font-size: 64px; font-weight: 900; color: #d4af37;">
                            $2700
                        </div>
                    </div>
                    <!-- Empty placeholders for future winners -->
                    <div class="signage-row" style="justify-content: space-between; padding: 20px 40px; opacity: 0.5; border-style: dashed; border-width: 2px; border-color: rgba(255,255,255,0.2);">
                        <div style="display: flex; align-items: center; gap: 32px;">
                            <div style="width: 72px; height: 72px; border-radius: 50%; background: rgba(255, 255, 255, 0.1); border: 2px solid rgba(255, 255, 255, 0.2); display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900; color: #94a3b8;">2</div>
                            <div style="font-size: 32px; font-weight: 700; color: #94a3b8; font-style: italic;">Awaiting Next Winner...</div>
                        </div>
                    </div>
                </div>

                <div style="padding-top: 22px; border-top: 2px solid rgba(212, 175, 55, 0.2); display: flex; justify-content: center; align-items: center; font-size: 26px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; color: #94a3b8;">
                    WILL YOU BE NEXT? GET YOUR TICKETS AT THE BAR!
                </div>
            </div>
        </div>
"""

content = re.sub(
    r'<!-- Slide 6: Winner Announcement \(Paused\) -->.*?</div>\s*</div>\s*<!-- Progress Bar -->',
    winner_and_hall_html + "\n    </div>\n\n    <!-- Progress Bar -->",
    content,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

