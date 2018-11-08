# Задача 1
fruits=["яблоко", "банан", "киви", "арбуз"]
i = 1
for fruit in fruits:
     print("{}.{:>10}".format(str(i), fruit))
     i+=1

## Пыталась задать выравнивае по самому длинному слову, но выдет ошибку
fruits=["яблоко", "банан", "киви", "арбуз"]
length=0
for fruit in fruits:
    if length<len(fruit):
        length=len(fruit)
i = 1
for fruit in fruits:
    print("{}.{:>length}".format(str(i), fruit))
    i+=1

# Задача 2
## Вариант 1
list1=['a',23,'d',4,5]
list2=['a',43,'k',4,6]
for b in list2:
    i=0
    for a in list1:
        if a==b:
            list1.pop(i)
        i+=1
print(list1)

##Вариант 2
list1=['a',23,'d',4,5]
list2=['a',43,'k',4,6]
s=set(list1)
t=set(list2)
list1=list(set(s-t))
print(list1)

# Задача 3
list1=[2,24,51,3,45,12]
list_new=[]
for i in list1:
    if i%2==0:
        i=i/4
    else:
        i=i*2
    list_new.append(i)
print(list_new)



