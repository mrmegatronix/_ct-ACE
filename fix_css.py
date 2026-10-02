import re

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix unified-title
css = css.replace("""
.unified-title {
    font-family: 'Playfair Display', serif !important;
    font-family: 'Inter', sans-serif !important;""", """
.unified-title {
    font-family: 'Playfair Display', serif !important;""")

css = css.replace("""
.unified-title {
    font-family: 'Inter', sans-serif !important;""", """
.unified-title {
    font-family: 'Playfair Display', serif !important;""")

with open('/run/media/zeus/6TB-1/__GITHUB NUC/_ct-ACE/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
