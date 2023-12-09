def most_frequent_character(input_string):
    # Create a dictionary to store the frequency of each character
    char_frequency = {}

    # Count the frequency of each character in the string
    for char in input_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Find the character with the maximum frequency
    most_frequent_char = max(char_frequency, key=char_frequency.get)

    return most_frequent_char

# Example usage
user_input = input("Enter a string: ")
result = most_frequent_character(user_input)

print(f"The most frequent character is: {result}")