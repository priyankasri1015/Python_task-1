def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()


    return sorted(str1) == sorted(str2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = are_anagrams(string1, string2)

if result:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
# Try it with listen & silent ans should be "the stings are Anagram"
