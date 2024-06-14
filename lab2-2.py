print("โปรดกรอกข้อมูล : ")

y = int(input("คะแนน : "))

if y >100:
    print("กรุณากรอกข้อมูล 0-100")
elif y <0:
    print("กรุณากรอกข้อมูล 0-100")
else:
    if y >=80:
        print("เกรด A")
    elif y >=70:
        print("เกรด B")
    elif y >=60:
        print("เกรด C")
    elif y >=50:
        print("เกรด D")
    else:
        print("เกรด F")
