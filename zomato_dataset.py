import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting=3)

import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()

"Replacing puncuations and numbers using re library"
data=[]
for i in range(0,1000):
    review=dataset["Review"][i]
    review= re.sub('[^a-zA-Z]',' ',review)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    data.append(review)
i+=1

df = pd.DataFrame(data)
dataset.to_csv("Restaurant_Reviews.csv", index=False)
