import re

CSS_ADDITIONS = """
/* --- UNIFIED SIGNAGE DESIGN SYSTEM --- */
.slide-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 3px solid rgba(212, 175, 55, 0.25);
    padding-bottom: 30px;
    margin-bottom: 40px;
    width: 100%;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 30px;
}

.header-icon-box {
    width: 120px;
    height: 120px;
    border-radius: 28px;
    background: rgba(212, 175, 55, 0.15);
    border: 3px solid rgba(212, 175, 55, 0.45);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
    flex-shrink: 0;
}

.header-icon-box .material-symbols-outlined {
    font-size: 80px;
    color: #d4af37;
}

.text-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 110px;
    line-height: 0.9;
    letter-spacing: 3px;
    color: #ffffff;
    text-transform: uppercase;
    margin: 0;
    white-space: nowrap;
    text-shadow: 0 5px 15px rgba(0, 0, 0, 0.8);
}

.text-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 38px;
    font-weight: 800;
    color: #d4af37;
    letter-spacing: 5px;
    text-transform: uppercase;
    margin-top: 12px;
    white-space: nowrap;
}

.text-subtitle-amber {
    color: #f59e0b;
}

.signage-row-unified {
    display: flex;
    align-items: center;
    gap: 30px;
    background: rgba(6, 8, 13, 0.6);
    border: 2px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 24px 36px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    transition: transform 0.3s ease, border-color 0.3s ease;
    animation: slideUpFade 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) both;
}

.row-icon {
    width: 90px;
    height: 90px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.row-icon-gold {
    background: rgba(212, 175, 55, 0.15);
    border: 2px solid rgba(212, 175, 55, 0.3);
}

.row-icon-amber {
    background: rgba(245, 158, 11, 0.15);
    border: 2px solid rgba(245, 158, 11, 0.3);
}

.row-text-label {
    font-family: 'Inter', sans-serif;
    font-size: 52px;
    font-weight: 600;
    color: #cbd5e1;
    white-space: nowrap;
}

.row-text-value {
    font-family: 'Playfair Display', serif;
    font-size: 64px;
    font-weight: 800;
    color: #ffffff;
    white-space: nowrap;
    letter-spacing: 2px;
}

/* Animations */
@keyframes slideUpFade {
    0% { opacity: 0; transform: translateY(40px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes pulseGlow {
    0% { filter: drop-shadow(0 0 20px rgba(212, 175, 55, 0.4)); transform: scale(1); }
    50% { filter: drop-shadow(0 0 50px rgba(212, 175, 55, 0.8)); transform: scale(1.02); }
    100% { filter: drop-shadow(0 0 20px rgba(212, 175, 55, 0.4)); transform: scale(1); }
}

@keyframes blink {
    0%, 49% { opacity: 1; }
    50%, 100% { opacity: 0; }
}

.blink-colon {
    animation: blink 1s infinite;
}

.slide-fullscreen .signage-card-gold, .slide-fullscreen .signage-card-amber {
    animation: slideUpFade 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) both;
    display: flex;
    flex-direction: column;
    justify-content: center; /* Center contents vertically by default */
}

/* Specific layout adjustments */
.content-flex-col {
    display: flex;
    flex-direction: column;
    gap: 30px;
    width: 100%;
}

.content-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    width: 100%;
}

.step-card {
    background: rgba(6, 8, 13, 0.88);
    border: 2px solid rgba(255, 255, 255, 0.15);
    border-radius: 28px;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 480px;
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7);
    animation: slideUpFade 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) both;
}

.step-number {
    font-family: 'Playfair Display', serif;
    font-size: 130px;
    color: #d4af37;
    line-height: 0.85;
    font-weight: 900;
}

.step-title {
    font-family: 'Playfair Display', serif;
    font-size: 64px;
    letter-spacing: 2px;
    color: #ffffff;
    text-transform: uppercase;
    line-height: 1;
    margin-bottom: 20px;
}

.step-desc {
    font-family: 'Inter', sans-serif;
    font-size: 38px;
    color: #94a3b8;
    font-weight: 600;
    line-height: 1.4;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
}
"""

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '/* --- UNIFIED SIGNAGE DESIGN SYSTEM --- */' not in css:
    with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + CSS_ADDITIONS)

