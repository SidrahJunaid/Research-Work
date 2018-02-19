# -*- coding: utf-8 -*-
import fileinput
from collections import defaultdict

class food_classify(object):
    def food_senti(self):

        # creating dictionary from food lexicon with score
        with open("food_list_lexicon.txt") as f:
            fields = {}
            for line in f:
                x = line.split(",")
                s = x[0]
                b = x[1]
                fields[s] = b.strip("\n")

        print(fields)

        # opening text file and assigning it healthy or unhealthy on the basis of term frequency in text
        text=("clean_vader_results\\data\\final.txt")



        for line in fileinput.input(text, inplace=False):
            line = line.rstrip().lower()
            final_result = defaultdict(int)
            if not line:
                    continue
            for f_key, f_value in fields.items():

                    if (f_key in line) and f_value== '1':

                        final_result['healthy']+=1
                    elif (f_key in line) and f_value== '0':
                        final_result['unhealthy'] +=-1


            #try:
            if final_result['healthy'] != 0 or final_result['unhealthy'] != 0:

                final_result['compound']=( final_result['healthy']+final_result['unhealthy'])/((final_result['healthy'])-(final_result['unhealthy']))
                if final_result['compound']==0:
                #writing it on text file
                 print('{},final:{}'.format(line,dict(final_result)),file=open("clean_vader_results\\data\\food_tweets.txt", "a"))


                if final_result['compound']>0:
                    #
                     # print(line),file=open("clean_vader_results\\data\\positive_food_sentiment.txt", "a"))
                      print(line)

                elif final_result['compound']<0:
                    print(line)#, file=open("clean_vader_results\\data\\negative_food_sentiment.txt", "a"))

                else:
                    print(line, file=open("clean_vader_results\\data\\neutral_food_sentiment.txt", "a"))
                        #
                #     #f.write('{}'.join(dict(final_result)))
                    print('final:{}'.format(dict(final_result))),file=open("validated_results_vader\\texas_unhealthy_vader_pos.csv", "a"))
                #     print(line, file=open("training_results_vader\\texas_unhealthy_vader_pos.txt", "a"))


obj=food_classify()
obj.food_senti()
