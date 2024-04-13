import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def find_minas(matrix):
    new_matrix = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            counter = 0
            if matrix[i][j] == "#":
                row.append("#")
                continue
            for x in range(max(0, i - 1), min(len(matrix), i + 2)):
                for y in range(max(0, j - 1), min(len(matrix[i]), j + 2)):
                    if matrix[x][y] == "#":
                        counter += 1
            row.append(str(counter))
        new_matrix.append(row)

    return new_matrix


if __name__ == "__main__":
    N = int(input())
    matrix = []

    for _ in range(N):
        line = input().split("   ")
        matrix.append(line)

    new_matrix = find_minas(matrix)

    for row in new_matrix:
        print("   ".join(row))
