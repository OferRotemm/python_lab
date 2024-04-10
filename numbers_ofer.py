from posixpath import split


def dividable_by_10(num) :
    if  num == 0 :
      return None
    elif num % 10 == 0 :
        return True
    else :
        return False


def sum_of_digits(num) :
    sum = 0
    if num < 0 :
      num = abs(num)
    num_list =  [int(x) for x in str(num)]
    for n in  num_list :
        sum = sum + int(n)
    return sum


def is_palindrome(num) :
    if num < 0 :
       num = abs(num) 
    num_list =  [int(x) for x in str(num)]
    op_num = num_list[::-1]
    if num_list == op_num :
        return True
    else :
        return False

if __name__ == '__main__' :

    t1 = dividable_by_10(50)
    t2 = dividable_by_10(36)
    t3 = dividable_by_10(0)
    t4 = dividable_by_10(-50)

    print(t1)
    print(t2)
    print(t3)
    print(t4)
   

    t5 = sum_of_digits(5)
    t6 = sum_of_digits(123)
    t7 = sum_of_digits(0)
    t8 = sum_of_digits(-50)

    print(t5)
    print(t6)
    print(t7)
    print(t8)
   


    t9 = is_palindrome(5678)
    t10 = is_palindrome(1221)
    t11 = is_palindrome(0)
    t12 = is_palindrome(-34543)
    print(t9)
    print(t10)
    print(t11)
    print(t12)