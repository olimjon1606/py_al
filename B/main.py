import time
import csv
import matplotlib.pyplot as plt

def binary_sunday(pattern, text):
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            return i
        i += (m - 1 - pattern.rfind(text[i + m - 1]))

    return -1

def gusfield_z(pattern, text):
    n = len(text)
    m = len(pattern)
    Z = [0] * n
    pattern_hash = hash(pattern)

    for i in range(1, n):
        if i <= m and text[i - 1] == pattern[i - 1]:
            Z[i] = 1
        elif i > m and text[i - 1 - m] == pattern[0]:
            Z[i] = 1

            if i - m < n - m:
                for j in range(1, m):
                    if text[i - m + j] == pattern[j]:
                        Z[i] += 1
                    else:
                        break

    for i in range(n - m + 1, n):
        if text[i] == pattern[i - n + m]:
            Z[i] += 1
        else:
            break

    for i in range(n):
        if Z[i] == m:
            return i - m

    return -1

def kmp(pattern, text):
    m = len(pattern)
    n = len(text)

    lps = [0] * m
    j = 0

    compute_lps_array(pattern, m, lps)

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                return i - j

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def compute_lps_array(pattern, m, lps):
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

def rabin_karp(pattern, text):
    prime = 101
    d = 256
    q = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(q - 1):
        h = (h * d) % prime

    for i in range(q):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(n - q + 1):
        if p == t:
            for j in range(q):
                if text[i + j] != pattern[j]:
                    break
            if j == q - 1:
                return i

        if i < n - q:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + q])) % prime
            if t < 0:
                t = t + prime

    return -1

# Test the algorithms and record execution times

pattern1 = "abcde"
text1 = "abcde" * 500000

pattern2 = "aaaaa"
text2 = "a" * 200000

pattern3 = "abcdefg"
text3 = "a" + "x" * 1000000  # x represents random characters

binary_sunday_time = []
gusfield_z_time = []
kmp_time = []
rabin_karp_time = []
rabin_karp_time2 = []
binary_sunday_time2 = []

for _ in range(5):
    start_time = time.time()
    binary_sunday(pattern1, text1)
    binary_sunday_time.append(time.time() - start_time)

    start_time = time.time()
    gusfield_z(pattern1, text1)
    gusfield_z_time.append(time.time() - start_time)

    start_time = time.time()
    kmp(pattern2, text2)
    kmp_time.append(time.time() - start_time)

    start_time = time.time()
    rabin_karp(pattern2, text2)
    rabin_karp_time.append(time.time() - start_time)

    start_time = time.time()
    rabin_karp(pattern3, text3)
    rabin_karp_time2.append(time.time() - start_time)

    start_time = time.time()
    binary_sunday(pattern3, text3)
    binary_sunday_time2.append(time.time() - start_time)

# Save the data in a CSV file

with open('algorithm_comparison.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Pattern', 'Text', 'Binary Sunday', 'Gusfield Z', 'KMP', 'Rabin-Karp'])

    for i in range(5):
        writer.writerow([pattern1, text1, binary_sunday_time[i], gusfield_z_time[i], "-", "-"])
        writer.writerow([pattern2, text2, "-", "-", kmp_time[i], rabin_karp_time[i]])
        writer.writerow([pattern3, text3, binary_sunday_time2[i], "-", "-", rabin_karp_time2[i]])

# Generate comparison graph

plt.plot(range(1, 6), binary_sunday_time, label='Binary Sunday (Pattern 1)')
plt.plot(range(1, 6), gusfield_z_time, label='Gusfield Z (Pattern 1)')
plt.plot(range(1, 6), kmp_time, label='KMP (Pattern 2)')
plt.plot(range(1, 6), rabin_karp_time, label='Rabin-Karp (Pattern 2)')
plt.plot(range(1, 6), binary_sunday_time2, label='Binary Sunday (Pattern 3)')
plt.plot(range(1, 6), rabin_karp_time2, label='Rabin-Karp (Pattern 3)')
plt.xlabel('Execution')
plt.ylabel('Time (s)')
plt.title('Algorithm Comparison')
plt.legend()
plt.savefig('algorithm_comparison.png')
plt.close()
