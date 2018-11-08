# Задача 1
new_list=[i**2 for i in old_list]

return(new_list)


# Задача 2
list1=['apple','cherry','watermelon','orange']
list2=['plum','grape','apple','orange','lime']

new_list=[ i for i in list1 if i is i in list2 ]

print(new_list)


#Задача 3
new_list=[i for i in list1 if i>0 and i%3==0 and i%4!= 0]

print(new_list)