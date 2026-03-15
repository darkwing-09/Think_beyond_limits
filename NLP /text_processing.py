import re
import pandas as pd
import string , time
import json

def html_tag_rem(text):
    pattern=re.compile('<.*?>')
    return pattern.sub(r'',text)

para=""" <html> <!DOCTYPE html> <html>
<body>
<p>This is <b>bold</b> text.</p>
<p>This is <i>italic</i> text.</p>
<p>This is <u>underlined</u> text.</p>
<p>This is <strong>important</strong> text.</p>
<p>This is <em>emphasized</em> text.</p>
</body>
</html>"""

print(html_tag_rem(p))

##When you use any data set let say df=pd.read_csv('data.csv')
##then you can apply this function to a column of the data set like this
df=pd.read_csv('data.csv') # reading the data set using pandas
df['column_name']=df['column_name'].apply(html_tag_rem) # where df is the file which is being read by pandas and column_name is the name of the column which contains the text data which you want to clean from html tags.

#for removing url 
def url(text):
    pattern=re.compile('https?://\S+|www\.\S+')
    return pattern.sub(r'',text)
url_text="""Hello everyone,

You can visit our main website at https://www.example.com for more information. 
If you want documentation, check http://docs.example.com/guide/start.html.

Our GitHub repository is available at https://github.com/example/project and the 
latest release notes can be found at https://github.com/example/project/releases.

You may also explore learning resources at:
www.coursera.org
www.edx.org
https://openai.com/research

Search engines like https://www.google.com or https://duckduckgo.com are useful 
for finding information quickly.

Here are some URLs with paths and parameters:
https://example.com/products/item?id=1024&ref=homepage
https://blog.example.org/2024/05/ai-future.html
https://news.site.net/article/technology?source=twitter

Some short links:
https://bit.ly/3Example
https://tinyurl.com/samplelink

FTP example:
ftp://files.example.com/downloads/file.zip

Thanks for visiting!"""

print(url(url_text))

df=pd.read_csv('data.csv') # reading the data set using pandas
df['column_name']=df['column_name'].apply(url) # where df is the file which is being read by pandas and column

# For Punctuation marks
remove=string.punctuation
print(remove)

def rem_pun(text):
  for char in remove:
    text=text.replace(char,"")
  return text

para=""""
<p>
Technology is evolving rapidly; every day, developers learn something new. 
Have you ever wondered how the internet works? Well, it’s a combination of 
protocols, servers, and billions of lines of code! Programming languages 
like Python, Java, and JavaScript help developers build applications, 
solve problems, and innovate continuously. Remember: practice, patience, 
and persistence are key to mastering programming.ASAP do the shuff and btw how are you ?
</p>

"""
start1=time.time()
print(rem_pun(para))
time1=time.time()-start1

df=pd.read_csv('data.csv') # reading the data set using pandas
df['column_name']=df['column_name'].apply(rem_pun) # where df is the file which is being read by pandas and column

#The above fun is slightly slow if we compare to the down below

def rem_pun1(text):
  return text.translate(str.maketrans('','',remove))

start2=time.time()
print(rem_pun1(para))
time2=time.time()-start2

#for time comparison 
print((time2/time1)*1000)

#for i.pynb file 


with open("data.ipynb") as f:
    notebook = json.load(f)

cells = []

for cell in notebook["cells"]:
    cells.append({
        "cell_type": cell["cell_type"],
        "content": "".join(cell["source"])
    })

df = pd.DataFrame(cells)
df.to_csv("notebook_content.csv", index=False)
#print(df)   #for Checking the data set you used thsat either the changes have been reverted or not


