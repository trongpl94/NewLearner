def tim_mang_YZ(list_x):
    try:
        import math
        list_y = []
        list_z = []
        for i in range(len(list_x)):
            res_for_listz = (math.cos(list_x[i]) - math.sin(list_x[i]))
            list_z.append(res_for_listz)
            res_for_listy = math.pi/2 - list_x[i]
            list_y.append(res_for_listy)
            total_y = math.fsum(list_y)
        print(total_y)
        print(list_y)
    except:
        print("Mang sai du lieu.")
tim_mang_YZ(list_x = [2,5,7,12,19])
