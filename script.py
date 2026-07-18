#
# class Cars:
#     def __init__(self,marka,ranggi,eshiklar_soni):
#         self.marka=marka
#         self.marka=ranggi
#         self.eshiklar_soni=eshiklar_soni
#
#
#
#     def get_aim(self):
#         return"moshina yuradi"
#
#     def get_marka(self):
#         return self.marka
#
#     def set_marka(self,new_marka)
#         self.marka= new_marka
#
#
#
#     def get_ranggi(self):
#         return self.get_ranggi
#
#     def set_ranggi(self, new_rang):
#         self.ranggi= new_rang
#
#
#     car1= Cars(marka='Limuzin', ranggi='qora',eshiklar_soni=4)
#     car2= Cars(marka='Convertible', ranggi='qizil',eshiklar_soni=2)
#     car1.set_marka("Rols-royls")
#     print(car1.get_marka())
#     print(car2.get_marka())
#     print(">>>>>>>>>>>>>>")
#     print(car2.get_ranggi())
#     car2.set_ranggi("yellow")
#
#     print(car2.get_ranggi())


# class Shifokor:
#     def __init__(self,name,age,geder,specialty):
#         self.ismi
#
# 1 float
# 2 boolean
# 3 string
# 4 list
# 5 set
# 6 tuple
# 7 integer
# 8 dictinoiry  - lugatlar bilan ishlaydi

# DICT

# my_dict = {}
# print(my_dict)
# print(type(my_dict))

# from pprint import pprint
# my_list = []
# my_dict = {'name': "Ali" ,
#            "age" : 19,
#            "city" : "Termiz"}
# my_list.append(my_dict)
# print(my_list)
# pprint(my_list)

# my_dict = {"name": "Ali" ,
#            "age" : 19,
#            "city" : "Termiz",
#            'is_active': True,
#            'rating': 4.9}

# print(my_dict["age"] , "\n",my_dict['rating'])
# my_dict['age'] = 21
# print(my_dict)

# my_dict.update({'is_active': True,'rating': 4.9})
# print(my_dict)

# del my_dict['city']
# print(my_dict)

# ochgan = my_dict.pop("name")
# print(my_dict)
# print(ochgan)

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# my_dict=[]
# print(my_dict)

# my_dict = {"name": "ali" ,
#            "age" : 19,
#            "city" : "Termiz",
#            'is_active': True,
#            'rating': 4.9}
# my_dict["name"]='jahongir'
# # print(my_dict)
# my_dict = {"name": "Ali" ,
#            "age" : 19,
#            "city" : "Termiz",
#            'is_active': True,
#            'rating': 4.9}
# print(my_dict.values())
# my_dict = {"name": "Ali" ,
#            "age" : 19,
#            "city" : "Termiz",
#            'is_active': True,
#            'rating': 4.9}
# print(my_dict)
# for i in range(100):
#      print(i)

# def uchburchak():
#     for i in range(1, 5 + 1):
#         print("*" * i)
# uchburchak()
# class Uchburchak:
#     def __init__(self, i):
#         self.i = i
#     def uchburchak(self):
#         for x in range(1, self.i + 1):
#             print("1" * x)
#
# u = Uchburchak(8)
# u.uchburchak()
# def a ():
#     print('salom')

# class cars:
#     def __init__(self,model,rangi):
#      self.rangi=model
#      self.rangi=rangi
#
#  def name (self):
#          return self.model
# car=cars("mers""rangi")
# print(car)
#
# class son:
#     def __init__(self,i):
#         self.i=i
#
# def chiqariw(self):
#     for a in range(self.i):
#         print(a**2)

# def son(a):
#     print(a)
# son(5)
# def son(a,b):
#     print(a+b)
# son(7,8)

# a = 55
# b = 7
#
# if a>b:
#     print(a)
# else:
#     print(b)


# def taqqoslash(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
#
# taqqoslash(84,8)

# def taqqoslash(a,b):
#     if a>b:
#       print(a)
#     else:
#       print(b)
#
# taqqoslash(57,67)
#


