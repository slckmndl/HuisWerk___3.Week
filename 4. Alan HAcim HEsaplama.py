

pi=float(3.14)

try:    # olusabilecek hatalari ongorup tolere edip print verecegimiz iicin bunu kullandik.
    while True:

        islem=input("""Lutfen Yapmak IStediginiz Islemi Seciniz ! \n
            1. Alan Islemleri\n
            2. Hacim Islemleri\n
            3. Cikis\n
            Islem: """)
        print("\n\n")

        if int(islem)==3:
            print("Cikiliyor..")
            break


        if int(islem)==1:
            secim=input("""Alan Islemleri : \n
            1- Kare \n
            2- Ucgen \n
            3- Dikdortgen\n
            Islem : """)
            print("\n\n")
            
            if int(secim)==3:
                a=int(input("Lutfen Kisa Kenar Uzunlugunu Giriniz/cm {or; 45}  : "))
                b=int(input("Lutfen Uzun Kenar Uzunlugunu Giriniz/cm {or; 126} : "))
                print("Hesaplamak Istediginiz Dikdortgenin Alani : ",int(a*b))
                print("\n\n")
        

        elif int(islem)==2:
            secim=input("""HAcim Islemleri : \n
            1- Kup \n
            2- Kure \n
            3- Koni\n
            Islem : """)
            print("\n\n")

            if int(secim)==2:
                a=int(input("Kurenin YAricapini Giriniz/cm {or; 10} : "))
                print("Hesaplamak Istediginiz kure nin Hacmi : ",float((4*pi*a**3)/3))
                print("\n\n")


            elif int(secim)==3:
                a=int(input("Koninin Yuksekligini Giriniz/cm {or; 110} : "))
                b=int(input("Koninin Yaricapini Giriniz/cm {or; 10} : "))
                print("Hesaplamak Istediginiz koni nin Hacmi : ",float((pi*b*b*a)/3))

except (ValueError,ZeroDevisionError) as HATA:  #sayi girecegi yere harf girer yada bir sayiyi 0 a bolmeye calisirsa diye..
    print("Lutfen Talimatlara Uygun HAreket Ediniz")


else:
    pass






        
        

        
