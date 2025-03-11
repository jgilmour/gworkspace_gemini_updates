import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import argparse

def fetch_workspace_updates(days):
    # URL of the feed
    url = "https://feeds.feedburner.com/GoogleAppsUpdates"
    
    try:
        # Fetch the feed
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the XML content
        root = ET.fromstring(response.content)
        
        # Define namespace mapping
        namespaces = {
            'atom': 'http://www.w3.org/2005/Atom',
            'blogger': 'http://www.blogger.com/atom/ns#'
        }
        
        # Find all entry elements
        entries = root.findall('.//atom:entry', namespaces)
        
        if not entries:
            print("No entries found in the feed. The feed might be empty or the XML structure might have changed.")
            return
            
        # Calculate the date X days ago
        days_ago = datetime.now(timezone.utc) - timedelta(days=days)
        
        # List to store Gemini posts
        gemini_posts = []
        
        total_entries = 0
        gemini_entries = 0
        recent_entries = 0
        
        for entry in entries:
            total_entries += 1
            
            # Get published date
            published_str = entry.find('atom:published', namespaces).text
            published_date = datetime.fromisoformat(published_str)
            
            # Skip if not within specified days
            if published_date <= days_ago:
                continue
                
            recent_entries += 1
                
            # Check if entry has Gemini category
            categories = entry.findall('atom:category', namespaces)
            categories_list = [cat.get('term') for cat in categories]
            
            is_gemini = 'Gemini' in categories_list
            
            if not is_gemini:
                continue
                
            gemini_entries += 1
                
            # Get the title
            title = entry.find('atom:title', namespaces).text
            
            # Get the link
            link = entry.find("atom:link[@rel='alternate']", namespaces)
            href = link.get('href') if link is not None else "No link available"
            
            # Create post info dictionary
            post_info = {
                'title': title,
                'link': href,
                'published': published_date,
                'categories': categories_list
            }
            
            # Add to Gemini posts list
            gemini_posts.append(post_info)
        
        print(f"Feed Statistics:")
        print(f"Total entries in feed: {total_entries}")
        print(f"Entries from last {days} days: {recent_entries}")
        print(f"Gemini-related entries: {gemini_entries}\n")
        
        print(f"Gemini-related updates from Google Workspace (last {days} days):\n")
        
        # Print all Gemini posts sorted by date
        if gemini_posts:
            for post in sorted(gemini_posts, key=lambda x: x['published'], reverse=True):
                print(f"Title: {post['title']}")
                print(f"Link: {post['link']}")
                print(f"Published: {post['published'].strftime('%Y-%m-%d %H:%M:%S %Z')}")
                print("Categories:", ", ".join(post['categories']))
                print("-" * 80 + "\n")
        else:
            if total_entries == 0:
                print("No entries found in the feed.")
            elif recent_entries == 0:
                print(f"No entries found from the last {days} days.")
            elif gemini_entries == 0:
                print(f"No Gemini-related entries found in the last {days} days.")
            
    except requests.RequestException as e:
        print(f"Error fetching the feed: {e}")
    except ET.ParseError as e:
        print(f"Error parsing the XML content: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Fetch Gemini-related updates from Google Workspace')
    parser.add_argument('-d', '--days', type=int, default=7,
                      help='Number of days to look back (default: 7)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the main function with the specified number of days
    fetch_workspace_updates(args.days)

if __name__ == "__main__":
    main() 