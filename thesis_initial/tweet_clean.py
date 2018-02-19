#-*- encoding: utf-8 -*-

import re

import unicodedata

#tweets cleaning

test_f = open('unhealthy_train_pos.txt')
result_f = open('unhealthy_train_pos1.txt', 'a')
for line in test_f:
    new_str = re.sub('[^a-zA-Z0-9\n\.]'," ", line)
   
    #new_str = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', line)
    #new_str = unicodedata.normalize("NFKD", line)
    result_f.write(new_str)

# also, this too, please:
test_f.close()
result_f.close()