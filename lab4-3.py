x ={"name" : "jidapa","age" : 18,"wt" : 45,"h" : 156}

print(x)
print("สวัสดีค่ะคุณ %s" % x["name"])
print("พ.ศ.เกิด %d อายุ %d ปี" % (2567-x["age"], x["age"]))
print("น้าหนัก %d ส่วนสูง %d เซนติเมตร" % (x["wt"], x["h"]))