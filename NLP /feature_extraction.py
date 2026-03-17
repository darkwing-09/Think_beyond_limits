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

##One Hot Coding
