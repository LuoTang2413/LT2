import requests
from feishu_sdk import FeishuRobot

# Define the RSS feed URLs
rss_feeds = [
    "https://example.com/rss/feed1",
    "https://example.com/rss/feed2",
    "https://example.com/rss/feed3",
    # Add more feed URLs as needed
]

# Fetch RSS feed data from each feed URL
rss_data = ""
for feed_url in rss_feeds:
    response = requests.get(feed_url)
    rss_data += response.text

# Send message to Feishu robot API
robot = FeishuRobot("YOUR_ROBOT_ACCESS_TOKEN")
message = {
    "msg_type": "text",
    "content": {
        "text": rss_data
    }
}
robot.send_message(message)
