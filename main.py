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
    # Implementation code

# Measure running time of an algorithm
def measure_running_time(algorithm, text, pattern):
    # Implementation code

# Run the pattern matching algorithms
def run_pattern_matching_algorithms():
    pattern = "Mom bought me a new computer"
    text_lengths = [10**3, 10**4, 10**5, 10**6]
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
        text = generate_text(pattern, length)
        row = [length]
        for algorithm in algorithms:
            running_time = measure_running_time(algorithm[1], text, pattern)
            row.append(running_time)
        results.append(row)

    return results

# Save results to CSV file
def save_results_to_csv(results):
    with open("pattern_matching_results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Text Length"] + [algorithm[0] for algorithm in algorithms])
        writer.writerows(results)

# Plot graph
def plot_graph(results):
    df = pd.DataFrame(results, columns=["Text Length"] + [algorithm[0] for algorithm in algorithms])
    plt.figure(figsize=(10, 6))
    for algorithm in algorithms:
        plt.plot(df["Text Length"], df[algorithm[0]], label=algorithm[0])
    plt.xlabel("Text Length")
    plt.ylabel("Running Time (seconds)")
    plt.title("Running Time of Pattern Matching Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
def main():
    results = run_pattern_matching_algorithms()
    save_results_to_csv(results)
    plot_graph(results)

if __name__ == "__main__":
    main()
