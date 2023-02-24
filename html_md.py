from jjcli import *
import aspose.words as aw

x = glob("camilo_html_md/*.html")

for y in x:
    doc = aw.Document(y)
    doc.save((y).replace(".html", "") + ".md")