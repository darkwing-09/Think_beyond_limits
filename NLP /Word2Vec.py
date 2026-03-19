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
model.similarity('Virat','player')
model.doesnt_match(['Virat','Rohit','player'])
player=model['Rohit']-model['Virat']+model['Dhoni']
model.most_similar([player])
