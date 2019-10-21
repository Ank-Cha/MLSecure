import sys
import csv
print(sys.maxsize)
csv.field_size_limit(sys.maxsize)

with open('.\Feature_dataset_2019-05-05.csv',
          encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    urls = []
    categories = []
    confi = []
    tokens = []
    for row in readCSV:
        print(row)
        url = row[1]
        category = row[2]
        confidence = row[3]
        token = row[4]

        urls.append(url)
        categories.append(category)
        tokens.append(token)
        confi.append(confidence)


