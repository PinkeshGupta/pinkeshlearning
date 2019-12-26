import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps=[]
if os.path.isfile("save.txt"):
    with open("save.txt","r")as f :
        TempApp = f.read()
        TempApp = TempApp.split(",")
        apps = [x for x in TempApp if x.strip()]
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.sh" or "*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.system(app) or os.startfile(app)

canvas = tk.Canvas(root,height = 700 , width = 700 , bg ="#263D42")


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx =0.1,rely=0.1)

OpenFile = tk.Button(root, text ="Opem File",padx=10,pady=5,
fg="white", bg="#263D42",command =addApp)

OpenFile.pack(side="bottom")
RunApps = tk.Button(root, text ="Run Apps",padx=10,pady=5,
fg="white", bg="#263D42", command =runApps)

RunApps.pack(side="bottom")


canvas.pack()
 
for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()


root.mainloop()


with open("save.txt","w") as f:
    for app in apps:
        f.write(app+ ',')
