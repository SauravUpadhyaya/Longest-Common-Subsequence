# Project:  CS 617
# Program:  Longest Common Subsequence (LCS)
# Purpose:  Find LCS of two sequences of symbols using dynamic programming
# Author:   Saurav Upadhyaya
# Source:   - T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein,
#             Introduction to Algorithms, Third Edition, The MIT Press, Cambridge MA, 2009
#           - M. Petty, Dynamic Programming, Lecture 15, 2022
# Created:  2022-03-12
# Modified: 2022-03-13

# global output variable for concatenating longest common subsequence for each pair of input
output = ""
# Set input and output file
input_file = "test_cases.txt"
output_file = open('output_file.txt', 'w')

# Find LCS length by filling in tables B and C as in lecture psuedocode
def lcs_length(x, y, m, n):         # Length of two strings have been passed as a parameter and initialized in main to avoid repetition in two functions
    B = [[0 for col in range(n)] for row in range(m)]         # Updated for 0-based indexing       
    C = [[0 for col in range(n+1)] for row in range(m+1)]     # Updated for 0-based indexing
    for i in range(m):                                        # Updated for 0-based indexing
        C[i][0] = 0
    for j in range(n):                                        # Updated for 0-based indexing
        C[0][j] = 0
    for i in range(0, m):                                     # Updated for 0-based indexing
        for j in range(0, n):
            if x[i] == y[j]:
                C[i+1][j+1] = C[i-1+1][j-1+1]+1               # Referenced from R code sample in lecture slide
                B[i][j] = "UPLEFT"
            elif C[i-1+1][j+1] >= C[i+1][j-1+1]:
                C[i+1][j+1] = C[i-1+1][j+1]
                B[i][j] = "UP"
            else:
                C[i+1][j+1] = C[i+1][j-1+1]
                B[i][j] = "LEFT"
    return B, C

# Print the longest common subsequence using table B
# Based on PRINT-LCS pseudocode, [Cormen, 2009] p. 395.
def print_lcs(B, X, i, j):
    global output
    if i < 0 or j < 0:                                      # Updated for 0-based indexing
        return
    if B[i][j] == "UPLEFT":
        print_lcs(B, X, i-1, j-1)
        output += X[i].replace("\n", "").replace("\s", "")
    elif B[i][j] == "UP":
        print_lcs(B, X, i-1, j)
    else:
        print_lcs(B, X, i, j-1)
    return output

# Writes to the output file
def write_to_out_file(string):
    global output_file
    output_file.write(string)

# Reads each sequences line by line contained in the input file and write LCS to the provided output file
def find_lcs_for_sequences(filename): 
    with open(filename, 'r') as test_file:
        for file_line in test_file:
            line = file_line.rstrip('\n').split(", ") # Converts each line into a list containing a pair of sequence
            X = line[0]
            Y = line[1]
            m = len(X)
            n = len(Y)
            B, C = lcs_length(X, Y, m, n)
         
            write_to_out_file(print_lcs(B, X, m-1, n-1) + '\n')   # Updated for 0-based indexing
            global output
            output = ""

if __name__ == "__main__":
    find_lcs_for_sequences(input_file)    # Reads the input file
