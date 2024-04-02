import pyaudio
import wave
import tkinter as tk
import os
import threading
import datetime
import time

class recorder:
    def __init__(self):
        self.root = tk.Tk()
        self.current = os.getcwd()
        self.main_dir = os.path.dirname(self.current)
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.root.resizable = (self.height,self.width)
        self.recording = False
        self.button = tk.Button(text="🎤",font=("Arial","120","bold"),command=self.click_handler)
        self.button.pack()
        self.label_recording = tk.Label(text="00:00:00")
        self.label_recording.pack()
        self.recording_file_name = ""

        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.button.config(fg="black")
        else:
            self.recording = True
            self.button.config(fg="red")
            threading.Thread(target=self.record_audio).start()

    def record_audio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        start = time.time()
        while self.recording:
            data = stream.read(1024)
            frames.append(data)
            passed = time.time() - start
            seconds = passed % 60
            minutes = passed // 60
            hours = minutes // 60
            self.label_recording.config(text=f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        # save the recorded input
        current_time = datetime.datetime.now()
        audio_recording_file_path = str(self.main_dir + "/")
        self.recording_file_name = f"recorded_input_{current_time.year}_{current_time.month}_{current_time.day}_{current_time.second}.wav"
        sound_file = wave.open(str(audio_recording_file_path + self.recording_file_name), "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()


recorder()