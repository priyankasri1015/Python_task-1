def count_unique_characters(input_string):
    unique_characters = set(input_string)
    return len(unique_characters)

user_input = input("Enter a string: ")
result = count_unique_characters(user_input)
print("Number of unique characters:", result)