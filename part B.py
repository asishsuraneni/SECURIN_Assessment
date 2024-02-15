def undoom_dice(die_a, die_b):
    # Initialize new dice lists
    new_die_a = [0] * 6
    new_die_b = [0] * 6
    
    # Calculate the probability of each sum with the original dice
    original_probabilities = {}
    for a in die_a:
        for b in die_b:
            total = a + b
            original_probabilities[total] = original_probabilities.get(total, 0) + 1
    
    # Calculate the total number of combinations with the original dice
    total_combinations = sum(original_probabilities.values())
    
    # Calculate the probability of each sum with the new dice
    new_probabilities = {}
    for a in die_a:
        for b in die_b:
            total = a + b
            new_probabilities[total] = new_probabilities.get(total, 0) + 1
    
    # Adjust the number of spots on Die B to maintain the same probabilities
    for total, count in original_probabilities.items():
        new_probabilities[total] = count / total_combinations
    
    # Reassign spots on Die A while respecting the constraint
    for i, a in enumerate(die_a):
        new_die_a[i] = min(4, a)
    
    # Reassign spots on Die B while allowing more than 6 spots
    for i, b in enumerate(die_b):
        # Calculate the difference between the original and new probabilities for the current sum
        diff = new_probabilities[total] - original_probabilities[total]
        # Adjust the spots on Die B based on the difference
        new_die_b[i] = b + int(diff * total_combinations)
    
    return new_die_a, new_die_b

# Input dice
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

# Undoom the dice
new_die_a, new_die_b = undoom_dice(die_a, die_b)

# Output the new dice
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)
