def count_vowels(string):
    vowels = "aeiou"  
    num_vowels = 0  # vowel counter
    
    # loop through the string
    for letter in string:
        if letter in vowels:
            num_vowels += 1
            
    return num_vowels

if __name__ == "__main__":
    string = "AEiOu"
    num_vowels = count_vowels(string.lower())
    print("Number of vowels in string: ", num_vowels)