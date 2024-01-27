
"""
Adı Soyadı:Oğuzhan Çilkurt
Öğrenci No: 210706041
Puan:


                          T.C. GİRESUN ÜNİVERSİTESİ
                            Mühendislik Fakültesi
                        Bilgisayar Mühendisliği Bölümü 
                        BILM-101 Bilgisayar Programlama 1
                             Güz 2021-2022 Ödev 2
                           Dr. Öğr. Üyesi Murat Moran
"""
# In[]:
"""                         AÇIKLAMALAR 
 
Bu ödevde 3 problem ve şıkları vardır, bunlar aşağıdadır. Ödevdeki problemlerin 
çözümü için bu dosyayı kendi isminiz ve öğrenci numaranızla isimlendirerek
kayıt edin (“Adı_Soyadı_ÖğrenciNo” şeklinde). Cevaplar'dan sonraki bölüme
ilgili sorunun cevabını yazın. Sorular 1 ve 2 için yorumun içine, 3. soru için
yorumlanmamış yürütülebilir olacak.

Bu ödeve ekleyeceğiniz kodlar yürütüldüğünde çalışıyor olmalı. Bu nedenle daha 
önceden test edilmeli. Kod satırlarında uygun görülen yerlere kod satırının 
işlevi ile ilgili yorumlarınızı yazınız (# ile). Olabildiğince yazdığınız 
kodların açıklamasını yapınız. Son hali ile hata veren kodlardan puan düşecektir. 

Tamamladığınızda cevapların olduğu sadece bu Python dosyasını (.py) sisteme 
yükleyin. Sistem, SADECE Python (.py) dosyalarını kabul edecektir. 

Ödev yükleme 21.12.2021 günü saat sabah 09:00'a kadar mümkündür. Bu gün ve saatin 
sonrasında sistem ödev yüklemeye izin vermeyecektir. Başka yollardan (e-mail vs.) 
gönderilen ödevler değerlendirilmeyecektir.

Problem çözümlerini kendi çabalarınızla yapmanızı rica ederim. Kopya çekildiği 
tespit edilmesi durumunda bu kişilerin sınavları geçersiz sayılacak ve idari 
işlem başlatılacaktır.

Başarılar.

"""
# In[1]:
                             ## PROBLEMLER 

# ========================
# Problem 1: Test etme ve istisnalar/Exceptions  (15 Puan)
# ========================
# Aşağıdaki fonksiyon spesifikasyonunu göz önünde bulundurarak en az 5 adet 
# test durumu / test case yazın. Her bir test durumu için; fonksiyonun girdisi, 
# fonksiyonun beklenen çıktısı ve bu testin neden önemli olduğunu açıklayınız.
# Aşağıdaki 1. test durumu örnek olarak verilmiştir. Sonraki 5 satırı doldurunuz.

def buyuk_kucuk_harf(s):
    """Bu fonksiyon s string'inin bir kopyasını, büyük harfleri küçük ve küçük 
    harfleri büyük yaparak alır. Harf olmayan karakterler (sayılar vs.) bundan 
    etkilenmez.
    Koşul: s bir string'dir.
    """

"""Cevaplar 1:
   -------- 

    Girdi          Cıktı                   Nedeni
    -----          -----                   ------
1.   ''             ''           Boş liste her zaman önemlidir.

2.  '19:03'        '19:03'       Harf dışında bir değer(sayı,nokta,ünlem...) girince
                                  ne olur diye kontrol ettik ve etki etmiyormuş
 
3.  'AsuS'         'aSUs'        Aynı kelime içinde ki  harften Büyük ==> Küçük , Küçük ==> Büyük yaptımı diye baktık

4.  'PES'          'pes'         Büyük harfleri küçük harf yapıyormu  

5.'oĞuzÇlkrt'  'OğUZçLKRT'       Türkçe karakterleri etkiliyormu


6.  'fifa'         'FİFA'        Küçük harfleri büyük harf yapıyormu
"""
# In[2]:
# ========================
# Problem 2: Nesneler ve Terminoloji  (15 Puan)
# ========================
# Aşağıdaki A ve B sınıflarının tanımını kullanarak, devamındaki soruları boş 
# bırakılan yere satır numarasını yazarak cevaplandırın. Bir kaç muhtemel doğru 
# cevap olabilir, SADECE 1 tanesini yazın.

