
# Spotify & Song List Downloader

Batch download MP3s with full metadata from Spotify URLs or a local text list using `spotDL`.

## Setup

```bash
python3 -m pip install spotdl
python3 -m spotdl --download-ffmpeg

```

## Usage

1. Open `main.py` and set `INPUT_TARGET`:
   * **Spotify Link**: `"https://open.spotify.com/playlist/YOUR_ID"`
   * **Text File**: `"songs.txt"` (one song title per line)


2. Run:
   ```bash
   python3 main.py

   ```



   Files save automatically to `./music_downloads/`.
