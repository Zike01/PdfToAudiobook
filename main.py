import PyPDF2
import pdfplumber
import pyttsx3

# Get the file name
FILENAME = "sample.pdf"

# Create a PDF file object
pdfFileObj = open(FILENAME, 'rb')

# Create a PDF file Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get the number of pages
pages = pdfReader.numPages

# Create a pdfplumber object and loop through the pages
with pdfplumber.open(FILENAME) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)

        # Initialize the pyttsx3 engine
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
