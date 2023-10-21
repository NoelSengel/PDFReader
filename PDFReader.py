import pyttsx3, PyPDF2

title = input("Which book would you like to listen to?\n") + ".pdf"
pdfreader = PyPDF2.PdfReader(open(title, 'rb'))
speaker = pyttsx3.init()

first_page = input("Starting with what page?\n")
last_page = input("Ending with what page?\n")

text = ""

for page_number in range(int(first_page - 1), int(last_page)):
      text = text + pdfreader.pages[page_number].extract_text()

clean_text = text.strip().replace('\n', ' ')
print(clean_text)

speaker.save_to_file(clean_text, 'result2.mp3')
speaker.runAndWait

speaker.stop()
