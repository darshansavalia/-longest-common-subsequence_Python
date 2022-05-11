import time

import pandas as pd

#lcs of length
def lcs_dp_cb(X, Y):
    m = len(X)
    n = len(Y)

    c = [[0 for p in range(n + 1)] for q in range(m + 1)]
    b = [[0 for p in range(n + 1)] for q in range(m + 1)]

    for i in range(1, m + 1):
        c[i][0] = 0
    for i in range(0, n + 1):
        c[0][i] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "\\"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "^"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "<"

    lenth_lcs = c[m][n]
    return list(c), list(b), lenth_lcs

#print lcs of given string
def print_lcs_cb(P, Q, m, n):
    concatenate = ""
    if m == 0 or n == 0:
        return
    elif P[m][n] == "\\":
        concatenate += str(Q[m - 1])
        print_lcs_cb(P, Q, m - 1, n - 1)
    elif P[m][n] == "^":
        print_lcs_cb(P, Q, m - 1, n)
    else:
        print_lcs_cb(P, Q, m, n - 1)
    print(concatenate,end='')


text_file = open("LCS2.txt", "r")

for file in text_file:
    substring = file.split(",")

    X = substring[0]
    Y = substring[1]
    Q = list(X)

    m = len(X)
    n = len(Y)
    c, b, lenth_lcs = lcs_dp_cb(X, Y)

    D = [[str(x) for x in l] for l in c]
    S = [[str(x) for x in l] for l in b]

    #The zip() function returns a zip object for iterator and paired together
    final_output = []
    for sub_list1, sub_list2 in zip(D[1:], S[1:]):
        final_output.append([p + q for q, p in zip(sub_list1[1:], sub_list2[1:])])

    final_output.insert(0, ['0' for i in range(len(S[0]) - 1)])

    for sd in final_output:
        sd.insert(0, '0')

    str_word1 = 'X' + substring[0]
    str_word2 = 'Y' + substring[1]

    str1_file = list(str_word1)
    str2_file = list(str_word2)

    # dataframe for inset tabular of rows and columns index
    df = pd.DataFrame(final_output, columns=str2_file, index=str1_file)
    if "\n" in df.columns:
        df.drop("\n", axis=1, inplace=True)

    #begin = time.process_time()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(">>>X=", X, ",", "Y=", Y)
    print(df)
    print("\n>>>Length of the Longest Common Subsequence is:", lenth_lcs)
    print(">>>The LCS of given String ",'\033[1m' + X.strip() + '\033[0m', " and ", '\033[1m' + Y.strip() + '\033[0m',end=' is: ')
    print_lcs_cb(S, Q, m, n)
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #end = time.process_time()
    #print(f"\n>>>Total runtime of the program is >> {end - begin} sec")
