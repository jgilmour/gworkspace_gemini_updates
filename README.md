# Google Workspace Updates Feed Parser

A Python command-line tool that fetches and filters Google Workspace update announcements from the official RSS feed, with a focus on Gemini-related updates.

## Overview

This script programmatically monitors the [Google Workspace Updates blog](https://workspaceupdates.googleblog.com) by parsing its RSS feed and filtering for posts tagged with "Gemini". It's designed for:

- **Automated Monitoring**: Track Gemini updates without manually checking the blog
- **Custom Time Ranges**: Query updates from the last 1-365 days
- **Integration-Ready**: Output can be piped to other tools or scripts
- **Quick Scans**: Get a summary of recent Gemini announcements at a glance

**Feed Source**: https://workspaceupdates.googleblog.com/feeds/posts/default/-/Gemini
**Original Source**: https://workspaceupdates.googleblog.com/search/label/Gemini

## Features

- ✅ **Smart Filtering**: Automatically filters for Gemini-tagged posts
- ✅ **Flexible Time Ranges**: Query 1-365 days of history (default: 7 days)
- ✅ **Rich Details**: Shows title, link, date/time, and categories for each post
- ✅ **Feed Statistics**: Displays total entries, recent entries, and Gemini matches
- ✅ **Input Validation**: Prevents invalid date ranges with clear error messages
- ✅ **Robust Error Handling**: Gracefully handles network and parsing errors
- ✅ **Type-Safe**: Fully type-hinted code for better IDE support

## Requirements

- Python 3.7 or higher
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

### Basic Usage

Check for Gemini updates from the last 7 days (default):
```bash
python workspace_updates.py
```

### Custom Time Ranges

Look back 30 days:
```bash
python workspace_updates.py -d 30
# or
python workspace_updates.py --days 30
```

Check the last 90 days:
```bash
python workspace_updates.py --days 90
```

Search the entire year:
```bash
python workspace_updates.py --days 365
```

### Command Line Options

| Option | Short | Description | Valid Range |
|--------|-------|-------------|-------------|
| `--days` | `-d` | Number of days to look back | 1-365 (default: 7) |
| `--help` | `-h` | Show help message and exit | N/A |

### Practical Examples

**Daily check for new updates:**
```bash
python workspace_updates.py -d 1
```

**Weekly summary:**
```bash
python workspace_updates.py -d 7
```

**Monthly overview:**
```bash
python workspace_updates.py -d 30
```

**Save results to a file:**
```bash
python workspace_updates.py -d 30 > gemini_updates.txt
```

**Check for updates and count them:**
```bash
python workspace_updates.py -d 7 | grep -c "Title:"
```

## Output Format

The script displays results in two sections:

### 1. Feed Statistics
```
Feed Statistics:
Total Gemini entries fetched: 8
Gemini-related entries in last 30 days: 8
```

### 2. Gemini Posts (Reverse Chronological Order)
```
Gemini-related updates from Google Workspace (last 30 days):

Title: Gemini Enterprise add-on now available for Google Workspace
Link: https://workspaceupdates.googleblog.com/2024/12/gemini-enterprise-addon.html
Published: 2024-12-10 18:30:00 UTC
Categories: Gemini, Google Workspace, Admin Console
--------------------------------------------------------------------------------

Title: New Gemini features in Google Docs
Link: https://workspaceupdates.googleblog.com/2024/12/gemini-docs-features.html
Published: 2024-12-05 14:15:00 UTC
Categories: Gemini, Google Docs, Productivity
--------------------------------------------------------------------------------
```

### Special Cases

**No Gemini updates found:**
```
Feed Statistics:
Total Gemini entries fetched: 0
Gemini-related entries in last 7 days: 0

Gemini-related updates from Google Workspace (last 7 days):

No Gemini-related entries found in the last 7 days.
```

**Network or parsing errors:**
```
Error fetching the feed: HTTPSConnectionPool(host='workspaceupdates.googleblog.com', port=443): Max retries exceeded
```

## Error Handling

The script provides clear error messages for common issues:

| Error Type | Cause | Example Message |
|------------|-------|-----------------|
| **Invalid Input** | Days outside 1-365 range | `ValueError: Days must be between 1 and 365, got 0` |
| **Network Error** | Cannot reach feed URL | `Error fetching the feed: HTTPSConnectionPool...` |
| **Timeout** | Request takes >10 seconds | `Error fetching the feed: ReadTimeout...` |
| **XML Parsing** | Malformed feed data | `Error parsing the XML content: syntax error...` |
| **No Gemini Posts** | No Gemini-tagged posts in range | `No Gemini-related entries found in the last X days.` |

### Troubleshooting

**Problem**: `Error fetching the feed: Max retries exceeded`
- **Solution**: Check your internet connection. The script times out after 10 seconds.

**Problem**: `ValueError: Days must be between 1 and 365, got X`
- **Solution**: Use a valid day value between 1-365. Example: `python workspace_updates.py -d 30`

**Problem**: No output or empty results
- **Solution**: Try increasing the time range: `python workspace_updates.py -d 90`

## Contact

For questions, issues, or suggestions:
- GitHub Issues: Feel free to open an issue in this repository
- Email: josh@joshgilmour.com
- Website: [joshgilmour.com](https://joshgilmour.com)
- LinkedIn: [Josh Gilmour](https://www.linkedin.com/in/joshgilmour/)

## License

MIT License

This project is licensed under the MIT License - feel free to use, modify, and distribute the code for any purpose.

## What's New

**Version 1.1.1** (2026-04-02)
- Fixed feed source: switched from deprecated FeedBurner URL to the direct Gemini-labeled Blogger Atom feed
- Added pagination so longer date ranges are fully covered

**Version 1.1.0** (2025-12-13)
- ✨ Added type hints for better IDE support
- 🔒 Added 10-second network timeout for improved reliability
- ✅ Added input validation (1-365 day range)
- 📝 Updated documentation with examples and troubleshooting
- 🧪 Added comprehensive test suite

See [CHANGELOG.md](CHANGELOG.md) for complete version history.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.

### Development

To run tests:
```bash
python test_script.py
```

To verify functionality:
```bash
python workspace_updates.py -d 30
``` 