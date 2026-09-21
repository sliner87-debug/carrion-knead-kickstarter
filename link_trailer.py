import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<div class="video-placeholder">', '<a href="trailer.html" style="text-decoration:none;"><div class="video-placeholder">')
html = html.replace('<div class="play-button">?</div>\n                </div>', '<div class="play-button">?</div>\n                </div></a>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
