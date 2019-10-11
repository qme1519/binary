def check(number):
    # convert the binary input into a list of strings
    number = list(str(number))
    ones = []
    # store the index of each 1 bit in the binary input in an array
    for i in range(len(number)):
        if number[i] == '1':
            ones.append(i)
    # check whether the number of ones is a multiple of 3 (if not the binary code
    # canno be split into 3 parts)
    if len(ones) % 3 != 0:
        return [-1, -1]

    # calculate the numer of 0s that follow the last 1 in each of the three parts
    trailingZeros = len(number) - int(ones[-1]) - 1
    part = len(ones) // 3

    # check if the first part has an adequate number of trailing zeros
    i = ones[part - 1] + 1
    end = i + trailingZeros
    for i in range(i, end):
        if number[i] != '0':
            return [-1, -1]

    # check if the second part has an adequate number of trailing zeros
    i = ones[2*part - 1] + 1
    end = i + trailingZeros
    for i in range(i, end):
        if number[i] != '0':
            return [-1, -1]

    # return the pivot points of part 1 and 2
    return [ones[part-1] + trailingZeros, ones[2*part - 1] + trailingZeros + 1]

check2("01010101001010")

# previous idea: recursive solution that would divide the binary code into
# 3 parts and check if their denary values were equal

def check2(number, target=None):
    number = str(number)
    for i in range(1, len(number)+1):
        part = number[:i]
        value = binaryDenary(part)
        rest = number[i:]
        if value == target or target is None:
            if rest == '':
                return True
            else:
                if check(rest, value):
                    print(part, rest)


def binaryDenary(binary):
    binary = str(binary)
    denary = 0
    for digit in binary:
        denary = denary*2 + int(digit)
    return denary
