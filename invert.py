A = [[1, 0, 0], [0, 1, 0], [0, 2, 2]]


# the worst way to calculate that i assure you
def rank(mat):
    for i in range(len(mat)):
        for k in range(i):
            for j in range(i):
                if mat[i][j] and mat[k][j]:
                    mat = rank_line(mat, k, i, (mat[i][j]/mat[k][j]))
                    mat = normalize_line(mat, i)
                    break

    return mat


def line_calc(line1, line2, scale):
    return [line2[i] - scale * line1[i] for i in range(len(line1))]

def rank_line(mat, l1, l2, scalar):
    return [mat[i] if i != l2 else line_calc(mat[l1], mat[l2], scalar) for i in range(len(mat))]

def print_mat(mat):
    for i in mat:
        print(i)

def canon_rank(mat):
    print_mat(rank(mat))
    print_mat(rank(transpose(rank(mat))))
    print_mat(mat)

def transpose(mat):
    matA_vals=mat
    matA_vals=[[mat[i][j] for i in range(len(mat))] for j in range(len(mat))]
    return matA_vals

def normalize_line(mat, l):
    if mat[l][l]:
        mat[l] = [mat[l][i]/mat[l][l] for i in range(len(mat))]
    return mat

def normalize_by(mat, l, i):
    if i:
        mat[l]=[mat[l][j]/i for j in range(len(mat[l]))]
    return mat


# now for the dumb shit you all came here for:
def invert(mat):
    inverse = [[1 if i ==j else 0 for j in range(len(mat))] for i in range(len(mat))]
    for i in range(len(mat)):
        for k in range(i):
            for j in range(i):
                if mat[i][j] and mat[k][j]:
                    inverse = rank_line(inverse, k, i, (mat[i][j] / mat[k][j]))
                    mat = rank_line(mat, k, i, (mat[i][j]/mat[k][j]))
                    inverse = normalize_by(inverse, i, mat[i][i])
                    mat = normalize_by(mat, i, mat[i][i])
                    break

    print_mat(inverse)
    mat = transpose(mat)
    inverse = transpose(inverse)
    for i in range(len(mat)):
        for k in range(i):
            for j in range(i):
                if mat[i][j] and mat[k][j]:
                    inverse = rank_line(inverse, k, i, (mat[i][j] / mat[k][j]))
                    mat = rank_line(mat, k, i, (mat[i][j] / mat[k][j]))
                    inverse = normalize_by(inverse, i, mat[i][i])
                    mat = normalize_by(mat, i, mat[i][i])
                    break


    return transpose(inverse)
#the problem is this is too stupid to work yet not stupid enough
# I have single-handedly created the W O R S T inversing algorithm
# I should have been struck down by the heavens for merely attempting to do it like this


#rank(A)

# print(line_calc(A[1], A[2], 1))
# canon_rank(A)
print_mat(A)
print_mat(invert(A))
# print_mat(transpose(rank(A)))
