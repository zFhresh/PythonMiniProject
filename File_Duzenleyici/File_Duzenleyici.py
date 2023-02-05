from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
import FileLib as FB;
import tkinter.ttk
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

Master = tkinter.Tk()

Master.geometry("600x600")

Master.title("Dosya düzenleyici")

Photo = tkinter.PhotoImage(file="pic\\test.png")

Master.iconphoto(False,Photo)


def CreateNewLabel(Text,font):
    NewLabel = Label(Master,text=Text,font=font)
    NewLabel.pack()
    return NewLabel

def ChangeLabelText(Label1,NewText):
        Label1.config(text=NewText)
def ChangeLabelColor(Label1,Color):
        Label1.config(fg = Color)
def GetFilePath():
    path = filedialog.askdirectory()
    if(path == None or path == ""):
        return "False"
    return path
def DosyalarıDuzenle(path):
    if(path == None or path == ""):
        messagebox.showerror("İşlem başarısız","Geçerli bir dosya dizini alınamadı ve işlem")
        return
    FB.ChangePath(path)
    FB.Setup()
    FB.GetFiles()
    FB.CreateFiles()
    FB.FileTransfer()
def Start():
    path = GetFilePath()
    if path != "False":
        DosyalarıDuzenle(path)
    else:
        messagebox.showerror("Geçerli bir yol  seçilmedi", "Lütfen geçerli yol seçin")



HeaderLabel = CreateNewLabel("Dosya düzenleyici",("Arial",12))

ActionLabel = CreateNewLabel("İşlem içeriği :",("Arial",12))

ChangeLabelColor(HeaderLabel,"red")
b = Button(Master,text="İşlemi başlat",command=Start)
b.pack()
#a = Label(Master, text="Not Ready", font=("Arial",12),fg="red")
#a.pack()













Master.mainloop()



