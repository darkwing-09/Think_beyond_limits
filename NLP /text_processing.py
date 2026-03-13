import re
import pandas as pd
def html_tag_rem(text):
    pattern=re.compile('<.*?>')
    return pattern.sub(r'',text)

p=""" <html> <!DOCTYPE html> <html>
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
