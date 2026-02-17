# NOTE: it is recommended to use this even if you don't understand the following code.
import sys
sys.stdin = open('isogram_input0.txt', 'r')
sys.stdout = open('output.txt', 'w')

# input data
N = int(input().strip())
risposta = 0 

for i in range(N):
    S = input().strip()

    # insert your code here
    pulita= ""
    for i in range(len(S)):
        if S[i].isalpha():
            clean += S[i]

pulita = pulita.lower()

isogram = True
contatori = {}
for c in clean:
    if c not in pulita:
        contatori[c] = 1
    else:
        contatori[c] += 1
    if contatori[c] > 2:
        isogram = False
        break
if isogram:
    risposta += 1



print(risposta)  # print the result