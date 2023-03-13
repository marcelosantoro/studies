def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        # if the dimensions of the two matrices are not equal, return None
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            # add the corresponding elements of the two matrices
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

if __name__ == "__main__":
    # define two matrices
    matrix1 = [[1, 2, 3], [3, 4, 5]]
    matrix2 = [[5, 6, 3], [7, 8, 9]]

    # call the add_matrices function and store the result in a variable
    result = add_matrices(matrix1, matrix2)

    # print the result
    print(result)