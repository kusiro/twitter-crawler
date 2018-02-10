# %%
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import json
import urllib.request
from PIL import ImageFile

twitter = "https://twitter.com/"
hashtag = "hashtag/b3d"
driver = webdriver.Chrome('D:\\tool\\chromedriver.exe')
driver.get(twitter + hashtag)
time.sleep(3)

for i in range(7):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'lxml')

# %%
image = []
likes = []
for tweet in soup.select('.tweet'):
    image.append(tweet.select('.AdaptiveMedia-container img'))
    likes.append(tweet.select('.ProfileTweet-action--favorite .ProfileTweet-actionButton .ProfileTweet-actionCountForPresentation')[0].text)

for i in range(len(image)):
    for j in range(len(image[i])):
        image[i][j] = image[i][j]['src']

# %%

tweet = {}
tweet['Like'] = likes

tweet['Image'] = image

# %%

def getImageSize(uri):
    file = urllib.request.urlopen(uri)
    size = file.headers.get("content-length")
    p = ImageFile.Parser()

    while 1:
        data = file.read(1024)
        p.feed(data)
        if not data:
            break
        if p.image:
            return p.image.width, p.image.height
            break
    file.close()
    return None
tweet['Size'] = []
for i in range(len(tweet['Image'])):
    tweet['Size'].append([])
    for j in range(len(tweet['Image'][i])):
        tweet['Size'][i].append(getImageSize(tweet['Image'][i][j]))


# %%
print(len(tweet['Size']))
json.dump(tweet, open('result.json', 'w'))
# %%
