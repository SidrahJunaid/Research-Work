from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import Word2Vec


sc = SparkContext(master="local",appName="SparkDemo")

inp = sc.textFile("clean_emojis_healthy_tweets.txt").map(lambda row: row.split(" "))

word2vec = Word2Vec().setWindowSize(15)
model = word2vec.fit(inp)
print(model)

# find the synonym in corpus
term=['squash','artichoke','arugula','asparagus','avocado','basil','beans','beets','bellpepper','blackeyedpeas','broccoli','brusselssprouts','cabbage','capers','carrot','cauliflower','celeriac','celery','chard','peas','chickpeas','chives','collardgreens','cucumber','daikon','eggplant','fennel','garlic','ginger','gourd','greens','hotchillipeppers','iceberglettuce','jicama','kale','leek','lentils','lettuce','maize','mushroom','mustard','okra','olive','onion','parsley','parsnip','pea','peanut','peppers','pickle','pumpkin','radicchio','radish','rhubarb','rocket','romaine','rutabaga','salad','salsa','scallion','seaweed','shallot','soybean','spinach','sprouts','sweetpotato','swisschard','taro','tomatillo','tomato','turnip','vegetable','wasabi','watercress','yam','zucchini','apple','apricot','banana','berry','blackberry','blueberry','cantaloupe','cherry','citrus','coconut','cranberry','date','fig','grape','grapefruit','guava','honeydew','jackfruit','kiwi','lemon','lime','lychee','scallopedpotatoes','wrap','tofu','patty','sauteed','roastedpotatoes','smokedturkey','pudding','teriyakisauce','veggiepizza','tuna','tilapia','salmon','beefstew','burrito','soup','mango','melon','nectarine','orange','papaya','passionfruit','peach','pear','persimmon','pineapple','plantain','plum','pomegranate','capsicum','prune','springonion','quince','raisin','raspberry','strawberry','tangerine','guacamole','omelet','muffin','fish','casserole','veggieburger','meatloaf','watermelon']
for items in term:
  synonyms = model.findSynonyms(items, 5)
  print(items,synonyms)
  f=open("word2vec\\healthy_emotion_word2vec.txt", "a")
  f.write("%s %s\n" %(items,synonyms))




