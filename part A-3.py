# Initialize dictionary to store probabilities
probabilities = {}

# Calculate probability for each sum
for die_a in range(1, 7):
    for die_b in range(1, 7):
        total = die_a + die_b
        if total not in probabilities:
            probabilities[total] = 1
        else:
            probabilities[total] += 1

# Normalize probabilities by dividing by total combinations
total_combinations = 6 * 6
for key in probabilities:
    probabilities[key] /= total_combinations

# Print probabilities
print("Probability of each possible sum:")
for key, value in probabilities.items():
    print(f"P(Sum = {key}) = {value:.2f}")
