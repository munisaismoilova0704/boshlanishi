# def savat(narxlar):
#     jami = sum(narxlar)
#
#     if jami > 100000:
#         chegirma = jami * 0.10
#         jami -= chegirma
#
#     return jami
#
# mahsulotlar = [30000, 40000, 50000]
# print(savat(mahsulotlar))
#
#
# class Shaxs:
#     def __init__(self, ism):
#         self.ism = ism
#
#     def malumot(self):
#         return self.ism
#
#
# class Oquvchi(Shaxs):
#     pass
#
#
# class Kitob:
#     def __init__(self, nomi, muallifi):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.oquvchilar = []
#
#     def berish(self, oquvchi):
#         self.oquvchilar.append(oquvchi)
#
#     def qaytar(self, oquvchi):
#         if oquvchi in self.oquvchilar:
#             self.oquvchilar.remove(oquvchi)
#         else:
#             return "Bu kitob sizda emas"
#
#     def malumot(self):
#         return self.nomi, self.muallifi
#
#
# class Kutubxona:
#     def __init__(self, nomi):
#         self.nomi = nomi


# class Kutubxonachi(Shaxs):
#     def __init__(self, ism, ish_staji):
#         super().__init__(ism)
#         self.ish_staji = ish_staji
#
#     def malumot(self):
#         return self.ism, self.ish_staji
#
#
# # Obyektlar
# o1 = Oquvchi("Ali")
# o2 = Oquvchi("Vali")
#
# k1 = Kitob("Python", "Anvar")
# k2 = Kitob("Matematika", "Hasan")
#
# kutubxona = Kutubxona("Markaziy kutubxona")
#
# kutubxonachi = Kutubxonachi("Dilshod", 5)
#
# # Kitob berish
# k1.berish(o1)
# k1.berish(o2)
#
# # Kitob qaytarish
# # print(k1.qaytar(o1))
# print(k1.qaytar(o1))
#
# # Natijalar
# print(k1.oquvchilar)
# print(kutubxonachi.malumot())


#
# 1-masala
def tugilgan_yil():
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    yil = 2026 - yosh
    print(f"{ism}, siz {yil}-yilda tug'ilgansiz.")

