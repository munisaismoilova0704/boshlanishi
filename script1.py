# def katta_son():
#     a = int(input("1-son: "))
#     b = int(input("2-son: "))
#
#     if a > b:
#         print(a)
#     elif b > a:
#         print(b)
#     else:
# #         print("Sonlar teng")
#
# class avto:
#     def __init__(self, model, rang,karopka, narx):
#         self.model = model
#         self.rang = rang
#         self.karopka =karopka
#         self.narx = narx
#         self.km = 0
#
#     def korsat(self):
#         return self.model,self.rang,self.rang,self.karopka,self.narx, self.km
#
#     def update_km(self,km):
#         return self.km
#
# avto1 = avto('cobalt','oq','avtomat','150000')
#
# avto1.update_km(500)
# avto.korsat()


def chipta():
    while True:
        yosh = input("Yoshingiz: ")

        if yosh == "exit" or yosh == "quit":
            return

        yosh = int(yosh)

        if yosh < 7:
            print("2000 so'm")
        elif yosh < 18:
            print("3000 so'm")
        elif yosh < 65:
            print("10000 so'm")
        else:
            print("Bepul")






