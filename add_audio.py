import re

html_path = 'H:\\Antigravity\\Adventure Modules\\The_Carrion_Knead\\kickstarter-mockup\\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

audio_section = """<div class="divider"></div>
                
                <h2 class="section-title" id="soundtrack">The Carrion Knead EP: Songs of the Maw</h2>
                <p>Immerse your players in the culinary horror! Every backer tier includes the 3-track promotional EP featuring the exact songs your party will hear echoing through the halls of Mother Gristle's bakery.</p>
                
                <div class="audio-gallery">
                    <div class="audio-track">
                        <h4>Yeast of Burden (Boss Theme)</h4>
                        <audio controls>
                            <source src="assets/yeast_of_burden.mp3" type="audio/mpeg">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    <div class="audio-track">
                        <h4>Don't Eat the Bard (The Scullery Warning)</h4>
                        <audio controls>
                            <source src="assets/dont_eat_the_bard.mp3" type="audio/mpeg">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    <div class="audio-track">
                        <h4>Mistress of the Hearth (Tavern Shanty)</h4>
                        <audio controls>
                            <source src="assets/mistress_of_the_hearth.mp3" type="audio/mpeg">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                </div>
                """

# Insert right after the VTT assets section and before the pledge tiers.
# The VTT section ends with: </div>\n                \n                <div class="divider"></div>\n                \n                <h2 class="section-title" id="tiers">
pattern = r'(<div class="vtt-gallery token-gallery">.*?</div>)\n                \n                <div class="divider"></div>\n                \n                <h2 class="section-title" id="tiers">'
replacement = r'\1\n                \n                ' + audio_section + r'\n                <div class="divider"></div>\n                \n                <h2 class="section-title" id="tiers">'

new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