# for i in range(200):
#     print(i)

# for i in range(100):
#     if i % 3==0 and i%5==0:
#         print(i)

# def salom(n):
#     for i in range(n):
#         if i % 3 == 0 and i % 5 == 0:
#             print(i,end=" ")
#
#
# salom(100)
#
# def olma(n):
#     for i in range(n):
#         if i % 3 == 0 and i % 5 == 0:
#             print(i,end=" ")
# olma(150)


# def taqqoslash (a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# taqqoslash(100,99)
#
# ismlar=[ ]
# n=int(input("nechta ism kiritmoqchsiz"))
# for i in range(n):
#     enter = input(f"{i+1}-ismni kiriitig:")
#     ismlar.append(enter)


# print(ismlar)

# def taqqoslash (a,b):
#     if a>b:
#        print(a)
#     else:
#        print(b)
#
#  taqqoslash(100,200

# def juft_son(sonlar):
#     juft = []
#     for son in sonlar:
#         if son % 2 == 0:
#             juft.append(son)
#     return juft
#
# malumot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(juft_son(malumot))
#


# def toq_son(sonlar):
#     toq = []
#     for son in sonlar:
#         if son % 2 ==0:
#            toq.append(son)
#     return toq
# son=[123456789]
# print(toq_son(son))


# def son (a,b):
#     print(a+b)
# son(2,3)


# car = {"model":"cobalt","colar":"red","ishlab_chiqarigan_yili":2026}
# print(car.get("model"))


# def xisobla(yosh):
#     print(2026-yosh)
#
# xisobla(24)
#


# def qaytar (a):
#     return a
# qaytar(2)
# print(qaytar)

# def qaytar(a):
#     return a**2
#
#
# print(qaytar(16))


# talaba={"ism":"diyor","fm":"safarov"}
#                values
#          keys2.
#
#            ITems

# car = {'rangi': 'sariq', 'eshiklar_soni': 4, 'shinalar_soni': 4, 'rul': 1}
# for i in car.items():
#     print(i)

# def xisobla(n):
#     a=f"{n**2} {n**3}"
#     print(9)
#


# i=1
# while i<100:
#     print(i)
#     i=i+1
#


# 1-masala
# def tugilgan_yil():
#     ism = input("Ismingizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))
#     yil = 2026 - yosh
#     print(f"{ism}, siz {yil}-yilda tug'ilgansiz.")
#

# # 2-masala
# def kvadrat_kub():
#     son = int(input("Son kiriting: "))
#     print("Kvadrati:", son ** 2)
#     print("Kubi:", son ** 3)
#
#
# # 3-masala
# def juft_toq():
#     son = int(input("Son kiriting: "))
#     if son % 2 == 0:
#         print("Juft son")
#     else:
#         print("Toq son")
#
#
# # 4-masala
def katta_son():
    a = int(input("1-son: "))
    b = int(input("2-son: "))

    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Sonlar teng")
#
#
# # 5-masala
# def daraja(x, y):
#     print(x ** y)
#
#
# 6-masala
# def daraja2(x, y=2):
#     print(x ** y)
#
#
# # 7-masala
# def bolinish_alomatlari(son):
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{son} {i} ga qoldiqsiz bo'linadi")
#
#
# # # Misol:
#
# # bolinish_alomatlari(70)


# def tugilgan_yil(ism, yosh):
#     print(f"{ism}, siz {2026-yosh}-yilda tug'ilgansiz.")
#
# tugilgan_yil("Munisa", 16)
#
#


# def kvadrat_kub(son):
#     print("Kvadrati:", son**2)
#     print("Kubi:", son**3)
#
# kvadrat_kub(5)


# son = 3
#
# while son <= 99:
#     print(son)
#     son += 2

# a = int(input("Son kiriting: "))
# for i in range(2, 11):
#     if a % i == 0:
#         print(f"{i} - ga qoldiqsiz bolinadi")
#     else:
#
#
#
#
# def bolinish(son):
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{i} ga qoldiqsiz bo'linadi")


