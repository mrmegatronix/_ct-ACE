import re

with open('rewrite_ui.py', 'r') as f:
    code = f.read()

# Extract the HTML_REPLACEMENT variable from rewrite_ui.py
import ast
# We'll just read it by slicing
html_repl = code.split('HTML_REPLACEMENT = """')[1].split('"""\n\n# Replace')[0]

for filename in ['/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', '/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/preview.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the start of the slides
    start_idx = html.find('<div class="slide slide-fullscreen active" id="slide-main">')
    if start_idx == -1:
        start_idx = html.find('<div class="slide slide-fullscreen" id="slide-main">')
        
    if start_idx == -1:
        print(f"Could not find slide-main in {filename}")
        continue
        
    # Find the end of the presentation container
    # The last slide is slide-hall-of-winners
    end_pattern = '<div class="slide slide-fullscreen" id="slide-hall-of-winners">'
    end_idx = html.find(end_pattern)
    if end_idx != -1:
        # Find the closing divs for slide-hall-of-winners
        # It has 3 closing divs: one for the row, one for the signage-card, one for the slide
        # Let's just find the end of the presentation container which comes after it.
        # Wait, preview.html has it structured slightly differently.
        # Let's just find the next <!-- Controls --> or <script> tag.
        script_idx = html.find('<!-- Controls -->', end_idx)
        if script_idx == -1:
            script_idx = html.find('<script>', end_idx)
            
        if script_idx != -1:
            # We want to keep everything before start_idx, insert html_repl, and keep everything from script_idx
            new_html = html[:start_idx] + html_repl + "\n    " + html[script_idx:]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Successfully replaced in {filename}")
        else:
            print(f"Could not find end of slides in {filename}")
