import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["trt"],kanal="trt"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal


    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten açık.")

        else:
            print("Televizyon açılıyor...")
            self.tv_durum="Açık"


    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("Televizyon zaten kapalı.")

        else:
            print("Televizyon kapanıyor...")
            self.tv_durum="Kapalı"

    def ses_ayarları(self):
        print("ses=", self.tv_ses)
        while True:

            cevap= input("Sesi açmak için '>' tuşuna basın.\n Sesi kısmak için '<' tuşuna basın.\n Çıkmak için 'exit' tuşuna basın.")

            if(cevap == "<"):
                if( self.tv_ses != 0):
                    self.tv_ses-=1
                    print("ses=",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
                    print("ses=", self.tv_ses)
            else:
               print("Ses güncellendi,çıkış yapılıyor...")
               break


    def kanal_ekleme(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")


    def rastgele_kanal(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]

        print("Şu anki kanal:",self.kanal)


    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "TV durumu: {}\nTV ses:{}\nKanal listesi:{}\nŞu anki kanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()

print("""
Televizyon Uygulaması
1. Tv aç
2. Tv kapat
3. Ses ayarları
4. Kanal ekle
5. Kanal sayısını öğrenme
6. Rastgele kanala geçme
7. Televizyon bilgileri
 
 Çıkmak için 'q'ya basın.

""")
while True:
    işlem=input("işlemi seçiniz:")

    if(işlem=="q"):
        print("program sonlandırılıyor...")
        break

    elif(işlem=="1"):
        kumanda.tv_ac()

    elif(işlem=="2"):
        kumanda.tv_kapat()

    elif(işlem=="3"):
        kumanda.ses_ayarları()

    elif(işlem=="4"):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak girin.")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekleme(eklenecekler)

    elif(işlem=="5"):
        print("kanal sayısı=",len(kumanda))

    elif(işlem=="6"):
        kumanda.rastgele_kanal()

    elif(işlem=="7"):
        print(kumanda)

    else:
        print("Geçersiz işlem")

