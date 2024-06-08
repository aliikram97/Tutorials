import speech_recognition as sr
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import filedialog
import os
class translator:
    def __init__(self):
        self.root = tk.Tk(screenName="Translator")
        self.current = os.getcwd()
        self.main_dir = os.path.dirname(self.current)
        self.root.resizable(False, False)  # Make the window not resizable

        self.label = tk.Label(self.root, text="Translator", font=("Arial", "50", "bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        self.browse_button = tk.Button(self.root, text="Browse Audio File", font=("Arial", "20", "bold"),
                                       command=self.browse_file)
        self.browse_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.file_name = ""

        # Language selection
        self.input_lang_var = tk.StringVar(self.root)
        self.output_lang_var = tk.StringVar(self.root)

        self.input_lang_label = tk.Label(self.root, text="Input Language:")
        self.input_lang_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.input_lang_dropdown = tk.OptionMenu(self.root, self.input_lang_var, "english", "urdu-PK", "french",
                                                 "arabic", "german", "hindi")
        self.input_lang_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        self.output_lang_label = tk.Label(self.root, text="Desired Language:")
        self.output_lang_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.output_lang_dropdown = tk.OptionMenu(self.root, self.output_lang_var, "english", "urdu-PK", "french",
                                                  "arabic", "german", "hindi", "pashto")
        self.output_lang_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.button = tk.Button(self.root, text="Translate Audio", font=("Arial", "12", "bold"),
                                command=self.translate_text)
        self.button.grid(row=4, column=0, columnspan=2, pady=20)

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



    def language_selected(self):
        input_language = self.input_lang_var.get()
        desired_language = self.output_lang_var.get()
        if input_language == "english":
            input_lang = 'en'
        elif input_language == "urdu-PK":
            input_lang = 'ur-PK'
        elif input_language == "french":
            input_lang = 'fr'
        elif input_language == "arabic":
            input_lang = 'ar-SA'
        elif input_language == "german":
            input_lang = 'de-DE'
        elif input_language == "hindi":
            input_lang = 'hi-IN'

        if desired_language == "english":
            output_lang = 'en'
        elif desired_language == "urdu-PK":
            output_lang = 'ur'
        elif desired_language == "french":
            output_lang = 'fr'
        elif desired_language == "arabic":
            output_lang = 'ar'
        elif desired_language == "german":
            output_lang = 'de'
        elif desired_language == "hindi":
            output_lang = 'hi'
        print(input_lang,output_lang)
        return input_lang,output_lang


    def transcribe_text(self):
        recognizer = sr.Recognizer()
        audio_file = self.file_name
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            query = recognizer.recognize_google(audio_data, language="auto")
        self.show_popup("Spoken text", query)
        return query

    def translate_text(self):
        input_lang, output_lang = self.language_selected()
        transcribed_query = self.transcribe_text()
        print(transcribed_query)
        translated_query = GoogleTranslator(source='auto', target=output_lang).translate(transcribed_query)
        print(translated_query)
        self.show_popup("Translated text", translated_query)


translator()