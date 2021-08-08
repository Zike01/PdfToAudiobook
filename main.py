import PyPDF2
import pdfplumber
import pyttsx3

# Get the file name
PDF_FILE = "samples/pdf/Harry-Potter-and-the-Philosopher.pdf"

# Create a PDF file object
pdfFileObj = open(PDF_FILE, 'rb')

# Create a PDF file Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get the number of pages
pages = pdfReader.numPages

# Initialize the pyttsx3 engine
speaker = pyttsx3.init()

# Set the rate of the speaker
speaker.setProperty('rate', 150)

# Create a pdfplumber object and loop through the pages
with pdfplumber.open(PDF_FILE) as pdf:
    text_list = []
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text().split()

        for word in text:
            text_list.append(word)

# Save audio to an mp3 file
MP3_FILE = PDF_FILE.split('/')[-1].split('.')[0] + '.mp3'
speaker.save_to_file(' '.join(text_list), f"samples/mp3/{MP3_FILE}")  
speaker.runAndWait()
