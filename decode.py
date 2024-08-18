import sys

def modulo_subtraction_per_digit(num_str1, num_str2):
    # Ensure both strings have the same length
    if len(num_str1) != len(num_str2):
        raise ValueError("Both strings must have the same length.")
    
    modulo = 10
    result = ""
    # Perform modulo subtraction on each digit
    for digit1, digit2 in zip(num_str1, num_str2):
        diff_digits = (int(digit1) - int(digit2)) % modulo
        result += str(diff_digits)
    
    return result

def numbers_to_letters(num_str):
    # Split the number string into chunks of 3 digits (ASCII values)
    ascii_values = [num_str[i:i+3] for i in range(0, len(num_str), 3)]
    
    # Convert each ASCII value to its corresponding character
    letters = ''.join(chr(int(value)) for value in ascii_values if int(value) >= 32 and int(value) <= 126)
    
    return letters

if __name__ == "__main__":
    # Ensure there are exactly 2 command-line arguments and one modulo (fixed to 10)
    if len(sys.argv) != 3:
        print("Usage: python combined_script.py <number_string1> <number_string2>")
        sys.exit(1)
    
    num_str1 = sys.argv[1]  # First number string
    num_str2 = sys.argv[2]  # Second number string

    # Perform modulo subtraction per digit
    try:
        subtraction_result = modulo_subtraction_per_digit(num_str1, num_str2)
        print(f"Modulo subtraction result: {subtraction_result}")
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Convert the result of modulo subtraction into letters
    letter_result = numbers_to_letters(subtraction_result)
    print(f"The resulting string is: {letter_result}")
