# afirmations tests
# started Sat May  7 12:33:37 PDT 2016
# by: Clear Menser
#
import os
import random

#current directory testing no "~" please
os.chdir('/Users/3crows/Dropbox/ai/code/affirmations/')

line = random.choice(open('affirmations.txt').readlines())

line = line[0].upper()+line[1:]

print line

