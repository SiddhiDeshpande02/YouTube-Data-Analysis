import requests #type: ignore
import pandas as pd   #type: ignore
import matplotlib.pyplot as plt #type: ignore
import re
from datetime import datetime
import os

csv_file = "youtube_education_trends.csv"

# Load existing data if file exists
if os.path.exists(csv_file):
    master_df = pd.read_csv(csv_file)
else:
    master_df = pd.DataFrame()

# ---------- CONFIGURATION ----------
API_KEY = "API_KEY"  
channels = {
    "FreeCodeCamp": "UC8butISFwT-Wl7EV0hUK0BQ",
    "KhanAcademy": "UC4a-Gbdw7vOaccHmFo40b9g",
    "CrashCourse": "UCX6b17PVsYBQ0ip5gyeme-Q",
    "3Blue1Brown": "UCYO_jab_esuFRV4b17AJtAw",
    "TED-Ed": "UCsooa4yRKGN_zEE8iknghZA"
}
MAX_RESULTS = 50
# -----------------------------------
def get_uploads_playlist(channel):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel}&key={API_KEY}"
    res = requests.get(url).json()
    return res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_videos_from_playlist(playlist_id, max_results=50):
    videos = []
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&maxResults={max_results}&playlistId={playlist_id}&key={API_KEY}"
    res = requests.get(url).json()
    for item in res['items']:
        videos.append({
            'video_id': item['contentDetails']['videoId'],
            'title': item['snippet']['title'],
            'published_at': item['contentDetails']['videoPublishedAt']
        })
    return videos

def get_video_stats(video_ids):
    stats = []
    ids = ",".join(video_ids)
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={ids}&key={API_KEY}"
    res = requests.get(url).json()
    for item in res['items']:
        stats.append({
            'title': item['snippet']['title'],
            'duration': item['contentDetails']['duration'],
            'views': int(item['statistics'].get('viewCount', 0)),
            'likes': int(item['statistics'].get('likeCount', 0)),
            'comments': int(item['statistics'].get('commentCount', 0)),
            'published_at': item['snippet']['publishedAt'],
            'engagement': (int(item['statistics'].get('likeCount', 0)) + int(item['statistics'].get('commentCount', 0))) / int(item['statistics'].get('viewCount', 1)),
            'duration_minutes': parse_duration(item['contentDetails']['duration'])
        })
    return stats


def parse_duration(duration):
    if not duration:
        return 0
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', duration)
    if not match:
        return 0
    hours, minutes, seconds = match.groups()
    total_minutes = (int(hours or 0)*60) + int(minutes or 0) + (int(seconds or 0)/60)
    return total_minutes


for channel_name, channel_id in channels.items():
    print(f"Fetching data for {channel_name}...")

    try:
        playlist_id = get_uploads_playlist(channel_id)
        videos = get_videos_from_playlist(playlist_id, MAX_RESULTS)
        video_ids = [v['video_id'] for v in videos]
        video_stats = get_video_stats(video_ids)
        
        df = pd.DataFrame(video_stats)
        df['channel_name'] = channel_name  # tag each row
        master_df = pd.concat([master_df, df], ignore_index=True)

    except Exception as e:
        print(f"Error fetching {channel_name}: {e}")

master_df.to_csv(csv_file, index=False)
print("All channel data saved successfully!")