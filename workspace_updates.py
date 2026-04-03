import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import argparse
from typing import List, Dict, Any, Optional

# Direct Blogger feed filtered to the Gemini label.
# The old FeedBurner URL (feeds.feedburner.com/GoogleAppsUpdates) only ever
# returned the 25 most recent posts across ALL Workspace categories, making
# Gemini results sparse and unreliable. This feed returns Gemini posts only
# and supports max-results/start-index pagination.
BASE_FEED_URL = "https://workspaceupdates.googleblog.com/feeds/posts/default/-/Gemini"
PAGE_SIZE = 100  # Blogger API maximum

def _fetch_page(start_index: int, timeout: int) -> ET.Element:
    """Fetch one page of feed results and return the parsed XML root."""
    params = {
        "max-results": PAGE_SIZE,
        "start-index": start_index,
    }
    response = requests.get(BASE_FEED_URL, params=params, timeout=timeout)
    response.raise_for_status()
    return ET.fromstring(response.content)

def fetch_workspace_updates(days: int) -> None:
    # Validate input
    if days < 1 or days > 365:
        raise ValueError(f"Days must be between 1 and 365, got {days}")

    namespaces = {
        'atom': 'http://www.w3.org/2005/Atom',
        'openSearch': 'http://a9.com/-/spec/opensearchrss/1.0/',
        'blogger': 'http://www.blogger.com/atom/ns#',
    }

    days_ago = datetime.now(timezone.utc) - timedelta(days=days)

    gemini_posts: List[Dict[str, Any]] = []
    total_fetched = 0
    start_index = 1

    try:
        while True:
            root = _fetch_page(start_index, timeout=10)
            entries = root.findall('.//atom:entry', namespaces)

            if not entries:
                break

            done = False
            for entry in entries:
                total_fetched += 1

                published_str = entry.find('atom:published', namespaces).text
                published_date = datetime.fromisoformat(published_str)

                # Entries are returned newest-first; once we go past the window
                # there is no point fetching more pages.
                if published_date <= days_ago:
                    done = True
                    break

                title = entry.find('atom:title', namespaces).text
                link = entry.find("atom:link[@rel='alternate']", namespaces)
                href = link.get('href') if link is not None else "No link available"
                categories = [cat.get('term') for cat in entry.findall('atom:category', namespaces)]

                gemini_posts.append({
                    'title': title,
                    'link': href,
                    'published': published_date,
                    'categories': categories,
                })

            if done or len(entries) < PAGE_SIZE:
                break

            start_index += PAGE_SIZE

        print(f"Feed Statistics:")
        print(f"Total Gemini entries fetched: {total_fetched}")
        print(f"Gemini-related entries in last {days} days: {len(gemini_posts)}\n")

        print(f"Gemini-related updates from Google Workspace (last {days} days):\n")

        if gemini_posts:
            for post in sorted(gemini_posts, key=lambda x: x['published'], reverse=True):
                print(f"Title: {post['title']}")
                print(f"Link: {post['link']}")
                print(f"Published: {post['published'].strftime('%Y-%m-%d %H:%M:%S %Z')}")
                print("Categories:", ", ".join(post['categories']))
                print("-" * 80 + "\n")
        else:
            print(f"No Gemini-related entries found in the last {days} days.")

    except requests.RequestException as e:
        print(f"Error fetching the feed: {e}")
    except ET.ParseError as e:
        print(f"Error parsing the XML content: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main() -> None:
    parser = argparse.ArgumentParser(description='Fetch Gemini-related updates from Google Workspace')
    parser.add_argument('-d', '--days', type=int, default=7,
                      help='Number of days to look back (1-365, default: 7)')
    args = parser.parse_args()
    fetch_workspace_updates(args.days)

if __name__ == "__main__":
    main()
