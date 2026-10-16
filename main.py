import os
import subprocess
import sys
from pathlib import Path


def download_songs(target_input: str, output_folder: str = "downloads"):
    """Downloads songs or playlists into a specified local folder using spotDL.

    :param target_input: A Spotify URL, a search query, or a path to a .txt file.
    :param output_folder: Relative or absolute path to the destination folder.
    """
    # 1. Ensure the output directory exists in your local repo
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    # 2. Define the filename output template inside the target folder
    # Template variables: {artist}, {title}, {output-ext}
    output_template = str(output_path / "{artist} - {title}.{output-ext}")

    # 3. Construct the spotdl command
    command = [
        sys.executable,
        "-m",
        "spotdl",
        "download",
        target_input,
        "--output",
        output_template,
    ]

    print(f"Starting download process for: '{target_input}'")
    print(f"Destination folder: '{output_path.resolve()}'\n")

    try:
        # Execute spotDL sub-process and stream logs to console
        result = subprocess.run(command, check=True)
        if result.returncode == 0:
            print(f"\nSuccessfully downloaded all songs into '{output_folder}/'")
    except subprocess.CalledProcessError as e:
        print(f"\nAn error occurred during download: {e}")
    except FileNotFoundError:
        print(
            "\n'spotdl' module not found. Run 'pip install spotdl' in your environment."
        )


if __name__ == "__main__":
    # --- CONFIGURATION ---
    # Destination folder inside your local repo
    SAVE_FOLDER = "music_downloads"

    # Example A: Download from a local text file (one song name or artist-title per line)
    # INPUT_TARGET = "songs.txt"

    # Example B: Download directly from a Spotify playlist link
    INPUT_TARGET = "https://open.spotify.com/playlist/3OOPFGM0F1Xm6amiu2eCXE?si=cd8cb6346c5849d2"

    # Run the download
    download_songs(target_input=INPUT_TARGET, output_folder=SAVE_FOLDER)