print("Kitap Kaydetme Programı")
ad = input("Kitabın Adı:")
yazar = input("Yazarın Adı:")
sayfa= int(input("Sayfa Sayısı:"))
bilgiler = [ad,yazar,sayfa]
print("Bilgiler Kaydediliyor...")
print("Kitabın Adı: {} \nYazarın Adı: {} \nSayfa Sayısı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
delta = b ** 2 - 4 * a * c
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)
print("Birinci Kök: {} \nİkinci Kök: {}\n".format(x1,x2))

//////////////////////////////////

a = int(input("dik kenar uzunluğu:"))
b = int(input("diğer dik kenar uzunluğu:"))
c = (a ** 2 + b ** 2) ** 0.5
print("dik kenarlarını {} ve {} olan üçgenin hipotenüs uzunluğu {}'dır.".format(a,b,c))

////////////////////////////////////

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c

x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print("Birinci kök: {} \n İkinci kök: {}\n".format(x1,x2))

//////////////////////////////////

/* sayi değiştirme */
a1 = input("Birinci sayı:")
a2 = input("ikinci sayı:")
print("Değiştirilmeden önceki değerler \n Birinci sayı: {} İkinci sayı: {}".format(a1,a2))
print("lütfen bekleyin...")

a1,a2 = a2,a1
print("işlem tamamlanıyor...")
print(".")
print(".")
print(".")
print("Sonraki değerler \n Birinci sayı: {} İkinci sayı: {}".format(a1,a2))
print("işleminiz başarıyla tamamlandı.")
/////////////////////////////////


