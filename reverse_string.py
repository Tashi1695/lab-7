def reverse_string(s):
    # Base case: if the string is empty or contains only one character
    if len(s) <= 1:
        return s
    else:
        # Recursive case: reverse the remaining string and append the first character to the end
        return reverse_string(s[1:]) + s[0]

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python"))  # Output: "nohtyp"
print(reverse_string(""))        # Output: ""
