import re

html_path = 'H:\\Antigravity\\Adventure Modules\\The_Carrion_Knead\\kickstarter-mockup\\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_stretch_goals = """<h2 class="section-title" id="stretch-goals">Stretch Goals</h2>
                <div class="stretch-goal unlocked">
                    <div class="sg-badge sg-unlocked">🔓 0K</div>
                    <div class="sg-text">
                        <h4>UNLOCKED: The Digital Handout Pack</h4>
                        <p>All backers receive a high-res digital pack of printable prop letters, in-universe menus, and wanted posters.</p>
                    </div>
                </div>

                <div class="stretch-goal unlocked">
                    <div class="sg-badge sg-unlocked">🔓 0K</div>
                    <div class="sg-text">
                        <h4>UNLOCKED: Crimson Foil Edges</h4>
                        <p>All physical Hardcovers and Butcher's Boxes will feature gorgeous, blood-red foil stamping on the page edges and covers.</p>
                    </div>
                </div>

                <div class="stretch-goal unlocked">
                    <div class="sg-badge sg-unlocked">🔓 0K</div>
                    <div class="sg-text">
                        <h4>UNLOCKED: Soundtrack of the Maw</h4>
                        <p>A 10-track dark ambient digital soundtrack composed to match the escalating dread of each Tier. Added to all pledge levels.</p>
                    </div>
                </div>

                <div class="stretch-goal locked">
                    <div class="sg-badge sg-locked">🔒 0K</div>
                    <div class="sg-text">
                        <h4>LOCKED: The Sous-Chef's Menagerie</h4>
                        <p>We will add 20 extra pages to the core book featuring new Gastromancy spells, magic items, and culinary abominations.</p>
                    </div>
                </div>

                <div class="stretch-goal locked">
                    <div class="sg-badge sg-locked">🔒 0K</div>
                    <div class="sg-text">
                        <h4>LOCKED: Metal-Core Bone Dice</h4>
                        <p>The Custom Bone Dice in the Synaptic Scholar and Butcher's Box tiers will be upgraded from standard resin to heavy, metal-core resin.</p>
                    </div>
                </div>

                <div class="stretch-goal locked">
                    <div class="sg-badge sg-locked">🔒 00K</div>
                    <div class="sg-text">
                        <h4>LOCKED: The Woven Cloth Canvas Map</h4>
                        <p>A beautiful, durable fold-out cloth map of the entire campaign realm. Added free to all physical pledge tiers!</p>
                    </div>
                </div>"""

# Replace the stretch goals section
# It starts at <h2 class="section-title" id="stretch-goals"> and ends before </div>\n            <div class="sidebar">
pattern = r'<h2 class="section-title" id="stretch-goals">.*?</div>\n            </div>\n            <div class="sidebar">'
replacement = new_stretch_goals + '\n\n            </div>\n            <div class="sidebar">'
new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
