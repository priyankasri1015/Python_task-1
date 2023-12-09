def is_palindrome(input_string):
    input_string = input_string.lower()  # Convert the input string to lowercase
    return input_string == input_string[::-1]


user_input = input("enter the string :")
result = is_palindrome(user_input)
if result:
    print("The string is a palindrome")
else:
    print("The string is not a pallindrome")
# print(is_palindrome(string1))  # Output: True
# print(is_palindrome(string2))  # Output: False