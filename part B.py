def undoom_dice(Die_A, Die_B):
    # Calculate the probabilities of each sum for the original dice (Die_A)
    original_probs = {}
    for i in range(1, 7):
        for j in range(1, 7):
            total = i + j
            original_probs[total] = original_probs.get(total, 0) + 1

    # Calculate the probabilities of each sum for the new dice (Die_B)
    new_probs = {}
    for i in range(1, 7):
        for j in range(1, 7):
            total = i + j
            new_probs[total] = new_probs.get(total, 0) + 1

    # Determine the scaling factor to adjust probabilities
    scaling_factor = sum(original_probs.values()) / sum(new_probs.values())

    # Create the new dice (Die_B) with adjusted probabilities
    New_Die_B = []
    for i in range(1, 7):
        for j in range(1, 7):
            total = i + j
            count = int(new_probs[total] * scaling_factor)
            New_Die_B.extend([i] * count)

    # Create the new dice (Die_A) with spots not exceeding 4
    New_Die_A = [min(4, x) for x in Die_A]

    return New_Die_A, New_Die_B

# Example usage:
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
