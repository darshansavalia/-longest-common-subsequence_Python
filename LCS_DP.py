# Dynamic Programming of LCS problem

import time


def lcs_dp(X, Y):
    # find the length of the strings

    a = len(X)
    b = len(Y)
    L = [[None] * (b + 1) for i in range(a + 1)]

    for i in range(a + 1):
        for j in range(b + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[a][b]


text_file = open("LCS1.txt", "r")
data = text_file.read()
contents_split = data.splitlines()
text_file.close()

print("The String Is >>", contents_split)
arraylength = len(contents_split)

for i in range(arraylength):
    substringg = contents_split[i].split(",")
    X = substringg[0]
    Y = substringg[1]
    print("----------------------------------------------")
    print("The String is " + X + " and " + Y)
    begin = time.process_time()
    print("Length of LCS is >> ", lcs_dp(X, Y))
    end = time.process_time()
    print(f"Total runtime of the program is >> {end - begin} sec")
