def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)

    return occurrences


def sunday(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    skip = [m] * 256
    for i in range(m):
        skip[ord(pattern[i])] = m - i

    i = 0
    while i <= n - m:
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)
        if i + m < n:
            i += skip[ord(text[i + m])]
        else:
            break

    return occurrences


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    lps = [0] * m
    compute_lps(pattern, m, lps)

    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences


def compute_lps(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def fsm(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    transition = compute_transition_function(pattern)

    state = 0
    for i in range(n):
        state = transition[state][ord(text[i])]
        if state == m:
            occurrences.append(i - m + 1)

    return occurrences


def compute_transition_function(pattern):
    m = len(pattern)
    transition = [[0] * 256 for _ in range(m + 1)]

    for state in range(m + 1):
        for char in range(256):
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[next_state - 1] != char:
                next_state = transition[next_state - 1][char]
            transition[state][char] = next_state

    return transition


def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    prime = 101
    pat_hash = 0
    txt_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * 256) % prime

    for i in range(m):
        pat_hash = (256 * pat_hash + ord(pattern[i])) % prime
        txt_hash = (256 * txt_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pat_hash == txt_hash:
            j = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                occurrences.append(i)
        if i < n - m:
            txt_hash = (
                256 * (txt_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if txt_hash < 0:
                txt_hash += prime

    return occurrences


def gusfield_z(text, pattern):
    # Implementation code
    def gusfield_z(text, pattern):
        concat = pattern + "$" + text
        n = len(concat)
        m = len(pattern)
        occurrences = []

        z = compute_z_array(concat)

        for i in range(n):
            if z[i] == m:
                occurrences.append(i - m - 1)

        return occurrences

    def compute_z_array(string):
        n = len(string)
        z = [0] * n

        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and string[z[i]] == string[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1

        return z
