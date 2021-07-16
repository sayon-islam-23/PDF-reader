import pyttsx3
import pyPDF2

book = open('name of the pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()