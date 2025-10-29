App Name: Twii

Tech Stack:
- Frontend: React Native (Expo)
- Styling: TailwindCSS v3.4.17 via NativeWind
- Backend: FastAPI (Python) using ytmusicapi for fetching YouTube Music metadata
- Audio playback: expo-av
- Downloads: expo-file-system
- Fonts: Rounded, playful, cozy cat-style fonts (Comic Neue, Poppins, Quicksand)
- Colors: pastel palette — cream, lilac, blush pink, sky blue, mint, warm gray
- Art style: Furry / Swiggly / Wiggly Cat Aesthetic — soft paw-shaped buttons, rounded corners, fuzzy icons, gentle motion

App Concept:
"Twii" is a cute, cat-themed music player and downloader that lets users search, play, and collect songs. The UI feels warm, cozy, and alive, like a small furry creature curating music for you.

App Features:

1. Home / Search Screen
- Top search bar with placeholder text: "Search your purr-fect tune..."
- Rounded paw-shaped search button
- Fetch results from backend endpoint /search?query= (powered by ytmusicapi)
- Display list of songs:
  - Thumbnail (rounded edges)
  - Title + artist
  - Play ▶ and Download ↓ buttons styled as paw pads
- Soft hover animations (wiggly / bouncy motion)

2. Player Screen
- Large rounded player card with album art
- "Now Playing" cat-ear banner
- Play / Pause / Skip buttons shaped like cat paws
- Animated waveform that wiggles with sound
- Pastel-colored glowing progress bar
- Optional "Meowify" mode (adds subtle purring background loop)

3. Downloads Page
- Shows downloaded songs
- Small sleeping-cat icon when empty
- Uses expo-file-system for storing and listing files

4. Settings
- Theme toggle (Light / Dark / Catnip Mode)
- Font selector (default: Poppins Rounded)
- Optional login/profile (future feature)

Backend:
Use FastAPI + ytmusicapi with routes:
GET /search?query=believer
→ Returns JSON with { title, videoId, artists, thumbnail, duration }

GET /stream/{videoId}
→ Returns streaming URL or proxy (optional)

GET /download/{videoId}
→ Returns downloadable .mp3 or redirect link

Enable CORS for all origins in dev mode.

Design Language:
- Fully rounded shapes, no sharp corners
- Soft shadows, pastel gradients
- Buttons shaped like cat paws, sliders shaped like tails
- Animated transitions using reanimated or framer-motion style easing
- Background gradient blush pink → lavender
- Icons shaped like paws, ears, whiskers
- Splash screen: sleeping cat with headphones fading into the main UI

App Flow:
1. User opens Twii → splash with sleeping cat
2. Lands on Search screen
3. Enters song → fetches from FastAPI (ytmusicapi)
4. Plays song → cute animation plays
5. Can tap Download → saves locally
6. Plays offline from Downloads tab

UI Text Style:
Friendly and lighthearted tone.
Examples:
"Fetching your meow-sical vibes..."
"Nothing found, maybe try a different tune?"
"Downloading... don't pull my tail"
"Now Purring: {song_title}"

Expo Packages to Include:
expo-av
expo-file-system
nativewind
react-navigation
react-native-reanimated
react-native-vector-icons

Extra Notes:
- Must support Android and iOS
- Subtle motion and paw hover effects
- Background ambient animation (floating cat ears or paw prints)
- Pastel transitions and glowing hover states
- Use FlatList for search results for performance

Output Requirements:
Windurf should generate:
1. Complete Expo React Native app (frontend)
2. FastAPI backend with ytmusicapi setup
3. Functional search → play → download flow
4. Tailwind-styled components (SongCard, PlayerBar, SearchBox)
5. Basic assets: pastel paw icons, Twii cat-ear text logo

Tagline:
Twii — your personal music whisker
