# Google Workspace Updates Feed Parser

A Python script that fetches and filters Google Workspace update announcements from the official feed, specifically focusing on Gemini-related updates.

## Description

This script fetches the Google Workspace Updates feed (https://feeds.feedburner.com/GoogleAppsUpdates) and filters for posts related to Gemini. It allows you to specify how many days back you want to look for updates and provides statistics about the feed content.

**Note:** This script provides similar functionality to visiting [Google Workspace Updates Blog's Gemini label](https://workspaceupdates.googleblog.com/search/label/Gemini), but does so by programmatically parsing the Feedburner RSS feed. This allows for automated monitoring, custom filtering by date range, and structured output of the updates.

## Features

- Fetches updates from the Google Workspace Updates feed
- Filters for Gemini-related posts
- Configurable time range (default: last 7 days)
- Displays post details including:
  - Title
  - Link
  - Publication date and time
  - Categories
- Provides feed statistics including:
  - Total number of entries
  - Number of recent entries
  - Number of Gemini-related entries

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jgilmour/gworkspace_gemini_updates.git
cd gworkspace_gemini_updates
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage (defaults to last 7 days):
```bash
python workspace_updates.py
```

Specify a custom number of days to look back:
```bash
python workspace_updates.py -d 14
```
or
```bash
python workspace_updates.py --days 14
```

### Command Line Arguments

- `-d, --days`: Number of days to look back (default: 7)
- `-h, --help`: Show help message

## Output Format

The script outputs:

1. Feed Statistics:
   - Total entries in feed
   - Entries from the specified time period
   - Number of Gemini-related entries

2. For each Gemini-related post:
   - Title
   - Link
   - Publication date and time
   - Associated categories

## Error Handling

The script handles various error cases:
- Network connectivity issues
- XML parsing errors
- Empty feeds
- No entries in the specified time range
- No Gemini-related entries

## Contact

For questions, issues, or suggestions:
- GitHub Issues: Feel free to open an issue in this repository
- Email: josh@joshgilmour.com
- Website: [joshgilmour.com](https://joshgilmour.com)
- LinkedIn: [Josh Gilmour](https://www.linkedin.com/in/joshgilmour/)

## License

MIT License

This project is licensed under the MIT License - feel free to use, modify, and distribute the code for any purpose.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements. 