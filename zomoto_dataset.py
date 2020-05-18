import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import re
import nltk

from datetime import datetime

#dataset = pd.read_csv('Zomato_Reviews.tsv', delimiter = '\t', quoting=3)
dataset = pd.read_csv('zomato.csv')

#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()

"Replacing puncuations and numbers using re library"
row_count = len(dataset)
print("No of rows#" + str(row_count))
for i in range(0,row_count):
    review = dataset["reviews_list"][i]
    review = re.sub('[^a-zA-Z]',' ',review)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    dataset.loc[i,"reviews_list"] = review
    #print(dataset.loc[i,13])
    #print(dataset["reviews_list"][i])
i+=1

#now = datetime.now() # current date and time
#date_time = now.strftime("%Y%m%d_%H%M%S")
#filename = "Restaurant_Reviews_" + date_time + ".csv"
filename = "Restaurant_Reviews.csv"

dataset = pd.DataFrame(dataset)
dataset.to_csv(filename,index=False)
