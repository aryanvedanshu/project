from gtts import gTTS
import os
import PyPDF2

def text_to_speech_from_text_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()

    tts = gTTS(text=text_content, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)
    os.system("start " + audio_file)

def text_to_speech_from_pdf_file(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text_content = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text_content += page.extractText()

    tts = gTTS(text=text_content, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)
    os.system("start " + audio_file)

# Example usage for a text file
text_to_speech_from_text_file("sample.txt")

# Example usage for a PDF file
text_to_speech_from_pdf_file("sample.pdf")
