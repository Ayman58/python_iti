"""Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is ' abdulrahman ' then the output Longest substring in
alphabetical order is: abdu"""

def myfifth_fun(mystr):
    result = ''
    temporary_result = ''
    if mystr == '':
        return "empty string "
    else:
        temporary_result = mystr[0]
    for i in range(len(mystr) - 1):
        if mystr[i].lower() <= mystr[i + 1].lower():
            temporary_result += mystr[i + 1]
        else:
            if len(temporary_result) > len(result):
                result = temporary_result
            temporary_result = mystr[i + 1]
    if len(result) == 0 or len(temporary_result) > len(result):
        result = temporary_result
    return result



print(myfifth_fun("abdulrahman"))