sayi=input("Lutfen Asal Sayi olup Olmadigini Ogrenmek IStediginiz Sayiyi Giriniz : ")
sayi=int(sayi)  # aldigimiz inputu tamsayiya cevirdik


key=0

while key==0:

    for bolen in range(2,int(sayi)):    #2 ile girilen sayi arasindaki sayilara kadar bakip..
        if int(sayi)%bolen==0:          # bu sayi kendisine kadar olan sayilardan birine bolumunden kalan 0 ise
            key+=1
            break
    if key!=0:
        print("Girmis oldugunuz ",sayi,"sayisi bir ASAL sayi DEGILDIR..! ")
            
    else:
        print("Girmis oldugunuz ",sayi,"sayisi bir ASAL sayidir..! ")
        key=1
    break
