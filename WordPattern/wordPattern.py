'''


This program Outputs the pattern of entered alphabets



'''




bg = '  '
br = '**'
A = [[bg for col in range(7)] for row in range(7)]
B = [[bg for col in range(7)] for row in range(7)]
C = [[bg for col in range(7)] for row in range(7)]
D = [[bg for col in range(7)] for row in range(7)]
E = [[bg for col in range(7)] for row in range(7)]
F = [[bg for col in range(7)] for row in range(7)]
G = [[bg for col in range(7)] for row in range(7)]
H = [[bg for col in range(7)] for row in range(7)]
I = [[bg for col in range(7)] for row in range(7)]
J = [[bg for col in range(7)] for row in range(7)]
K = [[bg for col in range(5)] for row in range(7)]
L = [[bg for col in range(7)] for row in range(7)]
M = [[bg for col in range(7)] for row in range(7)]
N = [[bg for col in range(7)] for row in range(7)]
O = [[bg for col in range(7)] for row in range(7)]
P = [[bg for col in range(7)] for row in range(7)]
Q = [[bg for col in range(8)] for row in range(8)]
R = [[bg for col in range(7)] for row in range(7)]
S = [[bg for col in range(7)] for row in range(7)]
T = [[bg for col in range(7)] for row in range(7)]
U = [[bg for col in range(7)] for row in range(7)]
V = [[bg for col in range(13)] for row in range(7)]
W = [[bg for col in range(7)] for row in range(7)]
X = [[bg for col in range(7)] for row in range(7)]
Y = [[bg for col in range(9)] for row in range(7)]
Z = [[bg for col in range(7)] for row in range(7)]
for row in range(7):
    for col in range(7):
        if ((col == 0 or col == 6) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 6)):
            A[row][col] = br
for row in range(7):
    for col in range(7):
        if (col == 0) or ((row == 0 or row == 3 or row == 6) and col != 6) or (col == 6 and (row != 0 and row != 3 and row != 6)):
            B[row][col] = br
for row in range(7):
    for col in range(7):
        if (col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and col != 0):
            C[row][col] = br
for row in range(7):
    for col in range(7):
        if col == 0 or ((row == 0 or row == 6) and col != 6) or (col == 6 and (row != 0 and row != 6)):
            D[row][col] = br
for row in range(7):
    for col in range(7):
        if col == 0 or row == 0 or row == 3 or row == 6:
            E[row][col] = br
for row in range(7):
    for col in range(7):
        if col == 0 or row == 0 or row == 3:
            F[row][col] = br
for row in range(7):
    for col in range(7):
        if (col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col != 0)) or (col == 6 and (row > 0 and row < 6 and row != 1 and row != 2) or (row == 3 and (col > 3 and col != 6))):
            G[row][col] = br
for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) or row == 3:
            H[row][col] = br
for row in range(7):
    for col in range(7):
        if row == 0 or row == 6 or col == 3:
            I[row][col] = br
for row in range(7):
    for col in range(7):
        if (row == 0 or col == 3) or (row == 6 and col < 3 and col != 0):
            J[row][col] = br
i = 0
j = 4
for row in range(7):
    for col in range(5):
        if col == 0 or row == col+2:
            K[row][col] = br
        elif row == i and col == j:
            K[row][col] = br
            i += 1
            j -= 1
for row in range(7):
    for col in range(7):
        if col == 0 or row == 6:
            L[row][col] = br
r = 1
c = 5
for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) or (col == row and row < 4):
            M[row][col] = br
        elif row == r and col == c and col > 3 and row < 3:
            M[row][col] = br
            r += 1
            c -= 1
for row in range(7):
    for col in range(7):
        if col == 0 or col == 6 or col == row:
            N[row][col] = br
for row in range(7):
    for col in range(7):
        if ((row == 0 or row == 6) and col != 0 and col != 6) or ((col == 0 or col == 6) and row != 0 and row != 6):
            O[row][col] = br
for row in range(7):
    for col in range(7):
        if ((col == 0 or row == 0 or row == 3) and col != 6) or (col == 6 and (row != 0 and row != 3 and row < 4)):
            P[row][col] = br
for row in range(8):
    for col in range(8):
        if ((row == 0 or row == 6) and (col != 0 and col != 6 and col < 6)) or ((col == 0 or col == 6) and (row != 0 and row != 6 and row < 6)) or ((col == row) and col > 3):
            Q[row][col] = br
for row in range(7):
    for col in range(7):
        if ((col == 0 or row == 0 or row == 3) and col != 6) or (col == 6 and row != 0 and row != 3 and row < 3) or row == col+2:
            R[row][col] = br
for row in range(7):
    for col in range(7):
        if ((row == 0 or row == 3 or row == 6) and col != 0 and col != 6) or (col == 0 and row < 3 and row != 0 and row != 3 and row != 6) or (col == 6 and row > 3 and row<6):
            S[row][col] = br
for row in range(7):
    for col in range(7):
        if row == 0 or col == 3:
            T[row][col] = br
for row in range(7):
    for col in range(7):
        if ((col == 0 or col == 6) and row != 6) or (row == 6 and (col != 0 and col != 6)):
            U[row][col] = br
c = 12
r = 0
for row in range(7):
    for col in range(13):
        if row == col:
            V[row][col] = br
        elif col == c and row == r and col > 3:
            V[row][col] = br
            c -= 1
            r += 1
r = 3
c = 3
for row in range(7):
    for col in range(7):
        if col == 0 or col == 6 or (col == 4 and row == 4) or (col == 5 and row == 5):
            W[row][col] = br
        elif row == r and col == c:
            W[row][col] = br
            r += 1
            c -= 1
for row in range(7):
    for col in range(7):
        if row == col or row + col == 6:
            X[row][col] = br
for row in range(7):
    for col in range(9):
        if (col == row and col < 5) or (col+row == 8 and row < 4) or (col == 4 and (row == 5 or row == 6 or row == 7)):
            Y[row][col] = br
for row in range(7):
    for col in range(7):
        if row == 0 or row == 6 or row+col == 6:
            Z[row][col] = br

d = dict(a=A, b=B, c=C, d=D, e=E, f=F, g=G, h=H, i=I, j=J, k=K, l=L, m=M, n=N, o=O, p=P, q=Q, r=R, s=S, t=T, u=U, v=V, w=W, x=X, y=Y, z=Z)
s = input('Enter a Word : ').lower()
for row in range(7):
    for c in s:
        if c == ' ':
            print(end='        ')
        if c in 'abcdefghijklmnopqrstuvwxyz':
            for col in range(len(d[c][row])):
                print(d[c][row][col], end='')
            print(end='  ')

    print()
