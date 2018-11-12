#Задача 1
def my_round(number, ndigits):
    num_list = list(str(number))
    num_string_new = ''
    n = 0
    for digit in num_list:
        if digit == ".":
            if int(num_list[n + ndigits+1]) >= 5:
                num_list[n + ndigits] = str(int(num_list[n + ndigits]) + 1)
                break
        n += 1
    for digit in num_list[:(n + ndigits+1)]:
        num_string_new +=digit
    return (float(num_string_new))




#Задача 2

def lucky_ticket(ticket_number):
    list_number=[int(i) for i in str(ticket_number)]
    if len(list_number)!=6:
        return('Check your number, there have to be 6 digits')

    if sum(list_number[:3])==sum(list_number[3:]):
        return("Lucky ticket, congrats!")
    else:
        return("Not this time")