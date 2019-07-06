kullanici_adi = input("Lutfen Kullanici Adini Giriniz : ")
sifre = input("Lutfen sifrenizi giriniz : ")

dosya = open("hesap.txt", "a+") #yazilabilir ve okunabilir dosya acip degiskene ata



print(kullanici_adi, file=dosya)  # kullanicidan alinan inputu dosyaya yaz

print(sifre, file=dosya)          # kullanicidan alinan inputu dosyaya yaz

dosya.seek(0)                     # imleci dosya basina getir


while True:

    for kullanici_adi in dosya.readline():      # satir olarak okutma
        print("Bu Kullanici Adi Daha Once Alinmis, Yeni Bir Tane Deneyin ! ")


    else kullanici_adi not in dosya.readline(): 
        print("Tebrikler Kullanici adi ve parolanizi basariyla olusturdunuz ! ")

    

        
    break


dosya.close()
