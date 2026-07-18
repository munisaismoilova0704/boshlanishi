def savat(narxlar):
    jami = sum(narxlar)

    if jami > 100000:
        chegirma = jami * 0.10
        jami -= chegirma

    return jami

mahsulotlar = [30000, 40000, 50000]
print(savat(mahsulotlar))
