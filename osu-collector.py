#get the data for training
#osucollector number lists for each catagory -> DL all .osu files
#convert to .csv with data points such as length, MAP TEXT DATA, bpm, and of course classification
import os
import csv
# assign directory
directory = r"C:\Users\angry\Documents\GitHub\osu-map-categorizer\test_osu\"
with open("output.csv", 'w') as output:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
    writer = csv.writer(file)
    for subdir in osu.listdir(directory):
        for filename in os.listdir(directory+subdir):
            f = os.path.join(directory+subdir, filename)
            # checking if it is a file
            if os.path.isfile(f):
                writer.writerow[f.read(), subdir]





# iterate over files in
# that directory
#for filename in os.listdir(directory):
#    f = os.path.join(directory, filename)
#    # checking if it is a file
#    if os.path.isfile(f):
#        print(f)
#f = open(r"C:\Users\angry\Documents\GitHub\osu-map-categorizer\test_osu\Imperial Circus Dead Decadence - Uta (Kite) [Himei].osu",'r', encoding="utf8")
#print(f.read())
