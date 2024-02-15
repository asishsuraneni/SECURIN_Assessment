# Initialize a 6x6 matrix to store the distribution
distribution = [[0] * 6 for _ in range(6)]

# Calculate the distribution
for die_a in range(1, 7):
    for die_b in range(1, 7):
        total = die_a + die_b
        distribution[die_a - 1][die_b - 1] += 1

# Print the distribution matrix
print("Distribution of all possible combinations:")
for row in distribution:
    print(row)
