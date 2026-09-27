import re
with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

pattern = r'(<div class="slide[^"]*" id="slide-hall-of-winners".*?)(?:\n\s*<!-- Slide|\n\s*</div>\s*<!-- Progress Bar)'
match = re.search(pattern, index, re.DOTALL)
if match:
    print("Found length:", len(match.group(1)))
    print("Ends with:", repr(match.group(1)[-100:]))
else:
    print("No match")
