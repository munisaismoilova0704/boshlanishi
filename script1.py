# # def katta_son():
# #     a = int(input("1-son: "))
# #     b = int(input("2-son: "))
# #
# #     if a > b:
# #         print(a)
# #     elif b > a:
# #         print(b)
# #     else:
# # #         print("Sonlar teng")
# #
# # class avto:
# #     def __init__(self, model, rang,karopka, narx):
# #         self.model = model
# #         self.rang = rang
# #         self.karopka =karopka
# #         self.narx = narx
# #         self.km = 0
# #
# #     def korsat(self):
# #         return self.model,self.rang,self.rang,self.karopka,self.narx, self.km
# #
# #     def update_km(self,km):
# #         return self.km
# #
# # avto1 = avto('cobalt','oq','avtomat','150000')
# #
# # avto1.update_km(500)
# # avto.korsat()
#
#
# # def chipta():
# #     while True:
# #         yosh = input("Yoshingiz: ")
# #
# #         if yosh == "exit" or yosh == "quit":
# #             return
# #
# #         yosh = int(yosh)
# #
# #         if yosh < 7:
# #             print("2000 so'm")
# #         elif yosh < 18:
# #             print("3000 so'm")
# #         elif yosh < 65:
# #             print("10000 so'm")
# #         else:
# #             print("Bepul")
#
#
# def kitob():
#     while True:
#         nom = input("Kitob nomi: ")
#         if nom == "stop":
#             return
# #         print(nom)
# #
#
# class Shaxs:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#
#     def get_info(self):
#         return f"Ism: {self.ism}, Yosh: {self.yosh}"
#
#
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#
#     def get_info(self):
#         return f"Fan: {self.nomi}"
#
#
# class Talaba(Shaxs):
#     def __init__(self, ism, yosh):
#         super().__init__(ism, yosh)
#         self.fanlar = []
#
#     def fanga_yozil(self, fan):
#         self.fanlar.append(fan)
#
#     def remove_fan(self, fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#         else:
#             return "Siz bu fanga yozilmagansiz"
#
#     def get_info(self):
#         fanlar = []
#         for fan in self.fanlar:
#             fanlar.append(fan.nomi)
#         return f"Talaba: {self.ism}, Yosh: {self.yosh}, Fanlar: {fanlar}"
#
#
# class Professor(Shaxs):
#     def __init__(self, ism, yosh, mutaxassislik):
#         super().__init__(ism, yosh)
#         self.mutaxassislik = mutaxassislik
#
#     def get_info(self):
#         return f"Professor: {self.ism}, Mutaxassisligi: {self.mutaxassislik}"
#
#
# class Foydalanuvchi(Shaxs):
#     def __init__(self, ism, yosh, login):
#         super().__init__(ism, yosh)
#         self.login = login
#
#     def get_info(self):
#         return f"Foydalanuvchi: {self.ism}, Login: {self.login}"
#
#
# class Admin(Foydalanuvchi):
#     def __init__(self, ism, yosh, login):
#         super().__init__(ism, yosh, login)
#
#     def ban_user(self):
#         return "Foydalanuvchi bloklandi"
#
#     def get_info(self):
#         return f"Admin: {self.ism}, Login: {self.login}"
#
#
# # Fan obyektlari
# matematika = Fan("Matematika")
# python = Fan("Python")
# ingliz = Fan("Ingliz tili")
#
# # Talaba
# t1 = Talaba("Ali", 20)
# t1.fanga_yozil(matematika)
# t1.fanga_yozil(python)
#
# print(t1.get_info())
#
# print(t1.remove_fan(ingliz))
#
# # Professor
# p1 = Professor("Karim", 45, "Matematika")
# print(p1.get_info())
#
# # Admin
# a1 = Admin("Vali", 30, "admin01")
# print(a1.get_info())
# print(a1.ban_user())




# class ismlar :
#     def __init__(self):
#         self.ismlar = []
#     def kiritish(self):
#         a=int(input("nechta ism kiritmochisi: "))
#
#         for i in range(a):
#             b=input(f"{i+1}-ism kiriting: ")
#             self.ismlar.append(b)
#         return self.ismlar
#
#
#
# print(ismlar().kiritish())


# class car :
#    def __init__(self,markasi,modelli, yili):
#        self.markasi = markasi
#        self.modeli = modelli
#        self.yili = yili
#    def info(self):
#        return f"{self.markasi}{self.modeli}{self.yili}"
#
#
#    car1 = car("chevrolet", "cobalt",2022)
#    car2 = car("Kia","K5",2024)
#
#
#    print(car1.info())
#    print(car2.info())
#




class Student:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

student1 = Student(input("Ism: "), input("Yosh: "), input("Kurs: "))
student2 = Student(input("Ism: "), input("Yosh: "), input("Kurs: "))

print(student1.ism, student1.yosh, student1.kurs)
print(student2.ism, student2.yosh, student2.kurs)


class Book:
    def __init__(self, nomi, muallifi, sahifa):
        self.nomi = nomi
        self.muallifi = muallifi
        self.sahifa = sahifa

book1 = Book(input("Nomi: "), input("Muallifi: "), input("Sahifa: "))
book2 = Book(input("Nomi: "), input("Muallifi: "), input("Sahifa: "))

print(book1.nomi, book1.muallifi, book1.sahifa)
print(book2.nomi, book2.muallifi, book2.sahifa)




class House:
    def __init__(self, manzil, xona, narx):
        self.manzil = manzil
        self.xona = xona
        self.narx = narx

house1 = House(input("Manzil: "), input("Xona: "), input("Narx: "))
house2 = House(input("Manzil: "), input("Xona: "), input("Narx: "))

print(house1.manzil, house1.xona, house1.narx)
print(house2.manzil, house2.xona, house2.narx)


class Restaurant:
    def __init__(self, nomi, taom_turi, vaqt):
        self.nomi = nomi
        self.taom_turi = taom_turi
        self.vaqt = vaqt

rest1 = Restaurant(input("Nomi: "), input("Taom turi: "), input("Ochilish vaqti: "))
rest2 = Restaurant(input("Nomi: "), input("Taom turi: "), input("Ochilish vaqti: "))

print(rest1.nomi, rest1.taom_turi)
print(rest2.nomi, rest2.taom_turi)





























































