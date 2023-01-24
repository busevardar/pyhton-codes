print("""
********************************
Kullanıcı Girişi Programı
********************************
""")
kullanıcı_adı = "busevardar"
parola = "12345"
giris_hakkı = 3

while True:
    kullanıcıadı = input("Kullanıcı adı giriniz:")
    parolaa = input("Parola giriniz:")
    if (kullanıcıadı == kullanıcı_adı and parola != parolaa):
        print("HATALI PAROLA")
        giris_hakkı -= 1
    elif (kullanıcıadı != kullanıcı_adı and parola == parolaa):
        print("Hatalı kullanıcı adı")
        giris_hakkı -= 1
    elif (kullanıcıadı != kullanıcı_adı and parola != parolaa):
        print("Hatalı kullanıcı adı ve parola")
        giris_hakkı -= 1
    else:
        print("SİSTEME BAŞARIYLA GİRİŞ YAPTINIZ.")
    if (giris_hakkı == 0):
        print("GİRİŞ HAKKINIZ KALMADI")
        break
