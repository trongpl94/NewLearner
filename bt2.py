def luythua2(a):
        list_a = []
        if a == 0:
            list_a.append(1)
        if a < 0:
            print("Lai xam`")
        else:
            for i in range(0,a):
                luythua2 = 2**i
                list_a.append(luythua2)
            print(list_a)
try:
    a = int(input("Nhap mot so bat ki:"))
    luythua2(a)
except:
    print("Lai nhap sai")