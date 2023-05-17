#web scraping py
import os
import csv




f = open("C:\Users\angry\Documents\GitHub\osu-map-categorizer\data\osucollectorNumbers.csv", 'r')
#figure out how to iterate csv
for line in f:
    number = int(line.rstrip())
    url = "https://osucollector.com/collections/" + number
