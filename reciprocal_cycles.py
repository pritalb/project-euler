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

def get_recurring_fractions(n):
    '''
    In:
        n: int

    Out:
        a list of tuples of n and 1/n. only tuples with 1/n being a recurring fraction are considered.
    '''
    out = []
    recurring_fract_len = len(str(1/3))

    for i in range(2, n):
        fract = 1/i
        if len(str(fract)) >= recurring_fract_len:
            out.append((i, fract))

    return out

def test_get_recurring_cycles():
    n = 10
    res = get_recurring_fractions(n)
    print(*res, sep='\n')

# returns a list of slices of str. the slices will be of the specified size.
def split_into_parts(inStr, size):
    out = []
    str_len = len(inStr)
    start_index = 0
    end_index = 0

    while end_index <= str_len:
        end_index = start_index + size

        out.append(inStr[start_index : end_index])
        start_index = end_index

    return out

# check if all elements in a list are identical. all elements must be str or lists
def are_same(ls):
    if ls == [] or len(ls) == 1:
        return True
    
    first_elem = ls[0]
    last_elem = ls[-1]

    for elem in ls[:-1]:
        if elem != first_elem:
            return False
    
    if len(first_elem) > len(last_elem):
        return first_elem[:len(last_elem)] == last_elem
    else:
        return first_elem == last_elem


def get_recurring_part(fract):
    '''
    IN:
        fract: a float
        a fraction in decimal form

    Out:
        a string of the properly formatted fraction
        e.g. 0.3333333333 -> 0.(3)
             0.1666666666 -> 0.1(6)
    '''
    out = '0.'
    fraction_part = str(fract)[2:]
    print(fraction_part)

    return out

def test_get_recurring_part():
    n = 3
    print(get_recurring_part(1/n))

def test_split_into_parts():
    size = 4
    s = 'abcdefghij'
    print(split_into_parts(s, size))

if __name__ == '__main__':
    s = '16666666666'
    s1 = split_into_parts(s, 1)

    print(are_same(s1))