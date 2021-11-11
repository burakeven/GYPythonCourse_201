#VERI YAPILARI

#--LISTELER -- Degistirilebilir, kapsayici, sirali
#Yol1; [] ile liste oluşturulabilir.
#Yol2;list() 

notlar=[90,70,80]
type(notlar)

liste =["a",19.3,"b"]
type(liste)


liste_genis=[liste1,"c",22]
len(liste_genis)

type(liste_genis[1])

tum_liste=[liste, liste_genis]
#del tum_liste #listeyi siler

#LISTELER - ELEMAN ISLEMLERI

yeniliste=[10,20,30,40]
yeniliste[1]

yeniliste[0:3]
yeniliste[:2]

liste_yeni=["a",1,[1,2,3]]
liste_yeni[2]

liste_yeni[2][2] #burada listenin ikinci indeksinin içerisindeki ikinci indexi aldım.

liste_yeni.insert(3,"a") #Yeni indeks 3'e a degerini atadim.

#Liste - Eleman degisimi

lisyeni=["Burak","veli","ahmet","ayşe"]
lisyeni[1]="velinin babası"

lisyeni[0:4]="burak_baba","veli_baba","ahmet baba","ayse baba"


del lisyeni[4]
lisyeni

#LISTE - LISTE METHODLARI
dir(list) #list methodlarına ulasmak icin
hoplis=["burak","veli","isik"]

#append && remove  - listeye kalici yeni deger atadi, remove ise sildi.
hoplis.append("can")
hoplis.remove("can")

hoplis.insert(0, "burrrrrak")
hoplis.insert(2, "mehmet")
hoplis.insert(5, "tugce")

hoplis.insert(len(hoplis),"beren") #len ile kac deger oldugunu saydirip isi hizlandirdim.

#pop - eleman silmek icin kullanilir.
hoplis.pop(0)

#count
hoplis.count("burak") #liste icerisinde belirli elemanin kac tane oldugunu gosterir.

#copy
yedek_liste=hoplis.copy()

#extend - birlestirme islemi yapar
hoplis.extend(["a","b",10])

#index() -kacinci indexte oldugunu soyler.
hoplis.index("burak")

#reverse() -liste elemanlarini terse cevirir.
hoplis.reverse()

#sort() - kucukten buyuge siralar
liliste=[10,20,30,50,12,32]
liliste.sort()

#clear - liste icini ucurur.
liliste.clear()

#VERI YAPILARINDAN 'TUPLE' - Listeden farki degisitirilemez olmasidir.
t=("ali","veli",1,2,3.2,[1,2,3,4])
y="ali","veli",1,2,3.2,[1,2,3,4]

t=("eleman",)
type(t)

b=("ali","veli",1,2,3.2,[1,2,3,4])
b[1]

#VERI YAPILARI - Dictionary(Sozluk)
sozluk= {"REG": "Regresyon Modeli",
         "LOJ":"Lojistik Regresyon",
         "CART": "Classification and Reg"
         }

sozluk
len(sozluk)

sozluk= {"REG": ["Regresyon Modeli",10],
         "LOJ":"Lojistik Regresyon",
         "CART": "Classification and Reg"
         }
#soldaki key, sag value.

sozluk["REG"]

sozluk= {"REG": {"RMSE":10,"MSE":20, "SSE":30},
         "LOJ":"Lojistik Regresyon",
         "CART": "Classification and Reg"
         }
sozluk["REG"]["SSE"]


#Dictionary eleman ekleme ve degistirme
sozluk= {"REG": "Regresyon Modeli",
         "LOJ":"Lojistik Regresyon",
         "CART": "Classification and Reg"
         }

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk


sozluk["REG"]="Coklu Dogrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Aglari"
sozluk

l = [1]

sozluk[l] = "Yeni bir sey"
#dictionarylerde key degerleri sabit veri yapilariyla olusturulabilir, ornegin string ve int gibi.

t = ("Tuple")
sozluk[t]="Yeni bir sey"
sozluk

#VERI YAPILARI - Sets
#Bunlar sirasizdir, degerleri essizdir, degistirilebilirler ve farkli tipleri barindirabilirler.
s = set()
s

l = [1,"a","ali",123]
s = set(l)
s

t = ("a","ali")
s = set(t)
s


ali = "selam_dunyali"
type(ali)

s = set(ali)
s
len(s)

l[0] #0.Indeks olan 1'i ekrana yazdirir.
s[0] #Sets indeks desteklemedigi icin hatayla karsilasilir.

#SETS - Eleman ekleme ve cikarma
l = ["gelecegi","yazanlar"]
s=set(l)
s

dir(s)
s.add("ile")
s

s.add("gelecege_git")
s

s.remove("ile")
s.pop()

s.discard("ali") #hata verdirmeden eleman silme methodudur.
#Ali'i basta sildik diyelim ve baska ali yok, remove kullanırsak hata gösterir.
#Fakat discard dersek hata aldırmadan yoluna devam eder kod akisini bozmaz.

#SETS - Klasik kume islemleri

# =============================================================================
# difference() ile iki kumenin farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symmetric_difference() ikisinde de olmayanlari.
# =============================================================================


#difference()
set1= set([1,3,5])
set2= set([1,2,5])

set1.difference(set2) #set1'de olup 2'de olmayanlari gosterir.
set2.difference(set1)

set1.symmetric_difference(set2) #2 ve 3'u gosterir cunku 1'de 2 yok 2'de 3 yok.
set1-set2
set2-set1

kesisim= set1.intersection(set2)
set2.intersection(set1)
set1 & set2

birlesim = set1.union(set2)

set1.intersection_update(set2) #set2'de var olan degerlere gore gunceller.
#Ornegin set1'de ham olarak 1,3,5 yazmistik update cekerek set2'de yer alan
#ortak degerlerden 1 ve 5'i korur fakat set1'dek 3'u silerek seti gunceller.

#Sets Sorgu Islemleri
set4=set([7,8,9])
set5=set([5,6,7,8,9,10])

#Ikı kumenin kesisiminin bos olup olmadiginin sorgulanmasi
set4.isdisjoint(set5) #Ikı kume kesisimi bos mu? Bos olmadigi icin false doner.

#bir kumenin butun elemanlarinin baska bir kume icerisinde yer alip almadigi
set1.issubset(set2) #set1 set2'nin alt kumesi midir? True doner.

#bir kume diger kumeyi kapsayip kapsar mi?
set2.issuperset(set1) #Set2 set1'i kapsar bu yuzden true doner.


set1 = set([5,7,9])
set2 = set([5,6,7])
set1.difference(set2)





