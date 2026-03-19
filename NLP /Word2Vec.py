#Word Embedding - It's a technique transforming words into vector so that machine can understand and apply algos to them
#Word2vec - captures sementic meaning of words , its small vector low dimension vector , dense vector i.e non zero(overfitting doesn't occus)

#try in colab
!pip install gensim
!pip install wget
import gensim
from gensim.models import KeyedVectors , Word2Vec
import gensim.downloader as api


model = api.load("word2vec-google-news-300", return_path=True)
print(model)

model = KeyedVectors.load_word2vec_format(
    model,
    binary=True,
    limit=500000   # reduce memory
)

from google.colab import drive
drive.mount('/content/drive')  #save the model for next time on drive
print(model['cricket'].shape)  #checks the number of features the model is trained on , here 300 features are there
model['cricket'] #gives an array representation of that number 
model['cricket']-model['Virat'] +model['Rohit']
model.most_similar('Rohit') #gives the similar entities 
model.similarity('Virat','player')  #The Word2vec understand by matching the simialarity in the vectors of its near angle
model.doesnt_match(['Virat','Rohit','player'])
player=model['Rohit']-model['Virat']+model['Dhoni']
model.most_similar([player])

#Each number is the array of 300 numbers , each numnber is a feature itself

#types of Word2vec
#1 CBOW - CONTINUOUS WORD OF BAG
#CONTEXT WORD IS GIVEN AS INPUT TO FIND OUT THE TARGETTED WORD USING NEURAL NETWORK
# 2 SKIP GRAM
# GIVEN TARGETTED WORD AS INPUT TO FIND OUT THE CONTEXT WORD AS OUTPUT VIA NEURAL NETWORK

# WE CAN INCREASE THE DATASET 
#INCREASE DIMENSION OF VECTOR OR BY INCREASING WINDOW SIZE , IT WILL LATER TAKE LONG TIME 

!pip install gensim
!p`ip install wget
import gensim
from gensim.models import KeyedVectors , Word2Vec
import pandas as pd 
import numpy as np
import os
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess
import nltk
nltk.download('punkt_tab') # Download the specific resource

nltk.download('punkt')
len(words)
model=gensim.models.Word2Vec(window=10,min_count=2,workers=4)
model.build_vocab(words)
model.train(words,total_examples=model.corpus_count,epochs=100)
model.wv.most_similar('king')
model.wv['king']