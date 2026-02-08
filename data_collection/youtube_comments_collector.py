from googleapiclient.discovery import build
import pandas as pd
import time

API_KEY = "AIzaSyCKSzTbjHujlh_wXk8kpy7T_TF_PxiQS-g"  

youtube = build("youtube", "v3", developerKey=API_KEY)

SEARCH_QUERY = "book review"
MAX_VIDEOS = 20              # increased from 5 → 20
COMMENTS_PER_VIDEO = 100    # per video (YouTube max per page is 100)

comments_data = []

# Search for videos
search_request = youtube.search().list(
    q=SEARCH_QUERY,
    part="snippet",
    type="video",
    maxResults=MAX_VIDEOS
)
search_response = search_request.execute()

video_ids = [item["id"]["videoId"] for item in search_response["items"]]

print(f"Found {len(video_ids)} videos")

# Fetch comments for each video
for idx, video_id in enumerate(video_ids, start=1):
    video_response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()

    video_title = video_response["items"][0]["snippet"]["title"]

    print(f"\n[{idx}/{len(video_ids)}] Collecting comments for: {video_title}")

    next_page_token = None
    collected = 0

    while collected < COMMENTS_PER_VIDEO:
        comment_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=min(100, COMMENTS_PER_VIDEO - collected),
            pageToken=next_page_token,
            textFormat="plainText"
        )

        comment_response = comment_request.execute()

        for item in comment_response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]

            comments_data.append({
                "video_title": video_title,
                "comment_text": snippet.get("textDisplay", ""),
                "author": snippet.get("authorDisplayName", ""),
                "like_count": snippet.get("likeCount", 0),
                "published_at": snippet.get("publishedAt", ""),
                "source": "youtube"
            })
            collected += 1

        next_page_token = comment_response.get("nextPageToken")
        if not next_page_token:
            break

        time.sleep(0.2)  # small delay to avoid quota spikes

print(f"\nTotal comments collected: {len(comments_data)}")

df = pd.DataFrame(comments_data)
df.to_csv("data/raw/youtube_book_comments.csv", index=False)

print("✅ YouTube comments saved to data/raw/youtube_book_comments.csv")