def brute_force_match(text, pattern):
    n = len(text)
    m = len(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if pattern[j] == '?' or pattern[j] == text[i]:
            i += 1
            j += 1
        elif pattern[j] == '*':
            j += 1
            if j == m:  # wildcard '*' at the end of the pattern matches the remaining text
                return True
            while i < n:
                if brute_force_match(text[i:], pattern[j:]):
                    return True
                i += 1
        else:
            return False

    if j == m:
        return True

    return False


def sunday_match(text, pattern):
    n = len(text)
    m = len(pattern)
    i = 0  # index for text

    while i <= n - m:
        j = 0  # index for pattern
        while j < m and (pattern[j] == '?' or pattern[j] == text[i + j]):
            j += 1

        if j == m:
            return True

        if i + m == n:
            return False

        # Find the next character in text after the mismatch
        next_char = text[i + m]
        shift = m + 1

        for k in range(m - 1, -1, -1):
            if pattern[k] == next_char:
                shift = m - k
                break

        i += shift

    return False


# Test the implementations
text = "Hello World"
pattern = "He?lo*"
escaped_pattern = "He\\?lo\\*"

print("Brute-Force:")
print(brute_force_match(text, pattern))  # True
print(brute_force_match(text, escaped_pattern))  # False

print("\nSunday:")
print(sunday_match(text, pattern))  # True
print(sunday_match(text, escaped_pattern))  # False
