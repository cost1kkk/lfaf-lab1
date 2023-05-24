# Importing necessary classes from modules
from Grammar import RegularGrammar
#from finiteautomata import FiniteAutomata
# Defining a dictionary representing a context-free grammar
p = {
    'S' : ['aB', 'bA' , 'A'],
    'A' : ['B', 'AS', 'bBAB' , 'b'],
    'B' : ['b', 'bS', 'aD', ''],
    'C' : ['Ba'],
    'D' : ['AA']
}

# Defining the non-terminals and terminals of the grammar
vn = ['S', 'A', 'B', 'C', 'D']
vt = ['a', 'b']
a = vt

# Creating a RegularGrammar object with the specified parameters
new_grammar = RegularGrammar(vn, vt, p, a)

# Converting the grammar into Chomsky Normal Form and storing it in a new object
cnf_form = new_grammar.ConvertCNF()

# Iterating over the dictionary of productions in the CNF form and printing them out
for key in cnf_form.p:
    print(f'{key} : {cnf_form.p[key]}')