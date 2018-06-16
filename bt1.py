def tim_quy_luat_so(number_n):
        list = [2]
        f_n = 2
        cong_sai_chan = 0
        if number_n <= 0:
            list = []
        for i in range(1,number_n):
            f_n += 1
            if f_n % 2 == 0:
                cong_sai_chan += 2.5
                next_n = f_n - cong_sai_chan
                list.append(next_n)
            if f_n % 2 == 1:
                list.append(-1)
        print(list)
while True:
    try:
        a = int(input("Nhap 1 so bat ki:"))
        tim_quy_luat_so(a)
        break
    except:
        print("Nhap lai di anh zai, Troll nhau a??:)")