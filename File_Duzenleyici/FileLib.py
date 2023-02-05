import os
import shutil
List = {
  
}
def Setup():
    GetAllExtencions()
def ChangePath(path):
    os.chdir(path)
def GetAllExtencions():
    for x in os.listdir(os.getcwd()):
        try:
            extencion = x.split(".")[1]
            if not extencion in List:
                List[extencion] = []
        except IndexError:
            print("Uzantısı olmayan bir dosya bulundu ve es geçildi")
    print("Bütün uzantılar başarıyla alındı. \n")

def GetFiles():
    for x in os.listdir(os.getcwd()):
        for y in List:
            if x.endswith("." + y):
                List[y].append(x)
def CreateFiles():
    for x in List:
        newPath = os.getcwd() + "\\" + x
        if not os.path.exists(newPath):
            print("Dosya oluştu")
            os.makedirs(newPath)
        else:
            print("Dosya zaten mevcut")
def FileTransfer():
    for x in List:
        print(x)
        for y in List[x]:
            print(y)
            shutil.move(y,x)