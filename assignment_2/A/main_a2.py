import time
import string
import csv
import matplotlib.pyplot as plt
from collections import defaultdict
from sortedcontainers import SortedSet


def load_word_list():
    with open('english_names.txt', 'r') as file:
        word_list = set(word.strip().lower() for word in file)
    return word_list


def build_linear_list(word_list):
    return list(word_list)


def build_bbst(word_list):
    bbst = SortedSet(word_list)
    return bbst


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


def build_trie(word_list):
    root = TrieNode()
    for word in word_list:
        current_node = root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True
    return root


def build_hash_map(word_list):
    hash_map = {word: True for word in word_list}
    return hash_map


def spell_check_linear_list(text, dictionary):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    misspelled = [word for word in words if word not in dictionary]
    return misspelled


def spell_check_bbst(text, dictionary):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    misspelled = [word for word in words if word not in dictionary]
    return misspelled


def spell_check_trie(text, dictionary, word_list):
    def dfs(node, prefix, misspelled):
        if node.is_word:
            if prefix not in word_list:
                misspelled.append(prefix)
        for char, child in node.children.items():
            dfs(child, prefix + char, misspelled)

    text = text.translate(str.maketrans('', '', string.punctuation))
    root = dictionary
    words = text.lower().split()
    misspelled = []
    for word in words:
        dfs(root, '', misspelled)
    return misspelled


def spell_check_hash_map(text, dictionary):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    misspelled = [word for word in words if word not in dictionary]
    return misspelled


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, result


def save_timing_data(timing_data):
    with open('timing_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Data Structure', 'Dictionary Building Time', 'Spell Checking Time'])
        for entry in timing_data:
            writer.writerow(entry)


def generate_graph(timing_data):
    structures = [entry[0] for entry in timing_data]
    build_times = [entry[1] for entry in timing_data]
    check_times = [entry[2] for entry in timing_data]

    plt.figure(figsize=(10, 6))
    plt.bar(structures, build_times, label='Dictionary Building Time')
    plt.bar(structures, check_times, label='Spell Checking Time')

    plt.xlabel('Data Structure')
    plt.ylabel('Time (seconds)')
    plt.title('Dictionary Building and Spell Checking Times')

    plt.legend()
    plt.tight_layout()
    plt.savefig('timing_graph.png')
    plt.show()


def main():
    # Load word list
    word_list = load_word_list()

    # Build data structures
    linear_list = build_linear_list(word_list)
    bbst = build_bbst(word_list)
    trie = build_trie(word_list)
    hash_map = build_hash_map(word_list)

    # Large piece of text for testing
    with open('text_test.txt', 'r') as file:
        large_text = file.read()

    # Measure timings
    timing_data = []

    linear_list_time, _ = measure_time(build_linear_list, word_list)
    timing_data.append(('Linear List', linear_list_time))

    bbst_time, _ = measure_time(build_bbst, word_list)
    timing_data.append(('BBST', bbst_time))

    trie_time, _ = measure_time(build_trie, word_list)
    timing_data.append(('Trie', trie_time))

    hash_map_time, _ = measure_time(build_hash_map, word_list)
    timing_data.append(('Hash Map', hash_map_time))

    linear_list_check_time, _ = measure_time(spell_check_linear_list, large_text, linear_list)
    timing_data[0] = timing_data[0] + (linear_list_check_time,)

    bbst_check_time, _ = measure_time(spell_check_bbst, large_text, bbst)
    timing_data[1] = timing_data[1] + (bbst_check_time,)

    trie_check_time, _ = measure_time(spell_check_trie, large_text, trie, word_list)
    timing_data[2] = timing_data[2] + (trie_check_time,)

    hash_map_check_time, _ = measure_time(spell_check_hash_map, large_text, hash_map)
    timing_data[3] = timing_data[3] + (hash_map_check_time,)

    # Save timing data
    save_timing_data(timing_data)

    # Generate graph
    generate_graph(timing_data)


if __name__ == '__main__':
    main()
