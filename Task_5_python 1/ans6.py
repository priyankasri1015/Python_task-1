def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store lengths of the common suffixes
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Variable to store the length of the longest common substring
    max_length = 0

    # Variable to store the ending index of the longest common substring
    end_index = 0

    # Fill the table and find the longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index = i - 1
            else:
                table[i][j] = 0

    # Extract the longest common substring
    longest_common_sub = str1[end_index - max_length + 1:end_index + 1]

    return longest_common_sub


# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = longest_common_substring(string1, string2)

if result:
    print(f"The longest common substring is: {result}")
else:
    print("There is no common substring.")