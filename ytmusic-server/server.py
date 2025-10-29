from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from ytmusicapi import YTMusic

app = FastAPI()
yt = YTMusic()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_music(query: str = Query(...)):
    results = yt.search(query, filter="songs")
    songs = [
        {
            "title": s["title"],
            "videoId": s["videoId"],
            "artists": [a["name"] for a in s["artists"]],
            "thumbnail": s["thumbnails"][-1]["url"],
            "duration": s.get("duration"),
        }
        for s in results
    ]
    return songs
