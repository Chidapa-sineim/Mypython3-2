
o = int(input("น้ำหนัก : "))
x = int(input("ส่วนสูง : "))

xy = o/(x/100)**2
print(xy)

if xy <= 18.50:
    print("น้ำหนักน้อย/ผอม")
elif xy <=18.50 and xy >=22.90:
    print("ปกติ(สุขภาพดี)")
elif xy >=23 and xy <=24.90:
    print("ท้วม/โรคอ้วนระดับ1")
elif xy >=25 and xy <=29.90:
    print("อ้วน/โรคอ้วนระดับ2")
else:
    print("อ้วน/โรคอ้วนระดับ3")