# Now, rebuild the slides in index.html and preview.html
HTML_REPLACEMENT = """
        <!-- Slide 1: Main Title -->
        <div class="slide slide-fullscreen active" id="slide-main">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center; gap: 50px;">
                <img src="logo.png" alt="Venue Logo" class="venue-logo" style="width: 280px; height: auto; animation: pulseGlow 4s infinite;" onerror="this.style.display='none'">
                <h1 id="text-main-title" class="font-headline glow-gold" style="font-size: 180px; line-height: 0.9; color: #ffffff; margin: 0; letter-spacing: 2px; text-transform: uppercase; white-space: nowrap;">
                    CHASE THE<br><span class="title-spade" style="color: #d4af37;">♠</span>ACE<span class="title-spade" style="color: #d4af37;">♠</span>
                </h1>
                <img src="ace-of-spades.png" alt="Ace of Spades" class="ace-logo" style="height: 320px; filter: drop-shadow(0 0 40px rgba(245, 158, 11, 0.4));" onerror="this.style.display='none'">
                <h2 id="text-main-subtitle" style="font-family: 'Playfair Display', serif; font-size: 56px; font-weight: 900; color: #d4af37; letter-spacing: 4px; text-transform: uppercase; margin-top: 20px; white-space: nowrap; line-height: 1.2;">
                    GAME PLAY IS CURRENTLY PAUSED AND WILL RESET IN A FEW WEEKS<br>BUILDING BACK TO $500!
                </h2>
            </div>
        </div>

        <!-- Slide 2: Current Jackpot -->
        <div class="slide slide-fullscreen" id="slide-jackpot">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center;">
                <div class="header-icon-box" style="margin-bottom: 40px; animation: pulseGlow 3s infinite;">
                    <span class="material-symbols-outlined">attach_money</span>
                </div>
                <h2 class="text-title" style="font-size: 100px; margin-bottom: 10px;">CURRENT JACKPOT</h2>
                <div class="jackpot-amount glow-gold" id="display-jackpot" style="font-family: 'Playfair Display', serif; font-size: 300px; font-weight: 900; color: #d4af37; line-height: 1; margin: 20px 0; white-space: nowrap;">
                    $0.00
                </div>
                <div class="text-subtitle" id="text-jackpot-footer" style="font-size: 46px; color: #94a3b8; margin-top: 50px; white-space: nowrap; line-height: 1.3;">
                    Jackpot increases by $100 after every draw!
                </div>
            </div>
        </div>

        <!-- Slide: Countdown -->
        <div class="slide slide-fullscreen" id="countdown-slide">
            <div class="signage-card-amber box-glow-amber" style="align-items: center; justify-content: center; text-align: center;">
                <h2 class="text-title" style="font-size: 110px; color: #ffffff; margin-bottom: 20px;">DRAW STARTS IN</h2>
                <div class="countdown-timer glow-amber" id="timer-display" style="display: flex; gap: 30px; font-family: 'Playfair Display', serif; font-size: 220px; font-weight: 900; color: #f59e0b; margin: 50px 0; align-items: baseline; justify-content: center; white-space: nowrap;">
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-d">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">DAYS</small></div>
                    <div style="color: #f59e0b; opacity: 0.6; transform: translateY(-30px);" class="blink-colon">:</div>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-h">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">HRS</small></div>
                    <div style="color: #f59e0b; opacity: 0.6; transform: translateY(-30px);" class="blink-colon">:</div>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-m">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">MIN</small></div>
                    <div style="color: #f59e0b; opacity: 0.6; transform: translateY(-30px);" class="blink-colon">:</div>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="cd-s">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">SEC</small></div>
                </div>
                <div class="text-subtitle text-subtitle-amber" style="font-size: 46px; margin-top: 40px;" id="text-countdown-footer">
                    GET YOUR TICKETS READY!
                </div>
            </div>
        </div>

        <!-- Slide: Next Draw Timer -->
        <div class="slide slide-fullscreen" id="next-draw-slide">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center;">
                <h2 class="text-title" style="font-size: 110px; margin-bottom: 20px;" id="next-draw-label">NEXT DRAW IN</h2>
                <div class="countdown-timer glow-gold" id="next-timer-display" style="display: flex; gap: 30px; font-family: 'Playfair Display', serif; font-size: 220px; font-weight: 900; color: #d4af37; margin: 50px 0; align-items: baseline; justify-content: center; white-space: nowrap;">
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-d">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">DAYS</small></div>
                    <div style="color: #d4af37; opacity: 0.6; transform: translateY(-30px);" class="blink-colon">:</div>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-h">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">HRS</small></div>
                    <div style="color: #d4af37; opacity: 0.6; transform: translateY(-30px);" class="blink-colon">:</div>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-m">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">MIN</small></div>
                    <div style="color: #d4af37; opacity: 0.6; transform: translateY(-30px);" class="blink-colon">:</div>
                    <div style="display: flex; flex-direction: column; align-items: center; line-height: 1;"><span id="nd-s">00</span><small style="font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800; letter-spacing: 4px; color: #94a3b8; margin-top: 15px;">SEC</small></div>
                </div>
                <div class="text-subtitle" style="font-size: 46px; margin-top: 40px;">
                    BE AT THE VENUE TO WIN!
                </div>
            </div>
        </div>

        <!-- Slide: Tuesday Rules -->
        <div class="slide slide-fullscreen" id="slide-tuesday">
            <div class="signage-card-gold box-glow-gold" style="justify-content: flex-start;">
                <div class="slide-header">
                    <div class="header-left">
                        <div class="header-icon-box">
                            <span class="material-symbols-outlined">calendar_month</span>
                        </div>
                        <div>
                            <h2 class="text-title">TUESDAY DRAW</h2>
                            <div class="text-subtitle">COASTERS TAVERN WEEKLY EVENT</div>
                        </div>
                    </div>
                    <div class="time-badge-gold glow-gold" style="font-family: 'Playfair Display', serif; font-size: 72px; font-weight: 900; background: rgba(212, 175, 55, 0.18); border: 3px solid #d4af37; color: #d4af37; padding: 20px 45px; border-radius: 9999px; box-shadow: 0 0 30px rgba(212, 175, 55, 0.3); white-space: nowrap;" id="text-tue-time">
                        5<span class="blink-colon">:</span>30 PM
                    </div>
                </div>
                <div class="content-flex-col">
                    <div class="signage-row-unified" style="animation-delay: 0.1s;">
                        <div class="row-icon row-icon-amber"><span class="material-symbols-outlined" style="font-size: 64px; color: #f59e0b;">schedule</span></div>
                        <span class="row-text-label">Beverage Window:</span>
                        <span class="row-text-value">4:30 PM <span style="opacity:0.5">-</span> 5:30 PM</span>
                    </div>
                    <div class="signage-row-unified" style="animation-delay: 0.2s;">
                        <div class="row-icon row-icon-gold"><span class="material-symbols-outlined" style="font-size: 64px; color: #d4af37;">confirmation_number</span></div>
                        <span class="row-text-value" style="font-family: 'Inter', sans-serif;">1 Ticket with every beverage purchased</span>
                    </div>
                    <div class="signage-row-unified" style="animation-delay: 0.3s;">
                        <div class="row-icon row-icon-amber"><span class="material-symbols-outlined" style="font-size: 64px; color: #f59e0b;">alarm_on</span></div>
                        <span class="row-text-label">Draw Time:</span>
                        <span class="row-text-value" style="color: #f59e0b;">5:30 PM Sharp!</span>
                    </div>
                    <div class="signage-row-unified" style="animation-delay: 0.4s; background: rgba(212, 175, 55, 0.1); border-color: rgba(212, 175, 55, 0.4);">
                        <div class="row-icon row-icon-gold"><span class="material-symbols-outlined" style="font-size: 64px; color: #d4af37;">local_bar</span></div>
                        <span class="row-text-value" style="color: #d4af37;">Bonus: Includes Members Pint Draw!</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide: Saturday Rules -->
        <div class="slide slide-fullscreen" id="slide-saturday">
            <div class="signage-card-amber box-glow-amber" style="justify-content: flex-start;">
                <div class="slide-header" style="border-bottom-color: rgba(245, 158, 11, 0.25);">
                    <div class="header-left">
                        <div class="header-icon-box" style="background: rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.45); box-shadow: 0 0 30px rgba(245, 158, 11, 0.2);">
                            <span class="material-symbols-outlined" style="color: #f59e0b;">event_available</span>
                        </div>
                        <div>
                            <h2 class="text-title">SATURDAY DRAW</h2>
                            <div class="text-subtitle text-subtitle-amber">COASTERS TAVERN WEEKLY EVENT</div>
                        </div>
                    </div>
                    <div class="time-badge-amber glow-amber" style="font-family: 'Playfair Display', serif; font-size: 72px; font-weight: 900; background: rgba(245, 158, 11, 0.18); border: 3px solid #f59e0b; color: #f59e0b; padding: 20px 45px; border-radius: 9999px; box-shadow: 0 0 30px rgba(245, 158, 11, 0.3); white-space: nowrap;" id="text-sat-time">
                        4<span class="blink-colon">:</span>30 PM
                    </div>
                </div>
                <div class="content-flex-col">
                    <div class="signage-row-unified" style="animation-delay: 0.1s;">
                        <div class="row-icon row-icon-amber"><span class="material-symbols-outlined" style="font-size: 64px; color: #f59e0b;">schedule</span></div>
                        <span class="row-text-label">Beverage Window:</span>
                        <span class="row-text-value">3:30 PM <span style="opacity:0.5">-</span> 4:30 PM</span>
                    </div>
                    <div class="signage-row-unified" style="animation-delay: 0.2s;">
                        <div class="row-icon row-icon-gold"><span class="material-symbols-outlined" style="font-size: 64px; color: #d4af37;">confirmation_number</span></div>
                        <span class="row-text-value" style="font-family: 'Inter', sans-serif;">1 Ticket with every beverage purchased</span>
                    </div>
                    <div class="signage-row-unified" style="animation-delay: 0.3s;">
                        <div class="row-icon row-icon-amber"><span class="material-symbols-outlined" style="font-size: 64px; color: #f59e0b;">alarm_on</span></div>
                        <span class="row-text-label">Draw Time:</span>
                        <span class="row-text-value" style="color: #f59e0b;">4:30 PM Sharp!</span>
                    </div>
                    <div class="signage-row-unified" style="animation-delay: 0.4s; background: rgba(212, 175, 55, 0.1); border-color: rgba(212, 175, 55, 0.4);">
                        <div class="row-icon row-icon-gold"><span class="material-symbols-outlined" style="font-size: 64px; color: #d4af37;">local_fire_department</span></div>
                        <span class="row-text-value" style="color: #d4af37;">Bonus: Weekly Meat Raffles!</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide: How To Win -->
        <div class="slide slide-fullscreen" id="slide-win">
            <div class="signage-card-gold box-glow-gold" style="justify-content: flex-start;">
                <div class="slide-header">
                    <div class="header-left">
                        <div class="header-icon-box">
                            <span class="material-symbols-outlined">help</span>
                        </div>
                        <div>
                            <h2 class="text-title">HOW TO WIN</h2>
                            <div class="text-subtitle">YOUR PATHWAY TO THE JACKPOT</div>
                        </div>
                    </div>
                    <div style="background: rgba(14, 17, 24, 0.9); border: 3px solid #d4af37; color: #d4af37; font-family: 'Inter', sans-serif; font-size: 38px; font-weight: 800; padding: 20px 45px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 2px; box-shadow: 0 0 30px rgba(212, 175, 55, 0.25); white-space: nowrap;">
                        If your ticket is pulled from barrel:
                    </div>
                </div>
                <div class="content-grid-3">
                    <!-- Step 01 -->
                    <div class="step-card" style="animation-delay: 0.1s;">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 30px;">
                            <span class="step-number glow-gold">01</span>
                            <div class="header-icon-box" style="width: 100px; height: 100px;"><span class="material-symbols-outlined" style="font-size: 64px;">lock_open</span></div>
                        </div>
                        <div>
                            <div class="step-title">PICK A<br>CARD</div>
                            <div class="step-desc">From the card vault<br><strong style="color: #ffffff; font-size: 44px;">(52 cards total)</strong></div>
                        </div>
                    </div>
                    <!-- Step 02 -->
                    <div class="step-card" style="animation-delay: 0.2s;">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 30px;">
                            <span class="step-number glow-gold">02</span>
                            <div class="header-icon-box" style="width: 100px; height: 100px;"><span class="material-symbols-outlined" style="font-size: 64px;">playing_cards</span></div>
                        </div>
                        <div>
                            <div class="step-title">REVEAL<br>CARD</div>
                            <div class="step-desc">Any card other than<br><strong style="color: #ffffff; font-size: 44px;">the Ace of Spades</strong></div>
                        </div>
                    </div>
                    <!-- Step 03 -->
                    <div class="step-card" style="animation-delay: 0.3s; background: rgba(212, 175, 55, 0.1); border-color: rgba(212, 175, 55, 0.5);">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 30px;">
                            <span class="step-number glow-gold">03</span>
                            <div class="header-icon-box" style="width: 100px; height: 100px; background: rgba(245, 158, 11, 0.2); border-color: #f59e0b;"><span class="material-symbols-outlined" style="font-size: 64px; color: #f59e0b;">paid</span></div>
                        </div>
                        <div>
                            <div class="step-title" style="color: #f59e0b;">WIN<br>$100</div>
                            <div class="step-desc" style="color: #cbd5e1; white-space: normal;">Card is destroyed & Jackpot increases by <strong style="color: #f59e0b; font-size: 44px;">$100</strong></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide: Vault Deck -->
        <div class="slide slide-fullscreen" id="slide-vault">
            <div class="signage-card-gold box-glow-gold" style="justify-content: flex-start;">
                <div class="slide-header">
                    <div class="header-left">
                        <div class="header-icon-box">
                            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">lock</span>
                        </div>
                        <div>
                            <h2 class="text-title">THE CARD VAULT</h2>
                            <div class="text-subtitle">LIVE REAL-TIME CARD DECK INVENTORY</div>
                        </div>
                    </div>
                    <div class="glow-gold" style="font-family: 'Playfair Display', serif; background: rgba(212, 175, 55, 0.18); border: 3px solid #d4af37; color: #d4af37; font-size: 64px; font-weight: 900; line-height: 1; padding: 24px 50px; border-radius: 9999px; box-shadow: 0 0 35px rgba(212, 175, 55, 0.45); white-space: nowrap; animation: pulseGlow 3s infinite;">
                        ODDS OF ACE: <span id="vault-odds-display" style="color: #ffffff;">1 IN 36</span>
                    </div>
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; gap: 80px; flex-grow: 1; padding: 20px;">
                    <!-- Left: 3D Playing Cards -->
                    <div style="position: relative; width: 450px; height: 500px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-left: 40px; animation: slideUpFade 1s cubic-bezier(0.2, 0.8, 0.2, 1) both;">
                        <div style="position: absolute; width: 260px; height: 380px; background: rgba(14, 17, 24, 0.9); border-radius: 24px; border: 3px solid rgba(212, 175, 55, 0.35); transform: rotate(-14deg) translateX(-55px); display: flex; flex-direction: column; justify-content: space-between; padding: 24px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.9);">
                            <div style="font-family: 'Playfair Display', serif; font-size: 64px; color: rgba(212, 175, 55, 0.8); font-weight: 900; line-height: 0.9;">52</div>
                            <div style="font-family: 'Inter', sans-serif; font-weight: 800; text-align: center; font-size: 36px; color: #94a3b8; letter-spacing: 3px;">TOTAL</div>
                            <div style="font-family: 'Playfair Display', serif; font-size: 64px; color: rgba(212, 175, 55, 0.8); font-weight: 900; line-height: 0.9; text-align: right; transform: rotate(180deg);">52</div>
                        </div>
                        <div style="position: absolute; width: 260px; height: 380px; background: rgba(14, 17, 24, 0.9); border-radius: 24px; border: 3px solid rgba(245, 158, 11, 0.5); transform: rotate(14deg) translateX(55px); display: flex; flex-direction: column; justify-content: space-between; padding: 24px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.9);">
                            <div id="card-fanned-flipped-top" style="font-family: 'Playfair Display', serif; font-size: 64px; color: #f59e0b; font-weight: 900; line-height: 0.9;">#16</div>
                            <div style="font-family: 'Inter', sans-serif; font-weight: 800; text-align: center; font-size: 36px; color: #f59e0b; letter-spacing: 3px;">MISSED</div>
                            <div id="card-fanned-flipped-bot" style="font-family: 'Playfair Display', serif; font-size: 64px; color: #f59e0b; font-weight: 900; line-height: 0.9; text-align: right; transform: rotate(180deg);">#16</div>
                        </div>
                        <div class="box-glow-gold" style="position: relative; z-index: 20; width: 310px; height: 440px; background: linear-gradient(180deg, #181c28 0%, #080a0f 100%); border: 4px solid #d4af37; border-radius: 28px; display: flex; flex-direction: column; justify-content: space-between; padding: 28px; box-shadow: 0 30px 70px rgba(0, 0, 0, 0.95), 0 0 40px rgba(212, 175, 55, 0.4);">
                            <div style="font-family: 'Playfair Display', serif; font-size: 72px; color: #d4af37; font-weight: 900; line-height: 0.9;">?</div>
                            <div style="display: flex; flex-direction: column; align-items: center;">
                                <div style="font-family: 'Inter', sans-serif; font-size: 80px; font-weight: 900; color: #ffffff; line-height: 1;" id="vault-remaining-num">36</div>
                                <div style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 36px; color: #d4af37; letter-spacing: 4px; margin-top: 10px;">REMAINING</div>
                            </div>
                            <div style="font-family: 'Playfair Display', serif; font-size: 72px; color: #d4af37; font-weight: 900; line-height: 0.9; text-align: right; transform: rotate(180deg);">?</div>
                        </div>
                    </div>
                    <!-- Right: Stats -->
                    <div style="display: flex; flex-direction: column; gap: 40px; width: 100%; max-width: 900px; animation: slideUpFade 1.2s cubic-bezier(0.2, 0.8, 0.2, 1) both;">
                        <div class="signage-row-unified" style="padding: 36px 48px;">
                            <div class="row-icon row-icon-amber" style="width: 110px; height: 110px;"><span class="material-symbols-outlined" style="font-size: 76px; color: #f59e0b;">layers</span></div>
                            <span class="row-text-label" style="font-size: 60px;">Total Deck Size:</span>
                            <span class="row-text-value" style="font-size: 76px; margin-left: auto;">52 CARDS</span>
                        </div>
                        <div class="signage-row-unified" style="padding: 36px 48px;">
                            <div class="row-icon row-icon-gold" style="width: 110px; height: 110px;"><span class="material-symbols-outlined" style="font-size: 76px; color: #d4af37;">block</span></div>
                            <span class="row-text-label" style="font-size: 60px;">Cards Destroyed:</span>
                            <span class="row-text-value" id="vault-flipped-num" style="font-size: 76px; margin-left: auto; color: #d4af37;">16 CARDS</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide: Winner Announcement -->
        <div class="slide slide-fullscreen" id="slide-winner">
            <div class="signage-card-gold box-glow-gold" style="align-items: center; justify-content: center; text-align: center;">
                <h2 class="text-title" style="font-size: 160px; color: #d4af37;">CONGRATULATIONS</h2>
                <div style="display: flex; align-items: baseline; gap: 30px; margin: 40px 0;">
                    <span style="font-family: 'Inter', sans-serif; font-size: 70px; font-weight: 800; color: #ffffff;">Ticket</span>
                    <span id="display-winner-ticket" style="font-family: 'Playfair Display', serif; font-size: 140px; font-weight: 900; color: #f59e0b;">#0</span>
                </div>
                <h3 id="display-winner-name" style="font-family: 'Playfair Display', serif; font-size: 110px; font-weight: 800; color: #ffffff; margin: 0; text-transform: uppercase;">WINNER NAME</h3>
                <p style="font-family: 'Inter', sans-serif; font-size: 46px; font-weight: 700; color: #94a3b8; margin-top: 50px; text-transform: uppercase; letter-spacing: 3px; line-height: 1.4;">
                    Game play is currently paused and will reset in a few weeks.<br>
                    <strong style="color: #ffffff;">Resuming October 13th when the Jackpot reaches $500!</strong>
                </p>
            </div>
        </div>

        <!-- Slide: Hall of Winners -->
        <div class="slide slide-fullscreen" id="slide-hall-of-winners">
            <div class="signage-card-gold box-glow-gold" style="justify-content: flex-start;">
                <div class="slide-header">
                    <div class="header-left">
                        <div class="header-icon-box">
                            <span class="material-symbols-outlined">emoji_events</span>
                        </div>
                        <div>
                            <h2 class="text-title">HALL OF WINNERS</h2>
                            <div class="text-subtitle">RECENT CHASE THE ACE CHAMPIONS</div>
                        </div>
                    </div>
                </div>
                <div class="content-flex-col" id="winners-list" style="margin-top: 20px;">
                    <!-- Dynamically populated, fallback hardcoded for layout -->
                    <div class="signage-row-unified" style="padding: 28px 48px; background: rgba(212, 175, 55, 0.15); border-color: rgba(212, 175, 55, 0.4);">
                        <div class="row-icon row-icon-gold" style="width: 100px; height: 100px; background: linear-gradient(135deg, #d4af37, #f59e0b); border: none;">
                            <span style="font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 900; color: #11141d;">1</span>
                        </div>
                        <div style="display: flex; flex-direction: column;">
                            <span style="font-family: 'Playfair Display', serif; font-size: 58px; font-weight: 900; color: #ffffff; letter-spacing: 2px;">Lucky Winner</span>
                            <span style="font-family: 'Inter', sans-serif; font-size: 34px; font-weight: 700; color: #d4af37; letter-spacing: 3px; text-transform: uppercase; margin-top: 6px;">September 26, 2026</span>
                        </div>
                        <span style="font-family: 'Playfair Display', serif; font-size: 80px; font-weight: 900; color: #f59e0b; margin-left: auto;">$2,700</span>
                    </div>
                    <div class="signage-row-unified" style="padding: 28px 48px; opacity: 0.6; border-style: dashed;">
                        <div class="row-icon" style="width: 100px; height: 100px; background: rgba(255, 255, 255, 0.1); border: 2px solid rgba(255, 255, 255, 0.2);">
                            <span style="font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 900; color: #94a3b8;">2</span>
                        </div>
                        <span style="font-family: 'Playfair Display', serif; font-size: 52px; font-weight: 700; color: #94a3b8; font-style: italic;">Awaiting Next Winner...</span>
                    </div>
                </div>
            </div>
        </div>
"""

# Replace the slides in both files
for filename in ['/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', '/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the bounds to replace (from slide-main to slide-hall-of-winners closing div)
    # Be careful, we can use regex dotall between <!-- Slide 1: Main Title --> and the end of the presentation container.
    pattern = r'<!-- Slide 1: Main Title -->.*<!-- Slide: Hall of Winners -->.*?</div>\s*</div>\s*</div>'
    match = re.search(pattern, html, flags=re.DOTALL)
    
    if match:
        html = html[:match.start()] + HTML_REPLACEMENT.strip() + html[match.end():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
    else:
        # Fallback to a safer approach if the strict pattern doesn't match
        # Let's just find the presentation-container inside and replace everything between it and the closing tag
        print(f"Regex failed for {filename}. You might need a different pattern.")
