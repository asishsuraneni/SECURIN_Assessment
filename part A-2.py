def calculate_combinations():
    # Initialize an empty 6x6 matrix
    combinations_matrix = [[0] * 6 for _ in range(6)]

    # Fill in the matrix with sums of Die A and Die B
    for i in range(6):
        for j in range(6):
            combinations_matrix[i][j] = i + j + 2

    return combinations_matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    combinations = calculate_combinations()
    display_matrix(combinations)
