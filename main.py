import PyPDF2
import pdfplumber
import pyttsx3
from tkinter import *
from tkinter import filedialog, messagebox

filename = None


def convert_to_audio(pdf_file, rate):
    # Create a PDF file object
    pdfFileObj = open(pdf_file, 'rb')

    # Create a PDF file Reader Object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Get the number of pages
    pages = pdfReader.numPages

    # Initialize the pyttsx3 engine
    speaker = pyttsx3.init()

    # Set the rate of the speaker
    speaker.setProperty('rate', rate)

    # Create a pdfplumber object and loop through the pages
    with pdfplumber.open(pdf_file) as pdf:
        text_list = []
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text().split()

            for word in text:
                text_list.append(word)

    # Save audio to an mp3 file
    mp3_file = pdf_file.split('/')[-1].split('.')[0] + '.mp3'
    speaker.save_to_file(' '.join(text_list), f"samples/mp3/{mp3_file}")  
    speaker.runAndWait()
    
    # Open messagebox once mp3 file is saved and close window once user clicks 'ok'
    messagebox.showinfo(title="MP3 Saved", message=f"{mp3_file} saved to samples/mp3.")
    window.destroy()
    
    
def select_pdf():
    """
    Opens a dialog box for the user to select a PDF file.
    """
    global filename
    filename = filedialog.askopenfilename(title='Select PDF', filetypes=[
        ("PDF", "*.pdf"),
    ])
    panel.configure(text=filename)
    
    # # Add convert button and slider button
    # Slider
    speaker_rate = Label(text="Set Speaker Rate:")
    speaker_rate.pack()
    
    slider = Scale(window,
                from_=100,
                to=200,
                orient='horizontal'
    )
    slider.pack()
    
    # Buttons
    convert_button = Button(text="Convert to Audio",  command=lambda: convert_to_audio(pdf_file=filename, rate=slider.get()))
    convert_button.pack()


#------------------------------- UI SETUP -------------------------#
window = Tk()
window.title("PDF To Audiobook")
window.geometry('600x200')
window.config(padx=20, pady=20)

# Labels
panel = Label(window, text=" ")
panel.pack()

# Buttons
select_pdf_button = Button(text="Select PDF", command=select_pdf)
select_pdf_button.pack()

window.mainloop()
