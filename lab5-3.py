def F(c):
    fa = (9/5)*c+32
    return fa

def K(c):
    ke = c+273.15
    return ke


c = int(input("ค่าอุณหภูมิองศาเซลเซียส : "))
print("อุณหภูมิฟาเรนไฮส์ = %.2f" % F(c))
print("อุณหภูมิเคอริน = %.2f" % K(c))