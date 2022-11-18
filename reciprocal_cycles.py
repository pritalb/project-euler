'''
Created on 9 Nov 2022 at 5:29 pm

@author: Prital Bamnodkar
'''

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


from decimal import getcontext, Decimal

# returns a list of slices of str. the slices will be of the specified size.
def split_into_parts(inputStr, size):
    out = []
    str_len = len(inputStr)
    start_index = 0
    end_index = 0

    while end_index <= str_len:
        end_index = start_index + size

        out.append(inputStr[start_index : end_index])
        start_index = end_index

    return out

# check if all elements in a list are identical. all elements must be str or lists
def are_same(ls):
    if ls == [] or len(ls) == 1:
        return False
    
    first_elem = ls[0]
    last_elem = ls[-1]

    for elem in ls[1:-1]:
        if elem != first_elem:
            return False
    
    if (len(first_elem) > len(last_elem)) and (len(last_elem) > 10):
        return first_elem[:len(last_elem)] == last_elem
    else:
        return first_elem == last_elem

def find_recurring_part(fract):
    temp = fract[:]

    for size in range(1, len(temp)):
        parts = split_into_parts(temp, size)
        found = are_same(parts)

        if found:
            return parts[0]
    return None

def get_recurring_part(fract):
    iterable = fract[:]
    out = ''
    non_recurring_part = ''

    while len(iterable) > 1:
        temp = find_recurring_part(iterable)

        if temp == None:
            non_recurring_part += iterable[0]
            iterable = iterable[1:]
        else:
            out = temp
            break
    return (non_recurring_part, out)


def format_fract(fract):
    '''
    IN:
        fract: a float
        a fraction in decimal form

    Out:
        a string of the properly formatted fraction
        e.g. 0.3333333333 -> 0.(3)
             0.1666666666 -> 0.1(6)
    '''
    fract_parts = get_recurring_part(fract)
    return f'{fract_parts[0]}({fract_parts[1]})'

def test_find_recurring_part():
    n = 659
    # n = 6
    fract = str(Decimal(1) / Decimal(n))[:-1]
    print(find_recurring_part(fract))

def test_get_recurring_part():
    n = 659
    # n = 6
    fract = str(Decimal(1) / Decimal(n))[:-1]

    print(fract)
    print(get_recurring_part(fract))

def test_split_into_parts():
    size = 4
    s = 'abcdefghij'
    print(split_into_parts(s, size))

def test_format_fraction():
    fract = str(Decimal(1) / Decimal(97))

    # the last digit of the fraction is rounded up, so it needs to be gotten rid of
    fract = fract[:-1]
    
    print(fract)
    print(format_fract(fract))



def get_recurring_fractions(n):
    '''
    In:
        n: int

    Out:
        a list of tuples of n and 1/n. only tuples with 1/n being a recurring fraction are considered.
    '''
    out = {}

    recurring_fract_len = len(str(Decimal(1) / Decimal(3))[:-1]) - 10 #10 is error correction since the fraction will also contain stuff like '0.'

    for i in range(2, n):
        fract = str(Decimal(1) / Decimal(i))[2:-1] # the '0.' at the start is not needed
        if len(fract) >= recurring_fract_len:
            temp = get_recurring_part(fract)

            recurring_part_size = len(temp[1])
            i_out = (i, temp[0], temp[1])

            if recurring_part_size in out.keys():
                out[recurring_part_size].append(i_out)
            else:
                out[recurring_part_size] = [i_out]
    return out

def test_get_recurring_fractions():
    n = 50
    res = get_recurring_fractions(n)
    print(res)



if __name__ == '__main__':
    #setting precision of decimal
    getcontext().prec = 1000

    n = 1000

    fracts = get_recurring_fractions(n)
    # print(fracts)

    biggest_key = max(fracts.keys())
    print(biggest_key)
    
    num_with_biggest_key = fracts[biggest_key]
    print(num_with_biggest_key)

    # test_format_fraction()
    # test_get_recurring_fractions(100)
    # test_find_recurring_part()
    # test_get_recurring_part()