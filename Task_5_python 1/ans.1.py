def count_vowels(s):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    total_vowels = 0
    for char in s.lower():
        if char in vowels:
            vowels[char] += 1
            total_vowels += 1
    return total_vowels, vowels


input_string = "guvi geeks network private limited"
total_vowels, individual_vowels = count_vowels(input_string)

print("total count of letters in a word is :",len(input_string))
print("total number of vowels:", total_vowels)
print("individual vowel counts:", individual_vowels)


