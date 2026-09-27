import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

new_logic = """
            if (isPaused) {
                remaining = 0;
            }

            // Hide the Tuesday, Saturday, and How to Win slides from the preview grid when paused
            if (isPaused) {
                const hideSlides = ['slide-tuesday', 'slide-saturday', 'slide-win'];
                hideSlides.forEach(id => {
                    const el = document.getElementById(id);
                    if (el && el.parentElement && el.parentElement.parentElement) {
                        el.parentElement.parentElement.style.display = 'none';
                    }
                });
            } else {
                const showSlides = ['slide-tuesday', 'slide-saturday', 'slide-win'];
                showSlides.forEach(id => {
                    const el = document.getElementById(id);
                    if (el && el.parentElement && el.parentElement.parentElement) {
                        el.parentElement.parentElement.style.display = 'block';
                    }
                });
            }
"""

preview = re.sub(
    r"if \(isPaused\) \{\s*remaining = 0;\s*\}",
    new_logic.strip(),
    preview,
    flags=re.DOTALL
)

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview)

