def first_non_repeating_char(string):
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1

    for char in string:
        if char_freq[char] == 1:
            return char

    return None

print(first_non_repeating_char('leetcode'))
print(first_non_repeating_char('hello'))
print(first_non_repeating_char('aabbcc'))
