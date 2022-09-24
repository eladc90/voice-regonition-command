from email.generator import Generator
import string
from threading import Thread
import speech_recognition 
import pyttsx3
import queue
import whisper


class Mic_listener:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self._voice_command_queue = queue.Queue()
        self._whisper_model = whisper.load_model("base")
        
        
    def thread_func(self, recognizer, audio):
        try:
            # language='iw-IL' Hebrew
            self._voice_command_queue.put(recognizer.recognize_google(audio))
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError as e:
            # print("Could not request results from Google Speech Recognition service; {0}".format(e))
            pass
        
            
    def listen_loop(self):
        """
        listen mic in loop and return every text found from 
        mic after recognize using recognize_google method.
        
        return a generator Which can iterate over all the text save as a string.
        """
          
        def callback(recognizer, audio):
            new_th = Thread(target=self.thread_func, args=(recognizer, audio))
            new_th.start()
            
        try:
            r = speech_recognition.Recognizer()
            m = speech_recognition.Microphone()
            with m as source:
                r.adjust_for_ambient_noise(source)  
            stop_listening = r.listen_in_background(m, callback, phrase_time_limit=3) 
            while True:
                text = self._voice_command_queue.get()
                text = text.lower()
                yield text
        except Exception as ex:
            print(ex)

