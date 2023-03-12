# Variable
word_check="Taco cat"

def is_palindrome(text):
    text = text.lower().replace(' ', '')
    return text == text[::-1]

if __name__ == "__main__":
    if is_palindrome(word_check):
        print("The input is a palindrome!")
    else:
        print("The input is not a palindrome.")