# Brute Force Programming of LCS problem

import time


def lcs_bf(X, Y, a, b):
    # find the length of the strings
    if a == 0 or b == 0:
        return 0
    elif X[a - 1] == Y[b - 1]:
        return 1 + lcs_bf(X, Y, a - 1, b - 1)
    else:
        return max(lcs_bf(X, Y, a, b - 1), lcs_bf(X, Y, a - 1, b))


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
    a = len(X)
    b = len(Y)
    print("----------------------------------------------")
    print("The String is " + X + " and " + Y)
    begin = time.process_time()
    length_lcs = lcs_bf(X, Y, a, b)
    print("Length of LCS is >>", length_lcs)
    end = time.process_time()
    print(f"Total runtime of the program is >> {end - begin} sec")
