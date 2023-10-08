def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the Pascal's Triangle with the first row (row 0).
    triangle = [[1]]

    for i in range(1, n):
        # Initialize the current row with the first element as 1.
        current_row = [1]

        # Calculate the values for the current row based on the previous row.
        for j in range(1, i):
            current_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Add the last element of 1 to the current row.
        current_row.append(1)

        # Append the current row to the triangle.
        triangle.append(current_row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)

