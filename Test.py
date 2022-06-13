import turtle as t
import math
a = int(input('Nhap so hinh vuong muon ve: '))
b = float(input('Nhap canh hinh vuong be nhat: '))

for i in range(a):
    for i in range(4):
        t.fd(b)
        t.lt(90)
    t.penup()
    t.lt(45)
    t.bk(5*math.sqrt(2))
    t.pendown()
    t.rt(45)
    b += 10