# OOP-object orino programming


# class benefet:
#
#     def __init__(self,hello):
#
#         self.hello = hello
#
#     def salom_ber(self):
#
#         return self.hello
#
# a = benefet("salom yaxshimisz")
#
# print(a.salom_ber())
#
# class qosh:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#
#
#
# print(Qosh(5, 7).qoshish())


# misol1
# jami = 0
#
# while True:
#     mahsulot = input("Mahsulot nomi: ")
#
#     if mahsulot.lower() == "stop":
#         break
#
#     narx = float(input("Narxi: "))
#     jami += narx
#
# print("Jami xarajat:", jami)

# 3misol
# class Nom:
#     def __init__(self,a):
#         self.a=a
#     def salom_ber(self):
#         return self.a
# print(Nom("salom Dunyo").salom_ber())

# 4misol
#
class ismlar:
    def __init__(self, munisa, elnura, gulnoza, mushtariy, sarvinoz):
        self.munisa = munisa
        self.elnura = elnura
        self.gulnoza = gulnoza
        self.mushtariy = mushtariy
        self.sarvinoz = sarvinoz

    def bir(self):
        return self.munisa

    def ikki(self):
        return self.elnura

    def uch(self):
        return self.gulnoza

    def tort(self):
        return self.mushtariy

    def besh(self):
        return self.sarvinoz

w = ismlar("Munisa","Elnura","Gulnora","Nozima","Bonu")
print(w.bir())

# class Manzil:
#     def __init__(self, kocha, mahalla, tuman, viloyat):
#         self.kocha = kocha
#         self.mahalla = mahalla
#         self.tuman = tuman
# #         self.viloyat = viloyat
# #
# #     def chiqar(self):
# #         print(self.kocha)
# #         print(self.mahalla)
# #         print(self.tuman)
# #         print(self.viloyat)
# #
# #
# # manzil = Manzil("Bog'bon", "Sog'bon", "Bodomzor", "Samarqand")
# # manzil.chiqar()
#
# taomlar = []

# while True:
#     taom = input("Taom kiriting: ")
#     if taom.lower() == "stop":
#         break
#
#     if taom in taomlar:
#         print("Bu taom ro'yxatda bor")
#     else:
#         taomlar.append(taom)
#
# print("Taomlar ro'yxati:")
# for i in taomlar:
#     print(i)
#
#
# baholar = []
#
# while True:
#     baho = input("Baho kiriting: ")
#
#     if baho.lower() == "stop":
#         break
#
#     baho = int(baho)
#     baholar.append(baho)
#
#     if baho == 2:
#         print("Yomon")
#     elif baho == 5:
#         print("A'lo")
#
# if len(baholar) > 0:
#     print("O'rtacha baho:", sum(baholar) / len(baholar))
# else:
#     print("Baho kiritilmadi")
#
#     kichiklar = []
#     kattalar = []
#
#     while True:
#         ism = input("Ism kiriting: ")
#
#         if ism.lower() == "stop":
#             break
#
#         yosh = int(input("Yoshi: "))
#
#         if yosh < 18:
#             kichiklar.append(ism)
#         else:
#             kattalar.append(ism)
#
#     print("18 yoshdan kichiklar:")
#     print(kichiklar)
#
#     print("18 yosh va undan kattalar:")
#     print(kattalar)
#
#     parol = input("Parol o'rnating: ")
#
#     urinish = 0
#
#     while urinish < 3:
#         tekshir = input("Parolni kiriting: ")
#
#         if tekshir == parol:
#             print("Xush kelibsiz")
#             break
#
#         urinish += 1
#
#     if urinish == 3:
#         print("Dastur bloklandi")

