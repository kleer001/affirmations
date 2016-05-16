# one off text cleaner

import os


newText = open('affirmations.new','w')


for line in open('affirmations.txt').readlines():
    line = line[0].upper()+line[1:]
    newText.write(line)