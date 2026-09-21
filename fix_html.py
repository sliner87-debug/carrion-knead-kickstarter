import re

html_path = 'H:\\Antigravity\\Adventure Modules\\The_Carrion_Knead\\kickstarter-mockup\\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken variables in the hero section
html = html.replace('<h2>,500</h2>', '<h2>,500</h2>')
html = html.replace('<p class="pledged-text">pledged of ,000 goal</p>', '<p class="pledged-text">pledged of ,000 goal</p>')

# Add the Risks and Shipping section before the sidebar ends or at the end of the campaign body
risks_section = """
                <div class="divider"></div>
                <h2 class="section-title" id="shipping">Shipping & Fulfillment</h2>
                <p>We have partnered with global fulfillment centers to ensure VAT-friendly shipping to the US, EU, UK, and Australia. Shipping costs will be collected after the campaign via BackerKit based on the actual weight of your pledge tier. Note: The Butcher's Box is incredibly heavy (estimated 6-8 lbs).</p>
                
                <h2 class="section-title" id="risks">Risks and Challenges</h2>
                <p>This is our most ambitious project yet. The core modules are 100% written, playtested, and edited. Our primary risks lie in the physical manufacturing delays of the Collector's Edition Butcher's Box, specifically the custom dice molding and faux-leather binding. We have padded our delivery estimates by 3 months to account for global freight delays.</p>
"""

# Insert right after stretch goals and before the closing tag of the main column
pattern = r'(<h2 class="section-title" id="stretch-goals">.*?</div>\n\n            </div>)'
replacement = r'\1\n' + risks_section

html = re.sub(pattern, risks_section + '\n            </div>', html, flags=re.DOTALL) # wait, re.sub might be tricky.

# Let's do a simple replace
target_string = '</div>\n            <div class="sidebar">'
if target_string in html:
    html = html.replace(target_string, risks_section + '\n            </div>\n            <div class="sidebar">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
