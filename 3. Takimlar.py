file = open("Futbolcular.txt", "r")

Gs = open("Galatasaray.txt", "a")   #actigimiz dosyalari isimlendirip yazilabilir sekilde degiskene atiyoruz!
Bjk = open("Besiktas.txt", "a")
Fb = open("Fenerbahce.txt", "a")

for line in file:
   if 'Galatasaray' in line:
       Gs.write(line)

   if'Fenerbahce' in line:
       Fb.write(line)

   if "Besiktas" in line:
       Bjk.write(line)



Gs.close()
Fb.close()
Bjk.close()
