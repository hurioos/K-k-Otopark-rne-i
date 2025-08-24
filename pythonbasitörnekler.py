print("Merhaba Dünya:")

isim = input("Merhaba, İsminiz Nedir?")
print("Merhaba",isim)

sayi = int(input("Bir Sayı Giriniz: "))

if sayi % 2 == 0:
    print("Girdiğiniz Sayı Çifttir.")
else:
    print("Girdiğiniz Sayı Tektir.")

sayi = int(input("Bir Sayı Giriniz:"))
if sayi > 0:
    print("Giridğiniz Sayı Pozitiftir:")
elif sayi < 0:
    print("Giridğiniz Sayı Negatiftir:")
else:
    print("Giridğiniz Sayı Nötrdür:")

    for i in range(1 , 11):
        print(i)

sayilar = [1,2,3,4,5]
toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
print("Sayilarin Toplamı:", toplam)
print("Sayilarin Ortalaması:", ortalama)

sayi = int(input("Bir Sayı Giriniz:"))
faktoriyel = 1
for i in range(1 , sayi + 1):
    faktoriyel *= i
    print("Girdiğiniz Sayının Faktoriyeli:", faktoriyel)

import random
sayi = random.randint(1, 100)

tahmin = int(input("1 İle 100 Arasında Bir Sayı Tahmin Ediniz:"))
if tahmin == sayi:
    print("Tebrikler Doğru Tahmin Ettiniz:")
elif tahmin < sayi:
    print("Daha Yüksek Bir Sayı Deneyiniz:")
else:
    print("Daha Düşük Bir Sayı Deneyiniz:")


görevler = []

while True:
    görev = input("Yeni Bir  Görev Ekleyin (Çıkmak İçin 'q' Tuşuna Basın):")
    if görev.lower() == 'q':
        break
    görevler.append(görev)
    print("Görev Eklendi:",görevler)


    sayi1 = float(input("Birinci Sayıyı Giriniz:"))
    sayi2 = float(input("İkinci Sayıyı Giriniz:"))

    işlem = input("Yapmak İstediğiniz İşlemi Seçiniz (+, -, *, /):")

    if işlem == '+':
        sonuç = sayi1 + sayi2
    elif işlem == '-':
        sonuç = sayi1 - sayi2
    elif işlem == '*':
        sonuç = sayi1 * sayi2
    elif işlem == '/':
        if sayi2 != 0:
            sonuç = sayi1 / sayi2
        else:
           print("Hata: Bir Sayı Sıfıra Bölünemez.")



           i = 1
           while i <= 5:
               print(i)
               i+=1


               i = 5
               while i > 0:
                    print(i)
                    i+=1

                    sifre = ""
                    while sifre != "1234":
                       sifre = input("Şifre Giriniz:")
                       print("Giriş Başarılı")

                       i = 0
                       while i < 20:
                           print(i)
                           i += 2


                           secim = ""

                           while secim != "q":
                               print("1.Toplama")
                               print("2.Çıkarma")
                               print("3.Çarpma")
                               print("4.Bölme")
                               print("5.'q' Çıkış ")
                               secim = input("Yapacağınız İşlemi Seçiniz:")
                               print("İşlem Sonlandırıldı:")

                               i = 100
                               while i > 0:
                                   print(i)
                                   i+=1



