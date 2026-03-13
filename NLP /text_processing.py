import re
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

