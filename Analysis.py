import pandas as pd #type: ignore
import matplotlib.pyplot as plt #type: ignore
import numpy as np #type: ignore
import os

data = pd.read_csv("youtube_education_trends.csv")
'''
#Adding date and time columns
time = data[['published_at']]
# Convert to datetime
time['published_at'] = pd.to_datetime(time['published_at'], utc=True)

# Create new columns
time['date'] = time['published_at'].dt.date
time['time'] = time['published_at'].dt.strftime('%I:%M:%S %p')  # 12-hour format with AM/PM

#insert the time data into the csv
data['date'] = time['date']
data['time'] = time['time']
data.to_csv("youtube_education_trends.csv", index=False)'''


# duration VS Engagement:
x = data['duration_minutes']
y = data['engagement']
plt.scatter(x, y)
plt.xlabel('Duration (minutes)')
plt.ylabel('Engagement')
plt.title('Duration vs Engagement')
plt.show()

#channel VS engegement
channel_engagement = data.groupby('channel_name')['engagement'].mean()
plt.scatter(channel_engagement.index, channel_engagement.values, color='orange')
plt.xlabel('Channel Name')
plt.ylabel('Average Engagement')
plt.xticks(rotation=90)
plt.title('Channel Name vs Average Engagement')
plt.show()

# channel vise views
channel_name = ['3Blue1Brown', 'CrashCourse', 'FreeCodeCamp', 'KhanAcademy', 'TED-Ed']
views = data.groupby('channel_name')['views'].mean()
channel_views = views.tolist()
plt.bar(channel_name, channel_views, color='green')
plt.xlabel('Channel Name')  
plt.ylabel('Average Views')
plt.title('Channel-vise Average Views')
plt.show()

# Views VS Likes
x = data['views']
y = data['likes']
plt.scatter(x, y, color='red')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.title('Views vs Likes')
plt.show()

# Views VS Comments
x = data['views']
y = data['comments']
plt.scatter(x, y, color='purple')       
plt.xlabel('Views')
plt.ylabel('Comments')
plt.title('Views vs Comments')
plt.show()
