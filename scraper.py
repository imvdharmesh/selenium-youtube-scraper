from selenium import webdriver

YOUTUBE_TREDNING_URL = 'https://www.youtube.com/feed/trending'

driver = webdriver.Chrome()

driver.get(YOUTUBE_TREDNING_URL)

print("Page title",driver.title)

