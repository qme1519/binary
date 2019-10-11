def check(number, target=None):
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


def check2(number):
    number = list(str(number))
    ones = []
    for i in range(len(number)):
        if number[i] == '1':
            ones.append(i)
    if len(ones) % 3 != 0:
        print("not 3")
        return [-1, -1]
    trailingZeros = len(number) - int(ones[-1]) - 1
    part = len(ones) // 3
    i = ones[part - 1] + 1
    end = i + trailingZeros
    for i in range(i, end):
        if number[i] != '0':
            print("trailing1")
            return [-1, -1]
    i = ones[2*part - 1] + 1
    end = i + trailingZeros
    for i in range(i, end):
        if number[i] != '0':
            print("trailing2")
            return [-1, -1]
    return [ones[part-1] + trailingZeros, ones[2*part - 1] + trailingZeros + 1]

check2("01010101001010")
