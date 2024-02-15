def calculate_probabilities():
    total_combinations = 36
    probabilities = [0] * 11  # Sums range from 2 to 12

    for i in range(1, 7):
        for j in range(1, 7):
            sum_value = i + j
            probabilities[sum_value - 2] += 1

    for sum_value in range(2, 13):
        print(f"P(Sum = {sum_value}) = {probabilities[sum_value - 2]}/{total_combinations}")

if __name__ == "__main__":
    calculate_probabilities()
