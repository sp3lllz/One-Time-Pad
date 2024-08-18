import sys

def text_to_ascii(text):
    # Convert text to a string of ASCII values
    ascii_values = ''.join(str(ord(char)) for char in text)
    return ascii_values

def modulo_addition_per_digit(num_str1, num_str2, modulo):
    # Ensure both strings have the same length
    if len(num_str1) != len(num_str2):
        raise ValueError("Both strings must have the same length.")
    
    result = ""
    # Perform modulo addition on each digit
    for digit1, digit2 in zip(num_str1, num_str2):
        sum_digits = (int(digit1) + int(digit2)) % modulo
        result += str(sum_digits)
    
    return result

if __name__ == "__main__":
    # Take the first command-line argument as the text input
    user_input = sys.argv[1]
    
    # Convert the input text to ASCII values
    ascii_output = text_to_ascii(user_input)
    
    # Count the number of digits in the ASCII string
    num_digits = len(ascii_output)
    print(f"The ASCII representation of '{user_input}' is: {ascii_output}")
    print(f"It contains {num_digits} digits.")

    # Prompt the user to input a string of the same length
    while True:
        num_str2 = input(f"Please enter a string of {num_digits} digits: ")
        if len(num_str2) == num_digits:
            break
        print(f"Error: The input must be exactly {num_digits} digits long.")

    # Modulo value for individual digits (can be customized)
    modulo = 10

    # Perform modulo addition per digit
    result = modulo_addition_per_digit(ascii_output, num_str2, modulo)

    # Output the final result
    print(f"The result of the modulo addition is: {result}")
