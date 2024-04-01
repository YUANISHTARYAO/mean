print ("Enter 5 numbers:")
a = input("number 1:")
fl_a = float(a)
b = input("number 2:")
fl_b = float(b)
c = input("number 3:")
fl_c = float(c)
d = input("number 4:")
fl_d = float(d)
e = input("number 5:")
fl_e = float(e)

output = (fl_a+fl_b+fl_c+fl_d+fl_e)/5

print(f"The mean of [{a}, {b}, {c}, {d}, {e}] is {output:.2f}")
