import requests
from bs4 import BeautifulSoup

YOUTUBE_TREDNING_URL = 'https://www.youtube.com/feed/trending'

# does not execute Javascript
response = requests.get(YOUTUBE_TREDNING_URL)
print('Status Code:',response.status_code)

with open('trending.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print("Page Title:",doc.title.text)

video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f'found {len(video_divs)} videos')