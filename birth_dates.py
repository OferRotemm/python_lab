import numbers_ofer

def is_lucky(x) :
    pal = numbers_ofer.is_palindrome(x)
    sum = numbers_ofer.sum_of_digits(x)
    div_10 = numbers_ofer.dividable_by_10(sum)
    if pal is True or div_10 is True :
        return True
    else:
        return False


import col

def lucky_people2(name, birth_dates) :
    bd_dic = col.lists2dict(name, birth_dates)
    lucky_li = []
    bd_duplicates = {}
    for name in bd_dic :
        if is_lucky(name) == True :
            lucky_li.append(name)

    for date in birth_dates:
        bd_duplicates = col.elems_count(date)  

    return lucky_li , bd_duplicates




def lucky_people(name, birth_dates) :
    years = []
    bd_duplicates = []
    lucky_li = []
    for date in birth_dates:
        date = date[-1:-4]
        if is_lucky(int(date)):
            lucky_li.append(name[date])
    
      

    return lucky_li , bd_duplicates



t1 = is_lucky(1987)
t2 = is_lucky(2002)
t3 = is_lucky(2008)

print(t1)
print(t2)
print(t3)
print('--------------------')

a = ['ofer', 'nir', 'amit', 'alon']
b = ['23-01-1982', '23-06-2012', '10-06-1984', '20-05-2002']
print(lucky_people(a,b))
print('--------------------')