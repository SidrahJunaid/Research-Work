# file = open('Green_Region_Clean.txt', 'r')
# book = file.read()
#
#
# def tokenize():
#     if book is not None:
#         words = book.lower().split()
#         return words
#     else:
#         return None
#
#
# def count_word(tokens, token):
#     count = 0
#
#     for element in tokens:
#         # Remove Punctuation
#         word = element.replace(",", "")
#         word = word.replace(".", "")
#
#         # Found Word?
#         if word == token:
#             count += 1
#     return count
#
#
# # Tokenize the Book
# words = tokenize()
#
# # Get Word Count
# # word = ['apple juice','apples','apricots','bananas','blueberries','cantaloupe','cherries','fruit cocktail','grape juice','grapefruit','grapefruit juice','grapes','honeydew','kiwi fruit','lemons','limes','mangoes','nectarines','orange juice','oranges','papaya','peaches','pears','plums','prunes','raisins','raspberries','strawberries','tangerines','watermelon','acorn squash','artichokes','asparagus','avocado','bean sprouts','beets','black beans','bok choy','broccoli','brussels sprouts','butternut squash','cabbage','cassava','cauliflower','celery','collard greens','cowpeas','cucumbers','dark green leafy lettuce','eggplant','field peas','zucchini','white beans','watercress','water chestnuts','turnips','turnip greens','tomato juice','taro','sweet potatoes','split peas','spinach','soy beans','romaine lettuce','red peppers','plantains','pinto beans','okra','navy beans','mustard greens','mushrooms','mesclun','lentils','kidney beans','hubbard squash''bacon','cake','cheese','cookies','donuts','energy drink','fruit drink','hot dogs','icecream','pastries','pizza','sausage','soda','Arby','Baskin Robin','Boston Market','Captain D','Chick-fil-A','Chipotle','Del Taco','Dunkin Donuts','Domino Pizza','Five Guys Burger & fries','Hardees','KFC','Krispy Kreme','McDonald','Panda Express','Pizza Hut','Starbucks','Wendy','Papa Johns','french fries','fried chicken','beer','bread','beef burger']
# # for word1 in word:
#     frequency = count_word(words)
#     #print(word1)
#     print('Word: [' + (word1) + '] Frequency: ' + str(frequency))

#


word_list = ['apple juice','apples','apricots','bananas','blueberries','cantaloupe','cherries','fruit cocktail','grape juice','grapefruit','grapefruit juice','grapes','honeydew','kiwi fruit','lemons','limes','mangoes','nectarines','orange juice','oranges','papaya','peaches','pears','plums','prunes','raisins','raspberries','strawberries','tangerines','watermelon','acorn squash','artichokes','asparagus','avocado','bean sprouts','beets','black beans','bok choy','broccoli','brussels sprouts','butternut squash','cabbage','cassava','cauliflower','celery','collard greens','cowpeas','cucumbers','dark green leafy lettuce','eggplant','field peas','zucchini','white beans','watercress','water chestnuts','turnips','turnip greens','tomato juice','taro','sweet potatoes','split peas','spinach','soy beans','romaine lettuce','red peppers','plantains','pinto beans','okra','navy beans','mustard greens','mushrooms','mesclun','lentils','kidney beans','hubbard squash''bacon','cake','cheese','cookies','donuts','energy drink','fruit drink','hot dogs','icecream','pastries','pizza','sausage','soda','Arby','Baskin Robin','Boston Market','Captain D','Chick-fil-A','Chipotle','Del Taco','Dunkin Donuts','Domino Pizza','Five Guys Burger & fries','Hardees','KFC','Krispy Kreme','McDonald','Panda Express','Pizza Hut','Starbucks','Wendy','Papa Johns','french fries','fried chicken','beer','bread','beef burger']

# i'm using this example text in place of the file you are using
text = open('SanAJose_Clean.txt','r')
textr=text.read()
text1 = textr.replace(',', ' ')  # these statements remove irrelevant punctuation
text1 = textr.replace('.', '')
text1 = textr.lower()  # this makes all the words lowercase, so that capitalization wont affect the frequency measurement

for repeatedword in word_list:
    counter = 0  # counter starts at 0
    for word in text1.split():
        if repeatedword.lower() == word:
            counter = counter + 1
            #print(repeatedword)
            # add 1 every time there is a match in the list
    print(repeatedword, ':', counter)  # prints the word from 'word_list' and its frequency