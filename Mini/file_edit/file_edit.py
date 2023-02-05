import os
import shutil
# ? Kodun çalıştığı uzantıyı değiştirir
os.chdir("C:\\Users\\dyunu\\Documents\\GitHub\\PythonMiniProject\\Mini\\file_edit\\DemoFolder")
List = {
  
}
def Setup():
    GetAllExtencions()

def GetAllExtencions():
    # ? os.listdir(os.getcwd()) kodun çalıştığı uzantıdaki bütün dosyaları bir liste halinde döndürür
    for x in os.listdir(os.getcwd()):
        try:
            extencion = x.split(".")[1]
            # ? dict in içinde bir değişkenin olup olmadıgını test etmek için 
            if not extencion in List:
                List[extencion] = []
        # ? IndexOutofRange hatası atıldığı zaman IndexError yakalar
        except IndexError:
            print("Uzantısı olmayan bir dosya bulundu ve es geçildi")
    print("Bütün uzantılar başarıyla alındı. \n")

def GetFiles():
    for x in os.listdir(os.getcwd()):
        for y in List:
            # ? Eğer dosyanın sonu listelenen uzantılardan biri ile bitiyorsa bunu dosyayı o uzantının dict keyinin altındaki array a ekle 
            # ? Bu array GetAllExtencions da üretiliyor
            if x.endswith("." + y):
                List[y].append(x)
def CreateFiles():
    for x in List:
        # ? Dosyaların ekleneceği dosyaları oluşturmak için çalışılan alanın içine oluşturulacak şekilde dosya yollunu hazırla
        newPath = os.getcwd() + "\\" + x
        # ? Eğer belirtien uzantaıda dosya mevcut değilse bu dosyayı oluştur aksi takdirde else ile bu dosyanın mevcut olduğunu bildir
        if not os.path.exists(newPath):
            print("Dosya oluştu")
            os.makedirs(newPath)
        else:
            print("Dosya zaten mevcut")
def FileTransfer():
    # ? Listeye kaydedilen bütün uzantıları ("py","txt") döndürür 
    for x in List:
        print(x)
        # ? Döndürülen uzantının içindeki dosya isimlerini döndürür ("py":["deneme1.py"] )
        for y in List[x]:
            print(y)
            # ? y değişkeninde tutulan dosya adını x değişkeninde tutulan uzantı adına sahip dosyanın içine gönderir
            shutil.move(y,x)

#? GetAllExtencion u çalıştırır ve bütün dosyaları tarayacak uzantıları kaydeder (Aynı uzantıları yanlızca 1 defa kaydeder)
Setup()
# ? Bulduğu uzantıya sahip dosyaların adını dict in içine kaydeder {"py":["dosya.py"]}
GetFiles()
# ? Setup'da kaydedilen uzantıların ismine sahip klasörler oluşturur
CreateFiles()
# ? Uzantılı dosyaları uzantı adına sahip klasörlere gönderir
FileTransfer()
print(List)