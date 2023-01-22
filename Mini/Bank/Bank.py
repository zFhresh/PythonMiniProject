import random
User = {
    "isim":"",
    "Sifre":0,
    "Para":0,
    "IBAN":0
}
def IbanOlustur():
    iban = ""
    iban += "TR"
    for i in range(6):
        iban += str(random.randint(0,9))
    return iban

def UyeOlustur():
    print("--- Kullanıcı oluşturma işlemi ---")
    User["isim"] = input("İsmini gir")
    User["Sifre"] = input("Şifreni gir")
    User["IBAN"] = IbanOlustur()

def GirisYap():
    sifre = input("Şifreni gir")
    return User["Sifre"] == sifre
def paraYatır():
    para = int(input("Yatıracagın parayı yaz:"))
    User["Para"] += para
    print("Tebrikler yatırma işlemin bitti \nMevcut Bakiyen:" + str(User["Para"]))
def ParaCek():
    para = int(input("Çekeceğin miktarı gir:"))
    if User["Para"] - para < 0:
        print("Mevcut bakiyen yetersiz")
        return
    User["Para"] -= para
    print("İşlem başarılı\nMevcut Bakiye:" + str(User["Para"]))

UyeOlustur()

while True:
    if(not GirisYap()):
       continue
    print("Hoşgeldin " + User["isim"])
    while True:
        islem = int(input("İslem:"))
        if islem == 1:
            paraYatır()
        elif islem == 2:
            ParaCek()
        f = open(f"{User['isim']}Bilgileri.txt","w")
        f.write(f"{User['isim']}:{User['Sifre']}:{User['IBAN']}:{User['Para']}")
        f.close()



