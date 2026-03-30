
#TEXT CLASSFICATION

#types-
# Binary 
 # Multi Level 
# Multi Labelled 



# Modelling 
#ML- Naive , Random Forest
#DL - RNN(LSTM) , CNN , BERT

#Heuristic Approach - When the data is not enough to train model, thus some jugaadu approach is followed 
#Api - https://nlpcloud.com/home/playground/headline-generation , GCP , AWS  generate Api from here for your work case and use them in your model to genrate the results desired. 

# download th4e datset from https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews


import numpy as np
import pandas as pd

print(dataset)
dataset['sentiment'].value_counts()
dataset['review'][1]
dataset.info()
dataset.isnull().sum()
dataset.drop_duplicates(inplace=True)
dataset.duplicated().sum()
import re 
def remove_tags(text):
  cleaned_text=re.sub(re.compile('<.*?>'),'',text)
  return cleaned_text
dataset['review']=dataset['review'].apply(lambda x:x.lower())
dataset['review']=dataset['review'].apply(remove_tags)
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
sw_list=stopwords.words('english')
dataset['review'] = dataset['review'].apply(lambda x: ' '.join([item for item in str(x).split() if item not in sw_list]))
dataset['review'][1]
dataset['review']=dataset['review'].apply(lambda x:''.join(x))
value_counts
print(X)
print(Y)