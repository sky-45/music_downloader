import sys
import subprocess
from pathlib import Path


def download_songs(target_input: str, output_folder: str = "music_downloads"):
    """Downloads songs from a Spotify URL, a local text file, or a search query."""
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    output_template = str(output_path / "{artist} - {title}.{output-ext}")

    target_input = target_input.strip()

    # 1. Check if input is a Spotify URL or URI
    if target_input.startswith(("http://", "https://", "spotify:")):
        queries = [target_input]
        print(f"Detected Spotify URL: {target_input}")

    # 2. Check if input is a local .txt file
    elif Path(target_input).is_file() and target_input.endswith(".txt"):
        input_file = Path(target_input)
        queries = [
            line.strip()
            for line in input_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        if not queries:
            print(f"Error: Local file '{target_input}' is empty.")
            return
        print(f"Loaded {len(queries)} track(s) from '{target_input}'")

    # 3. Fallback: Treat as a direct search query (e.g., "Daft Punk - One More Time")
    else:
        queries = [target_input]
        print(f"Detected direct search query: '{target_input}'")

    # Construct and run spotDL command
    command = [
        sys.executable,
        "-m",
        "spotdl",
        "download",
        *queries,
        "--output",
        output_template,
    ]

    print(f"Destination folder: '{output_path.resolve()}'\n")

    try:
        subprocess.run(command, check=True)
        print(f"\nSuccessfully finished downloading into '{output_folder}/'")
    except subprocess.CalledProcessError as e:
        print(f"\nAn error occurred during download: {e}")


if __name__ == "__main__":
    SAVE_FOLDER = "music_downloads"

    # Option A: Local text file
    INPUT_TARGET = "songs.txt"

    # Option B: Spotify Playlist / Album / Track Link
    # INPUT_TARGET = "https://open.spotify.com/playlist/5JKIEHTfrrFCY8qnFHILCo?si=UzyTz0saTj-qHhf4sm1XsQ&utm_source=whatsapp&pi=lH7WkNBTTU-2w"

    download_songs(target_input=INPUT_TARGET, output_folder=SAVE_FOLDER)