# Music Time Machine (YouTube Music Version)

An automated script that crawls the Billboard Hot 100 chart for any date in the past, searches for those songs on YouTube Music, and automatically creates a new playlist in your YouTube Music library containing those songs.

## Getting Started

### Prerequisites

You need to install the required dependencies:
```bash
pip install ytmusicapi beautifulsoup4 requests
```

### Authentication Setup

To interact with your YouTube Music library, you must provide authentication credentials:

1. Copy the `browser.json.example` file and name it `browser.json` in the same directory.
2. Log into [YouTube Music](https://music.youtube.com) in your web browser.
3. Open Developer Tools (F12) -> Network tab.
4. Filter by `/browse` or any API request to `music.youtube.com`.
5. Right-click the request and select **Copy -> Copy as fetch** (or copy headers).
6. Run `ytmusicapi` setup command or paste the headers in JSON format into `browser.json` (specifically the headers such as `cookie`, `authorization`, etc.). Refer to the official [ytmusicapi setup documentation](https://ytmusicapi.readthedocs.io/en/stable/setup.html) for detailed steps.

### Running the App

```bash
python main.py
```
Enter the target date in the format `YYYY-MM-DD` when prompted (e.g., `2010-10-10`). The script will fetch the Billboard Hot 100 for that date and create a new playlist: `YYYY-MM-DD Billboard 100`.
