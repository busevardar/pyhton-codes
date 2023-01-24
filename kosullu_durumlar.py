şekil = input("Tipini bulmak istediğiniz şekli girin:")
if şekil == "dörtgen":
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    if a==b and b==c and c==d:
        print("Kare.")
    elif (a==c and b==d):
        print("Dikdörtgen.")
    else:
        print("Sıradan dörtgen.")
elif şekil == "üçgen":
    e = int(input("e:"))
    f = int(input("f:"))
    g = int(input("g:"))
    if abs(f - g) < e and e < (f + g):
        print("Bir üçgen belirtiyor.")
        if e==f and f==g:
            print("Eşkenar üçgen.")
        elif (e==f and e!=g) or (e==g and e!=f) or (g==f and e!=f):
            print("İkizkenar üçgen.")
        elif e!=f and f!=g:
            print("Çeşitkenar üçgen.")
    else:
        print("Üçgen belirtmiyor.")
else:
    print("Geçersiz şekil!")
    
    ///////////////////////////////////////////////////////////
    
    vize1 = int(input("vize1 notu:"))
vize2 = int(input("vize2 notu:"))
final = int(input("final notu:"))
toplam_not = (vize1 * 30) / 100 + (vize2 * 30) / 100 + (final * 40) / 100

if toplam_not >=  90:
    print("AA")
elif toplam_not >=  85:
    print("BA")
elif toplam_not >=  80:
    print("BB")
elif toplam_not >=  75:
    print("CB")
elif toplam_not >=  70:
    print("CC")
elif toplam_not >=  65:
    print("DC")
elif toplam_not >=  60:
    print("DD")
elif toplam_not >=  55:
    print("FD")
else:
    print("FF")

    
    //////////////////////////////////////
    
    print("""*************
Hesap Makinesi Programı

İşlemler:

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma

4. Bölme
*************
""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

işlem = input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} in toplamı {}'dir.".format(a, b, a + b))
elif işlem == "2":
    print("{} ile {} in farkı {}'dir.".format(a, b, a - b))
elif işlem == "3":
    print("{} ile {} in çarpımı {}'dir.".format(a, b, a * b))
elif işlem == "4":
    print("{} ile {} in bölümü {}'dir.".format(a, b, a / b))
else:
    print("Geçersiz işlem!")

    /////////////////////////////////
    
    print("""
*********************
Vücut Kitle İndeksi Hesaplama
*********************
""")
boy = float(input("Boyunuzu giriniz:"))
kilo = int(input("Kilonuzu giriniz:"))
print("Bilgileriniz Yükleniyor...")


vücut_kitle_indeksi = kilo / (boy ** 2)
print("Vücut kitle indeksi:",vücut_kitle_indeksi)
if vücut_kitle_indeksi < 18.5:
    print("Zayıf.")
elif ( vücut_kitle_indeksi >= 18.5 and vücut_kitle_indeksi < 25):
    print("Normal.")
elif (vücut_kitle_indeksi >= 25 and vücut_kitle_indeksi < 30):
    print("Fazla Kilolu.")
else:
    print("Obez.")
    
