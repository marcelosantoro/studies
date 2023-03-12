def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        return f"FizzBuzz: {num}"
    elif num % 3 == 0:
        return f"Fizz: {num}"
    elif num % 5 == 0:
        return f"Buzz: {num}"
    else:
        return None

if __name__ == "__main__":
    nums = [1,3,33,45,50,67,49,105,525]
    for i in nums:
        ret = fizz_buzz(i)
        if ret is not None:
            print(ret)