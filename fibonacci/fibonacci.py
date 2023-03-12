
def fibonacci_sequence(num_terms, min_1, min_2):
    """
    Generates the Fibonacci sequence up to a specified number of terms.
    
    Parameters:
        num_terms (int): The number of terms to generate.
        
    Returns:
        list: A list containing the Fibonacci sequence up to the specified number of terms.
    """
    sequence = [min_1, min_2]
    while len(sequence) < num_terms:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence


if __name__ == "__main__":
    # Variables
    num_terms = 10
    min_1 = 0
    min_2 = 1
    print(fibonacci_sequence(num_terms, min_1, min_2))