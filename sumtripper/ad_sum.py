def ad_sum(a, b):
    return a+b

def sum_list(*numbers):
    res = 0 
    for el in numbers:
        res += el
    return res