#for the Slangs used in during the conversation 
slang_list = ["LOL - Laughing out loud", "LMAO - Laughing my ass off", "ROFL - Rolling on the floor laughing", "LMFAO - Laughing my freaking ass off", "BRB - Be right back", "BTW - By the way", "FYI - For your information", "IDK - I don't know", "IDC - I don't care", "IMO - In my opinion", "IMHO - In my humble opinion", "TBH - To be honest", "TBF - To be fair", "SMH - Shaking my head", "OMG - Oh my God", "OMFG - Oh my freaking God", "IKR - I know right", "TTYL - Talk to you later", "GTG - Got to go", "G2G - Got to go", "CU - See you", "CYA - See you", "ASAP - As soon as possible", "BFF - Best friends forever", "ILY - I love you", "ILU - I love you", "ILYSM - I love you so much", "ILY2 - I love you too", "XOXO - Hugs and kisses", "NP - No problem", "NVM - Never mind", "JK - Just kidding", "RN - Right now", "IRL - In real life", "TMI - Too much information", "FOMO - Fear of missing out", "YOLO - You only live once", "BAE - Before anyone else / partner", "DM - Direct message", "PM - Private message", "ICYMI - In case you missed it", "OOTD - Outfit of the day", "TBT - Throwback Thursday", "AMA - Ask me anything", "NSFW - Not safe for work", "AFK - Away from keyboard", "GG - Good game", "GLHF - Good luck have fun", "TY - Thank you", "TYSM - Thank you so much", "THX - Thanks", "PLS - Please", "PLZ - Please", "WTF - What the heck", "WTH - What the heck", "WYD - What are you doing", "WYA - Where you at", "SUP - What's up", "HBU - How about you", "NM - Not much", "K - Okay", "KK - Okay okay", "BRO - Friend or buddy", "DUDE - Friend", "LIT - Very exciting or amazing", "FIRE - Excellent or very good", "GOAT - Greatest of all time", "SUS - Suspicious", "CAP - Lie or fake", "NO CAP - Not lying / serious", "MID - Average / not impressive", "SALTY - Annoyed or bitter", "CRINGE - Embarrassing", "SAVAGE - Bold response", "SLAY - Doing something extremely well", "ICONIC - Legendary or memorable", "W - Win", "L - Loss", "RIZZ - Charisma or flirting ability", "BET - Agreement or okay", "FR - For real", "ONG - On God / serious", "ISTG - I swear to God", "SMTH - Something", "SMBDY - Somebody", "BC - Because", "CUZ - Because", "COS - Because", "B4 - Before", "GR8 - Great", "M8 - Mate", "L8R - Later", "2DAY - Today", "2MORO - Tomorrow", "4U - For you", "B4N - Bye for now", "HAND - Have a nice day", "GM - Good morning", "GN - Good night", "GA - Good afternoon", "TC - Take care", "BDAY - Birthday", "HBD - Happy birthday", "CONGRATS - Congratulations", "GRATS - Congratulations", "OMW - On my way", "ETA - Estimated time of arrival", "WBU - What about you", "FAM - Close friends or family", "SQUAD - Group of friends", "STAN - Obsessive fan", "FLEX - Show off", "HYPE - Excitement or promotion", "DRIP - Stylish fashion", "LOWKEY - Secretly or subtly", "HIGHKEY - Openly or strongly", "MOOD - Relatable feeling", "VIBE - Atmosphere or feeling", "BIG MOOD - Very relatable feeling", "SHOOK - Shocked", "DEAD - Something extremely funny", "SKSK - Expression of laughter or excitement", "AND I OOP - Expression of surprise"]
slang_dict = {item.split(" - ")[0]: item.split(" - ")[1] for item in slang_list}
print(slang_dict)

def normalize_slang(text):
    new_text = []
    for w in text.split():
      if w.upper() in slang_dict:
        new_text.append(slang_dict[w.upper()])
      else:
        new_text.append(w)

    return " ".join(new_text)

df["content"] = df["content"].apply(normalize_slang)
df.head(1)


###For Spelling Correction By TextBlob
from textblob import TextBlob
spel="""I realy dont know why this resturant is so populer. The food was actualy prety good but the servis was terrble and the waitor forgot our order twice. My freind said the place is usualy amazng, but today it felt kind of disapointing. Maybe we just came on a bad day becuase many peple online gave it good reveiws. I hope next time the experiance will be much beter.
"""
textblob_spel = TextBlob(spel)
textblob_spel.correct().string

#By Spell Checker

from spellchecker import SpellChecker

spell = SpellChecker()

text = "I realy dont like Bansal collge"

corrected_text = []

for word in text.split():
    corrected_text.append(spell.correction(word))

print(" ".join(corrected_text))

#For Stop word removing 
import nltk
import string
remove=string.punctuation
print(remove)

def rem_pun(text):
  for char in remove:
    text=text.replace(char,"")
  return text


