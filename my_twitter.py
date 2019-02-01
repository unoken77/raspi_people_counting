import re
import time
from datetime import datetime, timedelta

from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
import json

URL = 'https://api.twitter.com/1.1/search/tweets.json'
timelineulr = "https://api.twitter.com/1.1/statuses/user_timeline.json"
tweeturl = "https://api.twitter.com/1.1/statuses/update.json"  # APIの投稿専用URL
UserFollowList = "https://api.twitter.com/1.1/friends/list.json"

KEYS = {
    'consumer_key': '***************************',
    'consumer_secret': '***************************',
    'access_token': '***************************',
    'access_secret': '***************************', }
twitter = OAuth1Session(
    KEYS['consumer_key'],
    KEYS['consumer_secret'],
    KEYS['access_token'],
    KEYS['access_secret'])


# 指定Wordを検索
def get_tweets(search_word, count=100):
    if not search_word:  # 検索文字が無い場合は処理を中断
        print("Plz input 'search_word'")
        return

    params = {'q': search_word, 'count': count}

    req = twitter.get(URL, params=params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        metadata = timeline['search_metadata']
        statuses = timeline['statuses']
        return {
            'result': True,
            'metadata': metadata,
            'statuses': statuses, }
    else:
        print("Error: %d" % req.status_code)
        return {'result': False, 'status_code': req.status_code}


# 指定Wordを投稿
def tweetUpdate(word):
    params = {'status': word}
    req = twitter.post(tweeturl, params=params)

    if req.status_code == 200:  # 投稿成功
        print("投稿成功しました")
    else:
        print("失敗しました")
        print("失敗原因：" % req.status_code)


# フォローリストを取得
def get_followers(screen_name):
    params = {'screen_name': screen_name, 'cursor': -1, 'count': '200', 'skip_status': 'true',
              'include_user_entities': 'false'}
    req = twitter.get(UserFollowList, params=params, verify=True)
    flist = json.loads(req.text)
    return flist


def get_timeline(screen_name):
    params = {'screen_name': screen_name, 'cursor': -1, 'count': '20', 'skip_status': 'true',
              'include_user_entities': 'false'}
    req = twitter.get(timelineulr, params=params)
    timeline = json.loads(req.text)

    return timeline


def APIpass(count):  # ただ15分待ちましょう
    td = datetime.now() + timedelta(minutes=15)
    if count >= 15:
        print("ちょっと疲れた　_(:3」∠)_")
        print("つづきは" + td.strftime("%Y/%m/%d %H:%M:%S"))

        time.sleep(960)
        return 0
    return count


#########################################################################
# 時間整形以下
def make_convert_date_format(src_format, dst_format):
    def convert_date_format(s):
        return datetime.strftime(
            datetime.strptime(s, src_format),
            dst_format
        )

    return convert_date_format


convert_date_format = make_convert_date_format(
    '%a %b %d %H:%M:%S %z %Y', '%Y-%m-%d %H:%M:%S'
)


def retimenuber(time):
    dst = re.sub(r'-', '', time)
    dst = re.sub(r' ', '', dst)
    dst = re.sub(r':', '', dst)
    return dst

##################################################################
