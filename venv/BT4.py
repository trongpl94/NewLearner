def tinh_abs_tong(mang_1):
    try:
        import numpy as np
        first_nb = mang_1[0]
        for i in range(1,len(mang_1)):
            first_nb += mang_1[i]
            tong_mang = abs(first_nb)
        print("Total of List:",tong_mang)
    except:
        print("Kieu du lieu k tinh dc tong")
tinh_abs_tong(mang_1=[-1,-2,-10,-4])
