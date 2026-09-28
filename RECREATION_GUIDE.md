# Chase the Ace - Digital Signage Architecture

## 1. Overview
A vanilla HTML/CSS/JS digital signage application designed for 1080p TV displays. It cycles through informational slides, fetches live data from a Google Sheet, and features dynamic CSS animations and JS-driven confetti.

## 2. Tech Stack
*   **Frontend**: Pure HTML5, CSS3, Vanilla JavaScript.
*   **Data Source**: Published Google Sheets CSV (`fetch` API).
*   **Hosting**: GitHub Pages (`main` branch deployment).

## 3. Core Features
*   **Automated Slide Rotation**: JavaScript toggles a `.active` CSS class on `.slide` elements based on a customizable timer array.
*   **Live Data Sync**: Fetches a public Google Sheets CSV URL, parses it, and dynamically updates the DOM elements (Jackpot Amount, Winners, Cards Remaining) every 5-10 minutes.
*   **Countdown Logic**: Calculates the exact time remaining until Thursday at 6:00 PM (or specific draw times) and dynamically builds the countdown UI.
*   **Keyboard Controls**: 
    *   `ArrowLeft` / `ArrowRight`: Navigate slides.
    *   `Space`: Toggle rotation pause.
    *   `0`: Freeze rotation (locks active slide).
    *   `1`-`9`: Set custom slide display duration (10s to 90s).
    *   `A` / `R`: Open Admin or Remote interfaces.

## 4. Typography & Design
*   **Fonts**: 
    *   `Playfair Display` (Original main titles)
    *   `Bebas Neue` (Numbers, timers, digital readouts)
    *   `Inter` / `Outfit` (Subtitles, body text, rules)
*   **Animations**: CSS `@keyframes` for entrance transitions (`slideInUp`), pulsing glows, and a JavaScript canvas/DOM element loop for background confetti.

## 5. File Structure
*   `index.html`: Main TV display application.
*   `preview.html`: CSS Grid layout showing all slides simultaneously for monitoring.
*   `style.css`: Unified global styling, responsive scaling logic, and CSS keyframe animations.
*   `data.csv`: Local fallback data file used when the Google Sheets fetch fails.

## 6. Data Schema (Google Sheets CSV)
The application expects specific columns to populate the DOM:
*   Index 0: Jackpot Amount
*   Index 1: Draw Date
*   Index 2: Winner Name
*   Index 4: Winning Chance / Cards Flipped
