def remove_vowels(input_string):
 vowels="AEIOUaeiou"
 result= ""
 for char in input_string:
     if char not in vowels:
         result += char
 return result

user_input = input("Enter a string: ")
result = remove_vowels(user_input)
print("String without vowels:", result)

