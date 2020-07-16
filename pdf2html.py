#Required library: 
# pip3 install PyMuPDF
# pip3 install fitz
import sys, fitz


print("hello")

print("hi")
pdf = "sample.pdf"

doc = fitz.open(pdf)
for page in doc:
    html_text = page.getText("html")
with open('output.html', 'w') as f:
    f.write(html_text)
print("hello")
