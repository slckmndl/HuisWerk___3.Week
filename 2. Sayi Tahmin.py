
print(30*"\u2605", "\n",
    15*" ","SAYI TAHMIN OYUNU","\n",
    17*" ","Version : 1.0","\n",
      30*"\u2605","\n\n", sep="")   # Tabelamiz =))


number = 81# makinenin tuttugu sayi



trials=0        # kac kere denedigini ogrenmek icin dongu anahtari

anahtar=1       # while icin anahtar




while anahtar==1:

    trials+=1       #her seferinde deneme sayisini bir artiriyoruz ki asagida kullanabilelim

    guess = int(input("1-100 arasinda bir tamsayi giriniz : "))

    if guess==81:
        print("Tebrikler ! Dogru Tahmin Ettiniz..Sayi : ",number," dir.", trials, " denemede buldunuz..")

        anahtar==2      # sayi bilindiginde kac kerede bildigini gosterip islemi bitir

        break

    elif guess>0 and guess<=60:
        print("Girdiginiz sayi cok kucuk ! Lutfen Daha yuksek bir sayi girerek tekrar deneyiniz ")

    elif guess>60 and guess<=80:
        print("Cok Yaklastin Biraz Daha Cikmalisin !  ")

    elif guess>90 and guess<=100:
        print("Fazla Yukari Ciktin Bira Asagi In")

    elif guess>81 and guess<= 90:
        print("Cok Yaklastin Biraz Daha Inmelisin ! ")


# yukaridaki kodlar tahmin sonrasi bilinemediginde verilecek yazilar

    else:
        print("Lutfen Talimatlara Uygun Hareket Ediniz : ")

    

