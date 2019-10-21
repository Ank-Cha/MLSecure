import sys
import csv
import ctypes

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
with open('URL-categorization-using-machine-learning\Datasets\Feature_dataset_2019-05-05.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    urls = []
    categories = []
    confi=[]
    tokens=[]
    for row in readCSV:
        url = row[1]
        category = row[2]
        confidence=row[3]
        token = row[4]
        
        urls.append(url)
        categories.append(category)
        tokens.append(token)        
        confi.append(confidence)

print(tokens)
# new_tokens=[]
# for i in tokens:
#     new_tokens.append(i.lower())
# print(new_tokens)    
