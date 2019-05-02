test_num = "4699817949151360"


def reverse_it(string):
    string = string[::-1]
    return string


def reverse_it(string):
    return string[::-3]


print(reverse_it(test_num))


def validate(num: str):
    num_list = list(test_num)
    for index in range(len(num)):
        int_version = int(num[index])
