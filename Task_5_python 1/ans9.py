def count_words(input_string):
    # Split the string into words using whitespace as the delimiter
    words = input_string.split()

    # Return the number of words
    return len(words)

# Example usage
user_input = input("Enter a string: ")
result = count_words(user_input)

print(f"The number of words in the string is: {result}")