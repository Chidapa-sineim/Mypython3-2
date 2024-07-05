def beforMidterm(a,b,c):
    score = a+b+c
    return score


A = int(input("คะแนนเก็บ :"))
B = int(input("คะแนนจิตรพิสัย :"))
C = int(input("คะแนนกลางภาค :"))

if A <=20 and B <=10 and C <=20:
    print("คะแนนรวม %d" % beforMidterm(A ,B, C))
else:
    print("โปรดกรอกคะแนนใหม่")
