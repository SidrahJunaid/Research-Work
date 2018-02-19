
#!pip install Twython
from twython import TwythonStreamer
import sys
import json
import time

tweets = []

class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''
  
    # overriding
    try:
        def on_success(self, data):
            if ('lang' in data and data['lang'] == 'en'):
                #collect tweets state wise
                if ((data['user'])['location']) != None and ('New York City,NY' in ((data['user'])['location']) or 'NYC' in ((data['user'])['location'])  or 'New York City' in ((data['user'])['location']) or 'new york' in ((data['user'])['location'])  or 'NEWYORK' in ((data['user'])['location'])):
                    tweets.append(data)#.encode("utf-8")
                    print ('received tweet #', len(tweets), data['text'].encode("utf-8"))
                    print (data)
                    with open('data\\NewYorkCity_healthy_keywords.txt', 'a') as f:
                         f.write(json.dumps(data['text'].encode("utf-8")) + '\n')

                elif ((data['user'])['location']) != None and ('Los Angeles,CA' in ((data['user'])['location']) or 'Los Angeles' in ((data['user'])['location']) or 'LOS ANGELES,CA' in ((data['user'])['location']) or 'los angeles' in ((data['user'])['location']) or 'los Angeles,California' in ((data['user'])['location'])):
                    tweets.append(data)  # .encode("utf-8")
                    print( 'received tweet #', len(tweets), data['text'].encode("utf-8"))
                    print (data)
                    with open('data\\LosAngeles_TX_healthy_keywords.txt', 'a') as f:
                                 f.write(json.dumps(data['text'].encode("utf-8")) + '\n')



                else:
                    print ('irrelevant')
    except:
        pass

    # overriding
    try:
        def on_error(self, status_code, data):
            print (status_code, data)
            self.disconnect()
    except:
        pass



if __name__ == '__main__':



    # create your own app to get consumer key and secret
    CONSUMER_KEY = '*******************'
    CONSUMER_SECRET = '************************'
    ACCESS_TOKEN = '*******************************************'
    ACCESS_TOKEN_SECRET = '*************************************'

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


    
#To overcome ChunckedEncodingError-IncompleteRead
    counter=0
    while(len(tweets)<5):
        counter+=1
        try:
            if(counter%3!=0):
                #Taken from- https://dev.twitter.com/streaming/overview/request-parameters#track
                #Locations taken from http://boundingbox.klokantech.com/
                #change the location values & run again to get another state or combination of states.
                # track-collect tweets on the basis of keyword here we used food keywords

                stream.statuses.filter(location='-74.2591,40.4774,-73.7003,40.9176,-118.6682,33.7037,-118.1553,34.3373',track=['apple juice','apples','apricots','bananas','blueberries','cantaloupe','cherries','fruit cocktail','grape juice','grapefruit','grapefruit juice','grapes','honeydew','kiwi fruit','lemons','limes','mangoes','nectarines','orange juice','oranges','papaya','peaches','pears','plums','prunes','raisins','raspberries','strawberries','tangerines','watermelon','acorn squash','artichokes','asparagus','avocado','bean sprouts','beets','black beans','bok choy','broccoli','brussels sprouts','butternut squash','cabbage','cassava','cauliflower','celery','collard greens','cowpeas','cucumbers','dark green leafy lettuce','eggplant','field peas','zucchini','white beans','watercress','water chestnuts','turnips','turnip greens','tomato juice','taro','sweet potatoes','split peas','spinach','soy beans','romaine lettuce','red peppers','plantains','pinto beans','okra','navy beans','mustard greens','mushrooms','mesclun','lentils','kidney beans','hubbard squash'],language=['en'],since = "2017-09-01", until = "2014-09-08",)
            else:
                #Taken from - http://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
                #to overcome error: 420 Easy there Turbo, too many requests recently 
                time.sleep(10)
        except:
            continue
