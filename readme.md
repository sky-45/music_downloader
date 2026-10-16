# Spotify & Song List Music Downloader

A tool to batch-download audio files as MP3s directly from Spotify playlist URLs or local plain-text song lists. Powered by [`spotDL`](https://github.com/spotDL/spotify-downloader), it automatically embeds track metadata, lyrics, and album cover art into the downloaded files.

---

## Features

- **Multiple Input Types**: Download via Spotify URLs (playlists, albums, tracks) or local text files (`songs.txt`).
- **Full Tagging**: Automatically embeds high-res album art, artist names, track titles, and album metadata.
- **Custom Destination**: Downloads files directly into a structured local repository directory (e.g., `./music_downloads/`).

---

## Prerequisites & Setup

### 1. Requirements
- **Python 3.10+** installed on your system.

### 2. Installation

1. **Clone or download** this repository and navigate into the folder:
   ```bash
   cd ~/projects/music_downloader
