
import tkinter as tk 
from tkinter import messagebox

import pyttsx3

engine = pyttsx3.init()

def speak():
    text = text_box.get("1.0", tk.END.strip())

    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Input Error, Please Enter some Text.")


def stop():
    engine.stop()

root = tk.Tk()
root.title("SayItSmart - Your Speaking Assistant")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root,bg='#f0f0f0')
frame.pack(pady=20)

label = tk.Label(frame, text="Enter Text to Speak:", font=("Arial",14), bg=("#f0f0f0") )
label.pack(pady=10)

text_box = tk.Text(frame,height=8,width= 40,font=("Arial",14),wrap=tk.WORD)
text_box.pack(pady=10)

speak_button = tk.Button(root, text="Speak", command=speak, font=("Arial",14), bg=("#4CAF50"), fg="white")
speak_button.pack(pady=10)

stop_button = tk.Button(root,text="Stop",command=stop,font=("Arial",14), bg=("#4CAF50"), fg="white")
stop_button.pack(pady=10)

root.mainloop()

