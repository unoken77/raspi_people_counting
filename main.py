from Twitter import my_twitter
from server import client, host

mozi = "#unokumeta"
print('開始')
tweet = my_twitter.get_tweets(mozi, 20)
idsyu = []
for text in tweet["statuses"]:
    idsyu.append(text['id'])

print(idsyu)

while True:
    tweet = my_twitter.get_tweets(mozi, 20)
    for text in tweet["statuses"]:
        if text['id'] not in idsyu:
            if '人数' in text['text']:
                # hostに人数を聞く
                client.cile("人数")
            elif '部屋の様子' in text['text']:
                # hostに部屋の様子の写真を送ってもらう
                client.cile("様子")
            else:
                my_twitter.tweetUpdate("言葉を認識できませんでした")
    idsyu.append(text['id'])
