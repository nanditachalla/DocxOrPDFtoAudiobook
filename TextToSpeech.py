import pyttsx3
import PyPDF2
import ConvertDocxToPDF
import keyboard
import sys
book_name = ""
answer = input(
    "Is the given text in PDF form? press any key if true or else press enter \n")
if(answer):
    pass

else:
    ConvertDocxToPDF.Converter()

book_name = input("Type the book name now with .pdf extension: ")
book = open(book_name, "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                sys.exit()  # finishing the loop
            else:
                break
        except:
            break  # if user pressed
