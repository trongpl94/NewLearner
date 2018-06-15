list = [2]
f_n = 2
cong_sai_chan = 0
number_n = int(input("Nhap so:"))
for i in range(1,number_n):
    f_n += 1
    if f_n % 2 == 0:
        cong_sai_chan += 2.5
        next_n = f_n - cong_sai_chan
        list.append(next_n)
    if f_n % 2 == 1:
        list.append(-1)
print(list)
