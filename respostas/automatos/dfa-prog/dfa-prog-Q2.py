dfa = {'A':{'b':'B'},
       'B':{'a':'B', 'b': 'D','c':'C'},
       'C':{'a':'B'},
       'D':{'b':'A'}}

def dfa_algorithm(delta, initial, accepting, text):
    boolean = False
    state = initial
    try:
        for c in text:
            state = delta[state][c]
        boolean = state in accepting 
    except:
        boolean = False
    if boolean:
        print("Aceito")
    else: 
        print("Rejeitado")

dfa_algorithm(dfa, 'B', {'C'}, input().lower())