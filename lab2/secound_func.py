"""write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is is divisible by both return " FizzBuzz"""

def sec_func(myint :int):
    if myint %3 ==0 and myint % 5==0:
        return " FizzBuzz"
    elif myint % 3 ==0 :
        return "FIZZ"
    elif myint % 5 ==0:
        return "BUZZ"

print(sec_func(15))