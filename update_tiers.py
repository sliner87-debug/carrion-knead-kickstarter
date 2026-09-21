import re

html_path = 'H:\\Antigravity\\Adventure Modules\\The_Carrion_Knead\\kickstarter-mockup\\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the tiers section
# It starts with: <h2 class="section-title" id="tiers">Pledge Tiers</h2>
# And ends before: <h2 class="section-title" id="stretch-goals">Stretch Goals</h2> (or the divider right before it)

new_tiers = """<h2 class="section-title" id="tiers">Pledge Tiers</h2>
                
                <div class="tier-card">
                    <img src="assets/vtt_token_granny_marrow.jpg" alt="Tier 1" class="tier-image">
                    <div class="tier-content">
                        <h3> - The Digital Crumb (PDF)</h3>
                        <p>Get the complete 300+ page Master Omnibus PDF, plus all digital VTT tokens and high-resolution battlemaps.</p>
                    </div>
                </div>

                <div class="tier-card">
                    <img src="assets/vtt_token_harkon_the_lean.jpg" alt="Tier 2" class="tier-image">
                    <div class="tier-content">
                        <h3> - The Baker's Apprentice (Standard Hardcover)</h3>
                        <p>The beautiful, offset-printed Standard Hardcover Omnibus. Also includes the complete Digital Crumb PDF and VTT bundle.</p>
                    </div>
                </div>

                <div class="tier-card">
                    <img src="assets/vtt_token_father_theobald.jpg" alt="Tier 3" class="tier-image">
                    <div class="tier-content">
                        <h3> - The Synaptic Scholar (Hardcover + Accessories)</h3>
                        <p>The Standard Hardcover Omnibus, plus the physical <strong>Tarot Deck of the Unmade</strong> and a set of <strong>Custom Bone-Carved RPG Dice</strong>. Includes all digital rewards.</p>
                    </div>
                </div>

                <div class="tier-card premium-tier">
                    <img src="assets/vtt_token_baron_cassian_vael.jpg" alt="Tier 4" class="tier-image">
                    <div class="tier-content">
                        <h3> - The Whale Tier: "The Butcher's Box"</h3>
                        <p>The ultimate collector's edition. Shipped in a faux-leather butcher's parcel wrapped in butcher paper and twine. Includes the exclusive <strong>Faux-Leather Hardcover Omnibus</strong>, the physical Tarot Deck, Custom Bone Dice, the <strong>Physical GM Screen</strong>, and the <strong>Real-World DM Cookbook</strong>. Includes all digital rewards.</p>
                    </div>
                </div>
                
                <div class="divider"></div>"""

# Replace everything from <h2 class="section-title" id="tiers"> to the divider before stretch goals
pattern = r'<h2 class="section-title" id="tiers">Pledge Tiers</h2>.*?<div class="divider"></div>'
new_html = re.sub(pattern, new_tiers, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
