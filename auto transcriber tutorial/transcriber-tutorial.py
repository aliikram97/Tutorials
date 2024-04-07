import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
import os
class transcriber:
    def __init__(self):
        self.root = tk.Tk(screenName="Transcriber")
        self.current = os.getcwd()
        self.main_dir = os.path.dirname(self.current)
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.root.resizable = (self.height, self.width)
        self.label = tk.Label(text="Transcriber",font=("Arial","50","bold"))
        self.label.pack()
        self.browse_button = tk.Button(self.root, text="Browse Audio File",font=("Arial","20","bold"), command=self.browse_file)
        self.browse_button.pack()

        self.button = tk.Button(text="Transcribe Audio",font=("Arial","12","bold"),command=self.transcribe_text)
        self.button.pack()
        self.file_name = ""

        self.root.mainloop()


    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        self.file_name = file_path

    def show_popup(self,HEADING,message):
        popup = tk.Toplevel()
        popup.title(HEADING)

        label = tk.Label(popup, text=message, padx=20, pady=10)
        label.pack()

        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)

    def transcribe_text(self):
        recognizer = sr.Recognizer()
        audio_file = self.file_name
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            query = recognizer.recognize_google(audio_data, language="auto")
        # self.save_to_text_file(query, str(" Transcribed text"), str(self.main_dir +"/transcribed/") ,"transcription")
        self.show_popup("Transcribed", query)
        return query


transcriber()