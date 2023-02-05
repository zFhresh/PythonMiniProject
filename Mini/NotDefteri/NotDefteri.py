from datetime import date
def Yaz(text,dosyaAdı,mod):
    with open("Mini/NotDefteri/"+dosyaAdı+".txt",mod) as File:
        if mod == "w" or mod == "a":
            File.write(f"{text} \n")

DosyaAdı = input("Dosya adını gir ve metin yazmaya başla:")
while True:
    today = date.today()
    text = input()
    Yaz(f"[{today}]" + text,DosyaAdı,"w")
# def Oku(dosyaAdı):
#     with open("Mini/NotDefteri/"+dosyaAdı+".txt","r") as File:
#             for x in File:
#                 if x == "ben katilim":
#                     print("Suçlu birisi")

