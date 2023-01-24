print("""
*************************
ATM MAKİNESİNE HOŞGELDİNİZ.
İşlemler:
1. Bakiye sorgulama
2. Para yatırma
3. Para çekme
Programdan çıkmak için q'ya basın
**************************
""")
bakiye = 1000

while True:
    işlem = (input("işlem seçiniz:"))
    if(işlem=="q"):
        print("yine bekleriiz...")


    elif(işlem=="1"):
        print("bakiyeniz {} tldir.".format(bakiye))

    elif(işlem=="2"):
        miktar=int(input("miktarı giriniz:"))
        bakiye+=miktar

    elif (işlem =="3"):
        miktar=(int(input("çekmek istediğiniz miktarı giriniz:")))
        if (miktar>bakiye):
            print("yetersiz bakiye")
            continue
        elif (miktar<=bakiye):
            bakiye-=miktar

    else:
        print("geçersiz işlem")
