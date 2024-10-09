
import tkinter as tk 
#Tkinter is the standard Python interface to the Tk GUI toolkit, allowing you to create graphical user interfaces (GUIs) in Python.
from tkinter import messagebox
#message box is added to display errors.
import pyttsx3 #Importing Text to speech in the program
from PIL import Image, ImageTk  # Images and Background Image support
import threading #Import Threading to run speech in background.

engine = pyttsx3.init()
#initialize text-to-speech engine

def speak():
    text = text_box.get("1.0", tk.END.strip()) #Get Text from Text Box

    if text: #Checks if text box is not empty
        threading.Thread(target=speak_text,args=(text,)).start() #it now starts a new thread using threading
    else: #Displays error if text box is empty
        messagebox.showwarning("Input Error, Please Enter some Text.")

def speak_text(text):
    try:
        engine.say(text) #converts text to speech 
        engine.runAndWait()
    except Exception as e:
        print(f"Error while speaking: {e}")

def stop(): #Stop the speech
    engine.stop()

#Create Main Menu
root = tk.Tk()
root.title("SayItSmart - Your Speaking Assistant")
root.geometry("500x400")
root.resizable(False,False)

#Load Background Image
background_image = Image.open("background.jpg")
background_image = background_image.resize((500,400))
bg_image = ImageTk.PhotoImage(background_image)

#Create a label to display the background Image
background_label = tk.Label(root,image=bg_image, text="Enter Text to Speak:" )
background_label.place(relheight=1, relwidth=1) #Make it Fill the window

#Frame for main content
frame = tk.Frame(root,bg='#2E2B2B',bd=5)
frame.place(relx=0.5,rely=0.5, anchor=tk.CENTER)

#Create a table for instruction text
label = tk.Label(frame, text="Enter Text to speak", font=("Arial",12),fg="#D1C4E9",bg="#2E2B2B")
label.pack(pady=10)

#Text box or the Input Box
text_box = tk.Text(frame,height=5,width= 40,font=("Arial",10),fg="black",bg="#FFFFFF",insertbackground="white")
text_box.pack(pady=10)

button_style = {
    "font":("Arial",10),
    "bg":("#9C27B0"), 
    "fg" : "white",
    "width" : 8,
    "height" : 1,
    "relief" : "raised",
    "bd" : 3,
}

#Speak Button, whenever you click it, it starts speaking
speak_button = tk.Button(frame, text="Speak", command=speak,**button_style )
speak_button.pack(pady=2, padx=2)

#stopping the speaking when the button is clicked
stop_button = tk.Button(frame,text="Stop",command=stop, **button_style)
stop_button.pack(pady=2, padx=2)

#Add a footer Label
footer_label = tk.Label(root, text="Created By Saniya Imroze", font=("Arial",8) )
footer_label.place(relx=0.5,rely=0.95, anchor=tk.CENTER)

root.mainloop()