#1. class A():
#2.     x = 1
#3.     def __init__(self, n):
#4.         self.y = n
#5.         A.x += 1
#6.     def p(self):
#7.         print(self.y)
#8.         self.y += 3
#9.         self.r()
#10.     def r(self):
#11.         self.y += 2
#12.         print(self.y)
#13. class B(A):
#14.     x = 10
#15.     def __init__(self, n):
#16.         super().__init__(n)
#17.         sum = self.y + B.x
#18.         self.m = sum
#19.     def r(self):
#20.         self.y += self.x
#21.         print(self.m)
#22. a = A(1)
#23. b = B(2)
#24. a.p()
#25. b.p()

"""Cevaplar 2:
   -------- 

a. Satır 4 de/da bir nesne niteliği yaratılır 

b. Satır 14 de/da bir sınıf niteliği yaratılır 

c. Satır 13 de/da bir üst sınıf tanımı başlar 

d. Satır 19 de/da bir örnek metodu başlar

  
e. Satır 16 de/da bir metot tanımı üstü yazılmaya/override başlanır

"""
# In[3]:
# ========================
# Problem 3: Bir başka sayı tahmini oyunu  (70 Puan)
# ========================
"""  Bu sayı oyununda, öncelikle;
- Bilgisayara 10 rakamdan önce rastgele 6 rakam seçtirip, daha sonra bu 6 rakamı  
- kullanarak rastgele 4 rakam seçtireceksiniz.
- Bilgisayar, bu 4 rakamı seçerken, aynı sayıyı EN FAZLA 2 kere kullanılabilir.
- Daha sonra, oyuncu olarak siz, bu rakamları ve sırasını 13 tahminde bulmaya çalışacaksınız.
- Tahmin ettiğiniz rakamlar 6 rakamlı listeden olmalı.
- Bir tahmin sonunda, Bilgisayar, tuttuğu gizli rakamlara ve yerlerine göre: 
- Hem doğru rakam, hem de doğru yer için 'D' sayacı ile,
- Doğru rakam ancak yanlış yer/basamak için 'Y' sayacı ile oyuncuya bilgi versin.
- Yanlış cevaplar için (tutulan rakamlarda yoksa) hiç bir geri bildirime gerek yok.
- Oyuncu, Bilgisayarın verdiği bu bilgiler ışığında yeni tahminler de bulunur.
- Ta ki o rakamları ve yerlerini doğru tahmin edene kadar. Yani D:4, Y:0 olana kadar.

- Kodlarınıza olabildiğince açıklama yazın!
- Try/except, raise veya assert kullanın.


Örnek Oyun:
Seçilen 6 rakam : [0, 2, 3, 1, 7, 8] <- Seçilen 6 rakam ekrana yazılsın. Tahminler bunun içindeki rakamlardan oluşacak.
Tutulan 4 rakam : [2, 7, 7, 0] <- Tutulan 4 rakam sadece göstermek amaçlı (oynarken gizlenmeli)

Tahmin 1 < 3270 <- Bu tahminde, 3 gizli sayıda yok, 2 var ama yeri yanlış (Y:1), 7 ve 0 var ve yerleri doğru (D:2)
D : 2 Y : 1

Tahmin 2 < 1234 <- 2. Tahminde listede olmayan bir sayı kullanılmış (4).
Hata! Rakamları sadece [0, 2, 3, 1, 7, 8] listesinden seçiniz!

Tahmin 2 < 12370 <- 2. Tahmin tekrarlandı ancak beş karakterle.
Hata! Sadece 4 karaktere izin verilir!

Tahmin 2 < 2770 <- Doğru tahmin (rakamlar ve yerleri doğru)
D : 4 Y : 0
Kazandınız!


	Cevap 3:
   -------- 
""" 
print(" ")
print("0-10 arasından rastgele seçilen 6 rakam ile bulunmak istenen 4 haneli sayıyı bulmaya çalış.")





import random 
# random kütüphanesini kullandık burda

l =["0","1","2","3","4","5","6","7","8","9"]
# print(l)
# Listemiz bu


print("\n10 sayıdan rastgele 6 sayı alalım")

altisayi=random.sample(l,6)
# sample bize l listesindeki 6 tane rastgele sayı verir |sample(liste,kaç tane alınmalı)|
print(altisayi)

print("\nBu 6 sayı içinden oyuncuya sorulacak 4 rakam seçilecek")
dörtsayi=random.sample(altisayi*2,4)
# b bizim gizli 4 rakamımız olacak

