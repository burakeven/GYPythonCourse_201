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








