# Задача 1
def fibonacci(n,m):
    f=[1,1]

    for i in range(2,m):
           f.append(f[i-1]+f[i-2])
    print(f[(n-1):m])

fibonacci(3,12)


# Задача 2
def sort_to_max(origin_list):
    n=1
    while n<len(origin_list):
        for i in range(len(origin_list)-1):
            if origin_list[i]>origin_list[i+1]:
                origin_list[i],origin_list[i+1]=origin_list[i+1],origin_list[i]
        n+=1
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Дальше сдалась