# class Taomlar:
#     def tekshir(self):
#         royxat = []
#
#         while True:
#             taom = input("Taom: ")
#
#             if taom.lower() == "stop":
#                 break
#
#             if taom in royxat:
#                 print("Bu taom ro'yxatda bor")
#             else:
#                 royxat.append(taom)
#
#         print(royxat)
#
#         class Baho:
#             def tahlil(self):
#                 baholar = []
#
#                 while True:
#                     baho = input("Baho: ")
#
#                     if baho.lower() == "stop":
#                         break
#
#                     baho = int(baho)
#                     baholar.append(baho)
#
#                     if baho == 2:
#                         print("Yomon")
#                     elif baho == 5:
#                         print("A'lo")
#
#                 print("O'rtacha:", sum(baholar) / len(baholar))
#
#         obj = Baho()
#         obj.tahlil()
#
#
# obj = Taomlar()
# obj.tekshir()
#
# class Mehmon:
#     def royxat(self):
#         kichik = []
#         katta = []
#
#         while True:
#             ism = input("Ism: ")
#
#             if ism.lower() == "stop":
#                 break
#
#             yosh = int(input("Yosh: "))
#
#             if yosh < 18:
#                 kichik.append(ism)
#             else:
#                 katta.append(ism)
#
#         print("Kichiklar:", kichik)
#         print("Kattalar:", katta)
#
#
# obj = Mehmon()
# obj.royxat()
#
# class Parol:
#     def tekshir(self):
#         parol = input("Parol o'rnating: ")
#
#         for i in range(3):
#             kirit = input("Parolni kiriting: ")
#
#             if kirit == parol:
#                 print("Xush kelibsiz")
#                 return
#
#         print("Dastur bloklandi")
#
#
# obj = Parol()
# obj.tekshir()
#
#

 # 1 misol
#
# def juft_sonlar(list):
#     yangi = []
#     for son in list:
#         if son % 2 == 0:
#             yangi.append(son)
#     return yangi
#
# sonlar = [1, 2, 3, 4, 5, 6, 8]
# print(juft_sonlar(sonlar))
#
# # 2 misol
# def uzun_sozlar_soni(list):
#     sanoq = 0
#     for soz in list:
#         if len(soz) > 5:
#             sanoq += 1
#     return sanoq
#
# sozlar = ["olma", "dasturlash", "kitob", "telefon", "uy"]
# print(uzun_sozlar_soni(sozlar))
#
# # 3 misol
# n = int(input("N sonini kiriting: "))
#
# for i in range(1, n + 1):
#     print(f"{i} x {i} = {i*i}")
#
# # 4 misol
# def eng_katta(lst):
#     katta = lst[0]
#     for son in lst:
#         if son > katta:
#             katta = son
#     return katta
#
# sonlar = [12, 45, 7, 89, 23]
# print(eng_katta(sonlar))
#  # 5 misol
# def palindrom_sozlar(lst):
#     yangi = []
#     for soz in lst:
#         if soz == soz[::-1]:
#             yangi.append(soz)
#     return yangi
#
# sozlar = ["non", "kitob", "alla", "olma", "radar"]
# print(palindrom_sozlar(sozlar))
#
# # 6 misol
# def baho_tekshir(lst):
#     orta = sum(lst) / len(lst)
#     if orta > 60:
#         return "O‘tdi"
#     else:
#         return "Yiqildi"
#
# baholar = [70, 80, 50, 60]
# print(baho_tekshir(baholar))
#
#  # 7 misol
# def takrorni_ochir(lst):
#     yangi = []
#     for i in lst:
#         if i not in yangi:
#             yangi.append(i)
#     return yangi
#
# sonlar = [1, 2, 2, 3, 4, 4, 5]
# print(takrorni_ochir(sonlar))
#
# # 8 misol
# def yigindi_10_dan_katta(list):
#     yangi = []
#     for son in list:
#         yig = 0
#         for raqam in str(son):
#             yig += int(raqam)
#         if yig > 10:
#             yangi.append(son)
#     print(yangi)
#
# sonlar = [12, 99, 34, 100, 56]
# yigindi_10_dan_katta(sonlar)
#
# # 9 misol
# def parol_tekshir(parol):
#     katta_harf = False
#     raqam = False
#
#     for belgi in parol:
#         if belgi.isupper():
#             katta_harf = True
#         if belgi.isdigit():
#             raqam = True
#
#     if katta_harf and raqam:
#         return "Parol to‘g‘ri"
#     else:
#         return "Parolda kamida 1 ta katta harf va 1 ta raqam bo‘lishi kerak"
#
# print(parol_tekshir("Salom123"))
#
# # 10 misol
# def qimmat_mevalar(lugat):
#     natija = []
#     for meva, narx in lugat.items():
#         if narx > 5000:
#             natija.append(meva)
#     return natija
#
# mevalar = {
#     "olma": 4000,
#     "banan": 7000,
#     "anor": 8000,
#     "uzum": 5000
# }
#
# print(qimmat_mevalar(mevalar))
#
# # 11 misol
# def fibonachchi(n):
#     royxat = []
#     a, b = 0, 1
#     while len(royxat) < n:
#         royxat.append(a)
#         a, b = b, a + b
#     return royxat
# # 12 misol
# def harf_chastota(matn):
#     lugat = {}
#     for harf in matn:
#         if harf != " ":
#             if harf in lugat:
#                 lugat[harf] += 1
#             else:
#                 lugat[harf] = 1
#     return lugat
#
# matn = input("Matn kiriting: ")
# print(harf_chastota(matn))
#
# # 13 misol
# def bankomat(balans, summa):
#     if balans >= summa:
#         balans -= summa
#         return balans
#     else:
#         return "Mablag‘ yetarli emas"
#
# print(bankomat(100000, 30000))
#
# # 14 misol
def savat(narxlar):
    jami = sum(narxlar)

    if jami > 100000:
        chegirma = jami * 0.10
        jami -= chegirma

    return jami

