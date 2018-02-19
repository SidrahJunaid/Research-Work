import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from string import punctuation

txt=open("Yellow RegionWC.txt" , 'r')
data=txt.read()

#create word cloud of food in each region 


# word = ['apple juice','apples','apricots','bananas','blueberries','cantaloupe','cherries','fruit cocktail','grape juice','grapefruit','grapefruit juice','grapes','honeydew','kiwi fruit','lemons','limes','mangoes','nectarines','orange juice','oranges','papaya','peaches','pears','plums','prunes','raisins','raspberries','strawberries','tangerines','watermelon','acorn squash','artichokes','asparagus','avocado','bean sprouts','beets','black beans','bok choy','broccoli','brussels sprouts','butternut squash','cabbage','cassava','cauliflower','celery','collard greens','cowpeas','cucumbers','dark green leafy lettuce','eggplant','field peas','zucchini','white beans','watercress','water chestnuts','turnips','turnip greens','tomato juice','taro','sweet potatoes','split peas','spinach','soy beans','romaine lettuce','red peppers','plantains','pinto beans','okra','navy beans','mustard greens','mushrooms','mesclun','lentils','kidney beans','hubbard squash''bacon','cake','cheese','cookies','donuts','energy drink','fruit drink','hot dogs','icecream','pastries','pizza','sausage','soda','Arby','Baskin Robin','Boston Market','Captain D','Chick-fil-A','Chipotle','Del Taco','Dunkin Donuts','Domino Pizza','Five Guys Burger & fries','Hardees','KFC','Krispy Kreme','McDonald','Panda Express','Pizza Hut','Starbucks','Wendy','Papa Johns','french fries','fried chicken','beer','bread','beef burger']
# for words in word:
#     if words in data:
#         print ()

plt.figure(figsize=(15,10))
wc=WordCloud(background_color='white',mode='RGB',collocations = False, width=500,height=1000).generate(data)
plt.imshow(wc)
plt.axis("off")
plt.show()
