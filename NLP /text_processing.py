import re
import pandas as pd
import string , time

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
and persistence are key to mastering programming.
</p>

"""

rem_pun(para)

df=pd.read_csv('data.csv') # reading the data set using pandas
df['column_name']=df['column_name'].apply(rem_pun) # where df is the file which is being read by pandas and column