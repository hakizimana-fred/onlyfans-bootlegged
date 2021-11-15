import praw
import json
import requests
from random_string import file_random
import os
from flask  import Flask, jsonify
app = Flask(__name__)

def saveToPath():
    path = 'hotimages'
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def save_images(image_urls):
    for image in image_urls:
        extension = os.path.splitext(image)[1]
        img_data = requests.get(image).content
        with open(f'{saveToPath()}/{file_random(10)}.{extension}', 'wb') as handler:
            handler.write(img_data)

    

def main():
    file = open('credentials.json', 'r') 
    data = json.load(file)
    
    reddit = praw.Reddit(
             client_id=data['client_id'],
            client_secret=data['client_secret'],
            user_agent=data['user_agent']
                     )   
    onlyfans_subreddits = ['OnlyFansBrunette', 'OnlyFansReds', 'OnlyFansBlonde']
    
    image_urls = []
    for content in onlyfans_subreddits:
        subreddit = reddit.subreddit(content)
        for submission in subreddit.top(limit=1):
            image_urls.append(submission.url)
    save_images(image_urls)
    return image_urls

@app.route('/onlyfan-girls/', methods=['GET', 'POST'])
def server():
    urls = main()
    return jsonify(urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)