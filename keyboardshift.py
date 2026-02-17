#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

#sys.stdin = open('keyboard_input2.txt' )
sys.stdout = open('output.txt', 'w')

# input data
N = int(input().strip())
S = input().strip()


# insert your code here
Riga1= "qwertyuiop"
Riga2 = "asdfghjkl"
Riga3 = "zxcvbnm"

tasto={}
def aggiungi_tasti(tasto, righe):
    for i in range(0,len(righe)-1):
        cliccato=righe[i]
        corretto=righe[i+1]
        tasto[cliccato]=corretto

aggiungi_tasti(tasto,Riga1) 
aggiungi_tasti(tasto,Riga2) 
aggiungi_tasti(tasto,Riga3) 
Stringa=""
for i in range(0,len(S)):
    errato=S[i]
    corretto=tasto[errato]
    Stringa+=corretto



print(Stringa)  # print the result