
# collect_tweets.py


from TwitterAPI import TwitterAPI
import re
import sys
import time
import os
tweet_list = []
# donald = []

# twitter keys

consumer_key = '**************************'
consumer_secret = '******************************'
access_token_key = '***********************************'
access_token_secret = '*************************************'



def get_twitter():
    return TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)



def robust_request(twitter, resource, params, max_tries=5):
    for i in range(max_tries):
        request = twitter.request(resource, params)
        if request.status_code == 200:
            return request
        else:
            print('Got error %s \nsleeping for 15 minutes.' % request.text)
            sys.stderr.flush()
            time.sleep(61 * 15)


def get_tweets(twitter):

    c = 0


    nd=open("nodes.txt","w")
    tw = open("tweets_healthy.txt","a", encoding="utf-8")
    while True and c<=200:

        r = robust_request(twitter,'statuses/filter', {'track':['artichoke','asparagus','avocado','basil','beans','beets','bell pepper','black eyed peas','broccoli','brussels sprouts','cabbage','capers','carrots','cauliflower','celery','chard','peas','chives','collard greens','cucumbers','dandelion greens','eggplant','fennel','garlic','ginger','gourd','hot chile peppers','iceberg lettuce','kale','leek','lentils','lettuce','maize','mushroom','mustard greens','okra','olives','onion','parsley','parsnip','pattypan squash','peppers','pickle','pumpkin','radicchio','radish','romaine','salad','salsa','scallion','seaweed','shallot','soybean','spinach','sprouts','sweet potato','swiss chard','taro','tomatillo','tomato','turnip','wasabi','water chestnut','yam','zucchini','apples','apricot','banana','berries','blackberries','blueberry','breadfruit','cantaloupe','cherries','coconut','cranberry','fig','grape','grapefruit','guava','honeydew','kiwi','lime','lychee','scalloped potatoes','baked sweet potatoes','vegetable wrap','tofu','black beans patty','sauteed spinach and tomatoes','roasted potatoes','green beans potatoes','smoked turkey','corn pudding','teriyaki sauce','veggie pizza','tuna and noodles','vegetable rice','roasted tilapia','roasted salmon','beef stew','bean burrito bowl','chicken tetrazzini','sweet and sour pork','pico del gallo','vegetable soup','broiled tomatoes and cheese','mandarin orange','mango','melon','nectarine','oranges','papaya','passion fruit','peach','pear','persimmon','pineapple','plantain','plum','pomegranite','capsicum','prune','spring onion','quince','raisin','strawberry','tangerine','guacamole','green onion omelet','raisin muffin','baked fish','chicken casserole','veggie burger','meatloaf'],'language':'en'})
        for item in r:

            tweet = item['text']
            if not tweet.startswith('RT') and tweet not in tweet_list:
                tweet = re.sub('@[^\s]+','',tweet)
                tweet=tweet.replace("\n", " ")


                tweet = tweet.strip()

                tweet_list.append(tweet)
                tw.write(tweet)
                tw.write("\n")

                c +=1
                if c >= 1000:
                    break
    nd.close()
    tw.close()



def main():
    twitter = get_twitter()
    get_tweets(twitter)



if __name__ == '__main__':
    main()

