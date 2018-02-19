
f1 = open("clean_training_data\\clean_tweets_food_USA.txt",'r')
writer = open("clean_training_data\\rem_dup_clean_tweets_food_USA.txt", 'a')
tweet = set()
index = 50
for row in f1:
    if row[:index] not in tweet:
        writer.write(row)
        tweet.add( row[:index] )
f1.close()
writer.close()