from email.generator import Generator
import string
import speech_recognition
import pyttsx3


class Mic_listener:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        
    
    def listen_loop(self):
        """
        listen mic in loop and return every text found from 
        mic after recognize using recognize_google method.
        
        return a generator Which can iterate over all the text save as a string.
        """
        
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=1)
                    audio = self.recognizer.listen(mic)

                    text = str(self.recognizer.recognize_google(audio))
                    text = text.lower()
                    yield text
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                continue
    

