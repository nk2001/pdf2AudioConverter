
#This program reads and saves into a mp3 file format.
#This generates one mp3 file for each page. The resultant audio files are Page{#}.mp3
#Import libraries, text-to-speech (tts), pdfplumber and PDF2
import pyttsx3, pdfplumber, PyPDF2
import sys




def process(file):
    #Make sure the pdf file to be read is in the same directory.
    
    file = file
    
    
    #Create a PDF file object from the file.
    pdfFileObj = open(file, 'rb')
    
    
    #Create a PDF file reader Object from PDF object
    fileReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    #Get the number of pages
    pages = fileReader.numPages
    
    
    #Create a pdf plumber adnd loop through the number of pages in PDF file
    with pdfplumber.open(file) as pdf:
        #Loop through the number of pages. Extract the text and read them out before moving onto next page
        print(pages)
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            afname = "Page"+str(i)+".mp3"
            engine = pyttsx3.init()
            engine.say(text)
            engine.save_to_file(text, afname)
            engine.runAndWait()


def main(argv):
    file = None
    
    if len(sys.argv) != 2:
        print("Usage: pdf_to_audio.py file.pdf")
        return
    else:
        file = str(sys.argv[1])
        
    print(file)
    process(file)
    

if __name__ == "__main__":
    main(sys.argv[1:])


