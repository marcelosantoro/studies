
# Variables and Const
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
even_sum = 0

odd = []
odd_sum = 0

def find_even_or_odd(kind):
    global even_sum
    global odd_sum
    for num in numeros:
        if(kind == "even"):
            if num % 2 == 0:
                even.append(num)
                even_sum = num + even_sum
        else:
            if num % 2 != 0:
                odd.append(num)
                odd_sum = num + odd_sum

if __name__ == "__main__":
    print("Even")
    find_even_or_odd("even")
    print(even)
    print(f"Sum of Even: {even_sum}")

    print("##############################")

    print("Odd")
    find_even_or_odd("odd")
    print(odd)
    print(f"Sum of Odd: {odd_sum}")
