import csv
import random
import string
import time
import pandas as pd
import matplotlib.pyplot as plt
from pattern_matching_algorithms import (
    brute_force,
    sunday,
    kmp,
    fsm,
    rabin_karp,
    gusfield_z
)

# Generate random text based on the pattern


def generate_text(pattern, length):
    text = []
    pattern_length = len(pattern)
    for _ in range(length):
        if random.random() < 0.1:
            text.append(random.choice(string.ascii_letters))
        else:
            text.append(random.choice(pattern))
    return ''.join(text)


# Measure running time of an algorithm in nanoseconds
def measure_running_time(algorithm, text, pattern):
    start_time = time.perf_counter_ns()
    algorithm(text, pattern)
    end_time = time.perf_counter_ns()
    running_time = (end_time - start_time) / 1e9  # Convert to seconds
    return running_time

# Run the pattern matching algorithms


def run_pattern_matching_algorithms(small_pattern, large_pattern):
    i = 1000
    text_lengths = [5*i, i*10, i*20, i*40, i*80,
                    i*160, i*320, i*640, i*1280, i*2560, i*5620]
    algorithms = [
        ("Brute-Force", brute_force),
        ("Sunday", sunday),
        ("KMP", kmp),
        ("FSM", fsm),
        ("Rabin-Karp", rabin_karp),
        ("Gusfield Z", gusfield_z)
    ]
    results = []

    for length in text_lengths:
        small_text = generate_text(small_pattern, length)
        large_text = generate_text(large_pattern, length)
        row = [length]
        for algorithm in algorithms:
            small_running_time = measure_running_time(
                algorithm[1], small_text, small_pattern)
            large_running_time = measure_running_time(
                algorithm[1], large_text, large_pattern)
            row.append(small_running_time)
            row.append(large_running_time)
        results.append(row)

    return results

# Save results to CSV file


def save_results_to_csv(results, algorithms):
    with open("pattern_matching_results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Text Length"] + [algorithm[0]
                        for algorithm in algorithms])
        writer.writerows(results)

# Plot graph
# Plot graph
# Plot graph and save as image
# Plot graph and save as image
# Plot graph and save as image


def plot_graph(results, algorithms, output_file):
    columns = ["Text Length"]
    for algorithm in algorithms:
        columns.append(algorithm[0] + " (Small)")
        columns.append(algorithm[0] + " (Large)")

    df = pd.DataFrame(results, columns=columns)
    plt.figure(figsize=(10, 6))

    for algorithm in algorithms:
        plt.plot(df["Text Length"], df[algorithm[0] + " (Small)"],
                 label=algorithm[0] + " (Small)")
        plt.plot(df["Text Length"], df[algorithm[0] + " (Large)"],
                 label=algorithm[0] + " (Large)")

    plt.xlabel("Text Length")
    plt.ylabel("Running Time (seconds)")
    plt.title("Running Time of Pattern Matching Algorithms")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_file)  # Save the graph as an image
    plt.show()


# Main function
def main():
    small_pattern = "Mom bought me a new computer"
    large_pattern = "I am very happy that my mom bought me a new computer for my birthday. It's an amazing gift!"
    results = run_pattern_matching_algorithms(small_pattern, large_pattern)

    algorithms = [
        ("Brute-Force", brute_force),
        ("Sunday", sunday),
        ("KMP", kmp),
        ("FSM", fsm),
        ("Rabin-Karp", rabin_karp),
        ("Gusfield Z", gusfield_z)
    ]
    save_results_to_csv(results, algorithms)

    plot_graph(results, algorithms, "time-data_graph.png")


if __name__ == "__main__":
    main()