nltk.download('stopwords')
stopword=stopwords.words('english')
print(stopword)
para=[]
def stop_words(text):
  for word in text.split():
    if word in stopword:
      para.append('')
    elif word.isdigit():
      para.append('')
    elif word.lower() in stopword:
      para.append('')
    elif word.title() in stopword:
      para.append('')
  
    else:
      para.append(word)
  x=para[:]
  para.clear()
  return " ".join(x)

textt="This is a simple example of a paragraph that contains many common words which are often removed during natural language processing. In this text, we are using words like the, is, at, which, on, and for because these words usually do not carry strong meaning in a sentence. When we build an NLP model, we often remove these words so that the model can focus on the more important terms and extract useful information from the data."
punc_re=rem_pun(textt)
print(stop_words(punc_re))


##For Emoji removal and decomile them
#for removal
import re
def remove_emoji(text):
  emoji_pattern = re.compile(
"["
"\U0001F600-\U0001F64F"  # emoticons
"\U0001F300-\U0001F5FF"  # symbols & pictographs
"\U0001F680-\U0001F6FF"  # transport & map symbols
"\U0001F700-\U0001F77F"  # alchemical symbols
"\U0001F780-\U0001F7FF"  # geometric shapes extended
"\U0001F800-\U0001F8FF"  # supplemental arrows
"\U0001F900-\U0001F9FF"  # supplemental symbols & pictographs
"\U0001FA00-\U0001FA6F"  # chess symbols
"\U0001FA70-\U0001FAFF"  # symbols & pictographs extended
"\U00002702-\U000027B0"  # dingbats
"\U000024C2-\U0001F251"
"]+", flags=re.UNICODE) 
  return emoji_pattern.sub(r'', text)
text = "I love NLP 😂🔥🚀 but sometimes it is hard 😅"
print(remove_emoji(text))

#OR
!pip install emoji
import emoji


text = "I love NLP 😂🔥🚀 and Python ❤️"

clean_text = emoji.replace_emoji(text, replace='')

print(clean_text)

#for decompile 
import emoji

text = "I love NLP 😂🔥"

converted = emoji.demojize(text)

print(converted)

##Tokenization By NLTK 
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
text="""Hello! My name is Varun. I'm testing tokenization in NLP systems. 
Email: example@test.com 
Website: https://example.com
Price: $25.99
Date: 15/03/2026
Let's see how well this tokenizer handles punctuation, numbers, and contractions."""
word_tokenize(text)   #Fine but for tokenization we have to strive a lot for our results 


##Tokenization By spaCy(BEST FOR TOKENIZATION)
import spacy 
nlp=spacy.load('en_core_web_sm')
doc1=nlp(text)
doc1
for token in doc1:
  print(token.text)


#STEMMING (REDUCING INFLECTION)
#PORTER STEMMER AND SNOWBALL STEMMER 

#STEMMING - IF YOU WAN TO SHOW RESULTS TO USER AND SPEED MATTERS
#LEMMAITIZATION - IF YOU WANT TO SHOW RESULT TO USER AND SPEED DOES NOT MATTER

#stemming with porter 
from nltk.stem.porter import PorterStemmer
porter=PorterStemmer()

def stem_words(text):
  return " ".join([porter.stem(word) for word in word_tokenize(text)])
text="""The quick brown fox jumps over the lazy dog.
AI is changing the world rapidly.
Tokenization splits text into smaller units called tokens."""
stem_words(text)


#stemming by snowball
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
porter=PorterStemmer()

def stem_words(text):
  return " ".join([porter.stem(word) for word in word_tokenize(text)])
text="""The quick brown fox jumps over the lazy dog.
AI is changing the world rapidly.
Tokenization splits text into smaller units called tokens."""
stem_words(text)


snowball=SnowballStemmer("english")
snowball.stem(text)
tokens = word_tokenize(text)
sn = [snowball.stem(word) for word in tokens]
print(sn)


#LEMMAITIZATION - citation form of word ( root word )  called lemma 

import nltk
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

sentence="""The striped bats are hanging on their feet for best. 
They were running faster than the other animals and studies were being conducted carefully."""
punctuation=",.[]{}/\=_*"
sentence_words=word_tokenize(sentence)
for word in sentence_words:
  if word in punctuation:
    sentence_words.remove(word)
sentence_words

print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
  print("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word,pos=('v'))))

#Text Preprocessing Ended Here 



#links to create dataset
# https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=471
# https://api.themoviedb.org/3/genre/movie/list?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US
