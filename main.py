import PyPDF2
import pdfplumber
import pyttsx3

# Get the file name
FILENAME = "Harry-Potter-and-the-Philosopher.pdf"

# Create a PDF file object
pdfFileObj = open(FILENAME, 'rb')

# Create a PDF file Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get the number of pages
pages = pdfReader.numPages

# Initialize the pyttsx3 engine
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

# Create a pdfplumber object and loop through the pages
with pdfplumber.open(FILENAME) as pdf:
    text_list = []
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text().split()

        for word in text:
            text_list.append(word)
  
speaker.save_to_file(' '.join(text_list), FILENAME.split('.')[0] + '.mp3')
speaker.runAndWait()