mahsulotlar = [30000, 40000, 50000]
print(savat(mahsulotlar))
# #
# # 15 misol
# class Product:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
# def eng_qimmat_mahsulot(mahsulotlar):
#     eng_qimmat = mahsulotlar[0]
#
#     for mahsulot in mahsulotlar:
#         if mahsulot.narx > eng_qimmat.narx:
#             eng_qimmat = mahsulot
#
#     return eng_qimmat.nom
#
# p1 = Product("Telefon", 2500000)
# p2 = Product("Quloqchin", 300000)
# p3 = Product("Noutbuk", 7000000)
#
# royxat = [p1, p2, p3]
# print(eng_qimmat_mahsulot(royxat))
#
#
# class Salom:
#     def chiqar(self):
#         print("Salom")
#
# obj = Salom()
# obj.chiqar()
#
# class Myclass:
#     a=5
#
# p1=Myclass()


# print(p1.a)

# class Qoshish:
#     def init(self, a, b):
#         self.a = a
#         self.b = b
#
#     def natija(self):
#         return self.a + self.b
#
#
# a = float(input("1-son: "))
# b = float(input("2-son: "))
# ++
# hisob = Qoshish(a,b)
# print("Natija:", hisob.natija())




class Salom:
    matn = "Hello World!"

    def chiqar(self):
        print(Salom.matn)

Salom.chiqar()


class Xabar:
    xabar = "Bugun havo yaxshi."

    def chiqar(self):
        print(Xabar.xabar)

        Xabar.xabar = "Yangi xabar."
        print(Xabar.xabar)

Xabar.chiqar()


# class Misol:
#     class_ = "Python"
#
#     def chiqar(self):
#         print(Misol.class_)
#
# Misol.chiqar()
#
#
# class Aylana:
#     radius = 5
#     pi = 3.14159
#
#     def hisobla(self):
#         aylana_yuzi = Aylana.pi * Aylana.radius ** 2
#         print("Radiusi", Aylana.radius, "ga teng aylananing yuzi =", aylana_yuzi)
#
# Aylana.hisobla()



# class Aylana:
#     radius = 5
#     pi = 3.14159
#
#     def hisobla(self):
#         aylana_yuzi = Aylana.pi * Aylana.radius ** 2
#         print("Radiusi", Aylana.radius, "ga teng aylananing yuzi =", aylana_yuzi)





























