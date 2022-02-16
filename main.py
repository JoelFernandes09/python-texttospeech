from gtts import gTTS
import os
import PyPDF2

PDFFile = 'sample.pdf'
SaveFileName = 'sample-audio.mp3'

pdfReader = PyPDF2.PdfFileReader(PDFFile)
pages = pdfReader.numPages
print(pages)

for i in range(0, pages):
    myText = pdfReader.getPage(i).extractText()

output = gTTS(myText, lang="en", slow=False, tld="com")
output.save(SaveFileName)
os.system(SaveFileName)
