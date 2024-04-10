def unique_values(li) :
    if len(li) > 0 :
        new_li = []
        for num in li :
            if num not in new_li :
                new_li.append(num)
    else :
        return None           
    return new_li




def lists2dict2(keys, values) :
    if len(keys) > len(values):
      x = len(values)
    else:
      x = len(keys)
    dic = {}
    for li in range (x):
        if keys[li] in dic :
            return None
        else:
            dic[keys[li]] = values[li]

    return dic





def elems_count(x) :
    word_count = {}
    for word in x:
        if word not in word_count :
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count






if __name__ == '__main__' :

    x = [5,6,7,6,4,3,2,4]
    y = []
    z = [8,9,70,54,-9,3,70,8,21]

    t1 = unique_values(x)
    t2 = unique_values(y)
    t3 = unique_values(z)

    print(t1)
    print(t2)
    print(t3)
    print("-------------------")


    a = [1,2,3,4,5,6,7]
    b = ['a','b','c','d','e']

    t4 = lists2dict2(b, a)
    t5 = lists2dict2(a, b)
    print(t4)
    print(t5)

    c = [1,2,3,4,5,6,7]
    d = ['a','b','c','d','e','c','d']

    print(lists2dict2(c,d))
    print(lists2dict2(d,c))
    print("-------------------")

    print(elems_count(d))