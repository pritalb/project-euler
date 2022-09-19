'''

@author: Prital Bamnodkar

'''


# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 2
# 8 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
# if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as 
# the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater 
# than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced 
# any further by analysis even though it is known that the greatest number that cannot be expressed as the 
# sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.



import math

proper_divs_dict = {
    1 : [1],
}

def get_proper_divisors_of(n):
    if n in proper_divs_dict.keys():
        return proper_divs_dict[n]

    divs = []

    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if i == n:
            break

        if n % i == 0:
            divs.append(i)

            temp = n // i

            if temp not in divs and temp != n:
                divs.append(n // i)

            if i != 1:
                temp_divs = proper_divs_dict[temp]
                for temp_div in temp_divs:
                    temp2 = i * temp_div

                    if temp_div not in divs:
                        divs.append(temp_div)

                    if temp2 not in divs:
                        divs.append(temp2)
                break

    proper_divs_dict[n] = sorted(divs)
    return proper_divs_dict[n]

def get_proper_divisors_of_all_upto(n):
    max_known_num = max(proper_divs_dict.keys())

    for i in range(max_known_num, n + 1):
        divs = get_proper_divisors_of(i)

def is_abundant(n):
    if not n in proper_divs_dict.keys():
        get_proper_divisors_of_all_upto(n)

    divs = proper_divs_dict[n]
    return sum(divs) > n

def abundant_nums_upto(n):
    res = []

    for i in range(1, n + 1):
        if is_abundant(i):
            res.append(i)

    return sorted(res)

def two_abundant_num_sums_upto(n):
    res = []
    abundant_nums = abundant_nums_upto(n)

    for i in range(len(abundant_nums)):
        k = abundant_nums[i]
        temp_list = [j + k for j in abundant_nums[i:]]
        res = res + temp_list

    # convert to set to remove duplicates
    return sorted(list(set(res)))

def non_abundant_sums_upto(n):
    two_abundant_num_sums = two_abundant_num_sums_upto(n)

    nums_upto = list(range(1, n + 1))

    return list(set(nums_upto) - set(two_abundant_num_sums))

if __name__ == '__main__':
    n = 28123

    get_proper_divisors_of_all_upto(n)
    non_abundant_sums = non_abundant_sums_upto(n)
    print(sum(non_abundant_sums))