print("\nBu 4 sayıyı bulmak için 13 hakkınız var iyi düşünün :)")

print(['_ _ _ _'])

print("\nMümkünse listden olan sayıları girin kendi kolaylığınız için :}")

print("\nLütfen sadece 4 basamak girin ")

tahmin=0
D=0
Y=0
x=0
# Bu değerlerin başlangıc değerleri
# x benim tahmin sayacım 1. 2. 3. yazmak için kullandım  
print("-------------------------------------------------------------------------")


# print(dörtsayi)
# CEVAP

while tahmin<=13:
    if tahmin==13:
        print("Tüm Haklarını Kullandın Maalesef Kaybettin :(")
        break
    # Tahmin 13 olunca döngü biter
    x=x+1
    tahmin=tahmin+1

    # Tahmin 1 artmalı ki dögüden en sonunda çıkabilelim
    
    print(altisayi,"Liste Burada")
    # Bunu buraya ekleme sebebim oyuncuya kolaylık olsun
    
    oyuncugirdi=input("Tahmininizi girin")
    # Girdimizi alıyoruz
    
    
    try:
        int(oyuncugirdi)!=str
    except ValueError:
        print("Lütfen Sayı Girin")
        continue
    # Sayı girene kadar bunu tekrarlayacak
    
    
    
    if len(oyuncugirdi)>4:
        print("4 Basamaktan fazla girdiniz lütfen uyarılara uyun!!!")
        continue
   # 4 basamaktan fazla girmemesi için bu kodu kullandım
   
    if len(oyuncugirdi)<4:
        print("4 Basamaktan az girdiniz lütfen uyarılara uyun!!!")
        continue
    # 4 basamaktan az girmemesi için bu kodu kullandım
    
    
    print(x,".Hakkını Kullandın")
    
    if tahmin==12:
        print("\nSon Hakkın Dikkat Et!!!")

    
   
    for i in oyuncugirdi:
        #Bu döngüde girilen input ile b nin indexlerini karşılaştırıp doğru,yanlış yazdırdık

           
        if oyuncugirdi[0]==dörtsayi[0]:
        #Eğer girilen sayının 0. indexi ile b nin 0. indexi aynı ise D 1 artar 
            
                D=D+1
        if oyuncugirdi[0]!=dörtsayi[0] and (oyuncugirdi[0] in dörtsayi): 
        #Eğer 4 rakam içinde var ama yeri yanlışsa Y 1 artar 
            Y=Y+1 
        
        if oyuncugirdi[1]==dörtsayi[1]:
            
                D=D+1
        if oyuncugirdi[1]!=dörtsayi[1] and (oyuncugirdi[1] in dörtsayi):   
            
            Y=Y+1
        
                
        if oyuncugirdi[2]==dörtsayi[2]:
            
           D=D+1
           
        if oyuncugirdi[2]!=dörtsayi[2] and (oyuncugirdi[2]  in dörtsayi):
            
            Y=Y+1    
        
         
        if oyuncugirdi[3]==dörtsayi[3]:
    
            D=D+1
            
        if oyuncugirdi[3]!=dörtsayi[3] and (oyuncugirdi[3] in dörtsayi):
            
            Y=Y+1    
        
        # Eğer doğru ise D 1 artacak yanlış ise Y 1 artacak 
         
    D=D//4
    
    Y=Y//4
    # 4 e bölmemin sebebi 1 doğruyu/yanlışı 4 tane sayıyordu bu şekilde çözdüm o sorunu
    # Örneğin D:16 Y:0 gibi çıkıyordu
    
    if Y==5 and Y+D==5:
        
        Y=Y-1
    #Bu kodu yazmadığım zaman Y ilk yanlıştan sonra 5 tekrar edip duruyor du bu şekilde çözdüm sorunu
    # Birde toplamları bazen 5 çıkıyordu diye bu kodu ekledmiş bulundum
  
         
   
    
    
    print("D:",D)
    
    print("Y:",Y)
    
    # Doğru,Yanlış değerlerimiz bunlar burada çıktı alıyoruz yani
    
   

        
    if D==4 and Y==0:
        
            print("Tebrikler Doğru Cevap ^_^")
            
            break         
        
     #Eğer Doğru sayısı 4,Yanlış sayısı 0 olursa oyun biter
    

     
    
    


   
