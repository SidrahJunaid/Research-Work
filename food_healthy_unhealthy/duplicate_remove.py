f1 = open("files\\dup_tweets_healthy.txt",'r')
writer = open("files\\dup_tweets_healthy1.txt", 'a')
tweet = set()
index = 50
for row in f1:
    if row[:index] not in tweet:
        writer.write(row)
        tweet.add( row[:index] )
f1.close()
writer.close()