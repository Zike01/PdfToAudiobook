import PyPDF2
import pdfplumber
import pyttsx3
from tkinter import *
from tkinter import filedialog, messagebox

#------------------------------- CONSTANTS -------------------------#
BLUE = '#0275D8'
BEIGE = '#F1CCAC'
filename = None


def convert_to_audio(pdf_file, rate):
    if pdf_file:
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
        messagebox.showinfo(title="MP3 Saved", message=f"Successfully saved '{mp3_file}' to samples/mp3.")
        window.destroy()
    else:
        messagebox.showerror(title="Error", message="No pdf file selected, please try again.")
    
    
    
def select_pdf():
    """
    Opens a dialog box for the user to select a PDF file.
    """
    global filename
    filename = filedialog.askopenfilename(title='Choose a file', filetypes=[
        ("pdf file", "*.pdf"),
    ])
    panel.configure(text=filename.split('/')[-1].split('.')[0])
    


#------------------------------- UI SETUP -------------------------#
window = Tk()
window.title("PDF To Audiobook")
window.config(padx=20, pady=20, bg=BEIGE)
window.eval('tk::PlaceWindow . center')

# IMAGE
canvas = Canvas(width=80, height=80, bg=BEIGE, highlightthickness=0)
pdf_icon = PhotoImage(file="assets/pdf-icon.png")
canvas.create_image(40, 40, image=pdf_icon)
canvas.grid(row=0, column=1, padx=30, pady=0)

# LABELS
panel = Label(text="No file selected.", bg=BEIGE)
panel.grid(row=1, column=1, padx=30, pady=0)

# BUTTONS
select_pdf_button = Button(text="Select PDF", bg=BLUE, fg="white", command=select_pdf)
select_pdf_button.grid(row=2, column=1, padx=30, pady=0)

convert_button = Button(text="Convert to Audio", bg=BLUE, fg="white", command=lambda: convert_to_audio(pdf_file=filename, rate=slider.get()))
convert_button.grid(row=2, column=2, padx=30, pady=0)

# SLIDER
speaker_rate = Label(text="Speaker Rate:", bg=BEIGE)
speaker_rate.grid(row=1, column=0, padx=30, pady=0)

slider = Scale(window,
            from_=100,
            to=200,
            orient='horizontal',
            highlightthickness= 0,
            bg=BEIGE
)
slider.grid(row=2, column=0, padx=30, pady=0)

window.mainloop()
