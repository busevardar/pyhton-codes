import random
import time

print("""****************************************


SAYI TAHMIN OYUNU
0 ile 400 arasında seçilen rastgele sayıyı bulunuz.

****************************************""")

rastgele_sayı=random.randint(0,400)

tahmin_hakkı=8

while True:
    tahmin = int(input("Tahmininiz:"))
    if(tahmin<rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("{} den daha büyük bir sayı deneyin.".format(tahmin))
        tahmin_hakkı-=1
        print("{} tahmin hakkınız kaldı".format(tahmin_hakkı))
    elif(tahmin>rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("{} den daha küçük bir sayı deneyin.".format(tahmin))
        tahmin_hakkı -= 1
        print("{} tahmin hakkınız kaldı".format(tahmin_hakkı))
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Sayıyı buldunuz. sayı=",rastgele_sayı)
        break
    if(tahmin_hakkı==0):
        print("Sayıyı bulamadınız")
        print("sayınız:",rastgele_sayı)
        break
