chest = int(input("กรอกขนาดหน้าอก: "))

if chest <= 34:
    print("ขนาดเสื้อ: XS")
elif chest <= 36:
    print("ขนาดเสื้อ: S")
elif chest <= 38:
    print("ขนาดเสื้อ: M")
elif chest <= 40:
    print("ขนาดเสื้อ: L")
else:
    print("ขนาดเสื้อ: XL")
