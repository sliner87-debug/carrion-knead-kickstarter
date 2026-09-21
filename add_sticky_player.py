import re

html_path = 'H:\\Antigravity\\Adventure Modules\\The_Carrion_Knead\\kickstarter-mockup\\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

sticky_player_code = """
    <!-- STICKY GLOBAL AUDIO PLAYER -->
    <div id="sticky-audio-player">
        <button id="global-play-btn">▶️</button>
        <div class="scrolling-text-container">
            <span id="now-playing-text">Play Official Soundtrack</span>
        </div>
    </div>

    <script>
        const playlist = [
            { title: "Don't Eat The Bard", src: "assets/dont_eat_the_bard.mp3" },
            { title: "Mistress of the Hearth", src: "assets/mistress_of_the_hearth.mp3" },
            { title: "Yeast of Burden", src: "assets/yeast_of_burden.mp3" }
        ];
        
        let currentTrack = 0;
        const globalAudio = new Audio(playlist[currentTrack].src);
        const playBtn = document.getElementById('global-play-btn');
        const nowPlaying = document.getElementById('now-playing-text');
        
        globalAudio.addEventListener('ended', () => {
            currentTrack++;
            if (currentTrack >= playlist.length) {
                currentTrack = 0; // Loop back to the beginning
            }
            globalAudio.src = playlist[currentTrack].src;
            globalAudio.play().catch(e => console.log(e));
            updateText();
        });

        function updateText() {
            nowPlaying.innerText = "🎵 Now Playing: " + playlist[currentTrack].title;
        }

        playBtn.addEventListener('click', () => {
            if (globalAudio.paused) {
                // If it's the first time playing, make sure source is correct
                if (!globalAudio.src.includes(playlist[currentTrack].src)) {
                    globalAudio.src = playlist[currentTrack].src;
                }
                globalAudio.play();
                playBtn.innerHTML = '⏸️';
                updateText();
            } else {
                globalAudio.pause();
                playBtn.innerHTML = '▶️';
                nowPlaying.innerText = "🔇 Paused";
            }
        });
    </script>
</body>
"""

# Replace the closing body tag with our new code
html = html.replace('</body>', sticky_player_code)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
