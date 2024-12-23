import random

kelime_listesi = ["Türkiye","İzmir","İstanbul","programlama","bilgisayar","bilişim","okul","deniz"]
secili_kelime = random.choice(kelime_listesi) #rastgele bir kelime seçiliyor
tahmin_sayisi = 5
harfler = [] #kullanicinin girdiği harfleri saklayacağımız liste
x = len(secili_kelime)
z = list('_' * x)
print(' ',join(z) end='\n')
while tahmin_sayisi > 0:
    harf = input("Bir harf giriniz: ")
    if harf in harfler:
        print("Lütfen daha önce tahmin ettiğiniz harfleri tekrar girmeyiniz!")
        continue
    
    elif len(harf) > 1:
        print("Sadece bir harf girilebilir.")
        continue

    elif harf not in secili_kelime: #girilen harf kelime icinde yoksa
        tahmin_sayisi -= 1
        print("Bu harf kelimede yok! {} tane tahmin hakkınız kaldı.".format(tahmin_sayisi))

    else:
        for i in range(len(secili_kelime)):
            if harf == secili_kelime[i]:
                print("Doğru tahmin")
                z[i] = harf
                harfler.append(harf)
        print(' '.join(z), end = '\n')

    cevap = input("Kelimenin tamamını tahmin etmek istiyor musunuz? ['e' veya 'h']: ")

    if cevap == "e":
        tahmin = input("Kelimenin tamamını tahmin edebilirsiniz: ")
        if tahmin == secili_kelime:
            print("Tebrikler bildiniz!")
            break
        else:
            tahmin_sayisi -= 1
            print("Yanlış tahmin ettiniz. {} tane tahmin hakkınız kaldı.".format(tahmin_sayisi))

        if tahmin_sayisi == 0:
            print("Tahmin hakkınız kalmadı. Kaybettiniz! Adam asıldı.")
            break