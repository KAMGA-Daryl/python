import pyttsx3
import pyPDF2

livre = open('08 Utilisateurs.pdf','rb')
lecture = pyPDF2.pdffileReader(livre)
pages = lecture.numpages
print(pages)
droid = pyttsx3.init()
#droid.say('')
droid.runAndWait()