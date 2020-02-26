import pdftotext
 
# Load your PDF
with open("sample.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
 
# Save all text to a txt file.
with open('output.txt', 'w') as f:
    f.write("\n\n".join(pdf))