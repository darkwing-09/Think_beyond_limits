#Garbage In -> Garbage Out , bad algo can better results with better input and vice versa
#Better the feature better the input
#Here We'll change text into numbers and it's one of the difficult processess if we compare to feature extraction of image or audio-clip

#Common words Which we'll follow up are - 
# Corpus - the concatenation of all words from all the dataset { e.g If dataset have 100 col , the the corpus is adding the each column text and concatenate in to make a big string }
#Vocab - Its the unique words the corpus is made up of 
#Document - Each column is a document , i.e each unique representation is document 
#word - each token in the corpus is word


#eg
"""
doc_id,document
1,"I love learning NLP"
2,"This system is very slow"
3,"Book a bus ticket for Delhi"
4,"Where is my order now"
5,"Cancel my booking immediately"
6,"The service was excellent"
7,"I am not happy with this product"
8,"Track my bus location"
9,"How to reset my password"
10,"The app crashes frequently"
11,"Show available buses to Lucknow"
12,"Payment was successful"
13,"Refund my money"
14,"Login is not working"
15,"I want to change my seat"
"""

#corpus - I love learning NLP This system is very slow Book a bus ticket for Delhi Where is my order now Cancel my booking immediately The service was excellent I am not happy with this product Track my bus location How to reset my password The app crashes frequently Show available buses to Lucknow Payment was successful Refund my money Login is not working I want to change my seat
"""vocab -['a','am','app','available','book','booking','bus','buses','cancel','change',
'crashes','delhi','excellent','for','frequently','happy','how','i','immediately',
'is','learning','location','login','love','lucknow','money','my','nlp','not',
'now','order','password','payment','product','refund','reset','seat','service',
'show','slow','successful','system','the','this','ticket','to','track','very',
'was','want','where','with','working']"""
#words = 52

##One Hot EnCoding

#It produces the sparse matrix and the order of matrix is not fixed , and to ML models the fix input is always given
#e.g

# I1=I am Varun Dev                             I am Varun Dev studying NLP works on
# I2=I am studying NLP
# I3=Varun works on NLP
 # I1=[[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0]] , I2=[[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0]] , I3=[[0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,0]]
# And if any how any input as I4 came in as = I am varun dev mishra , them the order will be 5*8 and mishra is not in words , then the model will be more confused rater training


#SO THE PROMBLEMS ARE -
#SPARSITY
#OOV- OUT OF VOCAB
# NO FIXED SIZE 
#NO CAPTURING OF SEMENTIC MEANING



#2 - BAG OF WORDS
"""
What it does:

Takes text

Breaks it into words

Builds a vocabulary

Counts how many times each word appears
""" 
#IT TELLS THAT THE OCCURENCE OF WORS I THE DOCUMENT AND REST IS SAME AS ONE HOT ENCODING
# I1=I am Varun                             I am Varun is loves Dev
# I2=Varun is Varun
# I3=Varun loves Dev
 # I1=[1,1,1,0,0] , I2=[0,0,2,1,0], I3=[0,0,1,0,1,1]
#CONTEXT AND SEMENTIC MEANING IS MEANT

# uRl = https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
#must go 
#class sklearn.feature_extraction.text.CountVectorizer(*, input='content', encoding='utf-8', decode_error='strict', strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None, stop_words=None, token_pattern='(?u)\\b\\w\\w+\\b', ngram_range=(1, 1), analyzer='word', max_df=1.0, min_df=1, max_features=None, vocabulary=None, binary=False, dtype=<class 'numpy.int64'>)

import pandas as pd
import numpy as np
df = pd.read_csv('/content/NLP_DATA - Sheet1(1).csv')
print(df)
df = df.dropna(axis=1, how='all')
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
bow=cv.fit_transform(df['text'])
print(cv.vocabulary_)   # Removes stopword
#Array 
print(bow[0].toarray())
print(bow[1].toarray())
print(bow[2].toarray())