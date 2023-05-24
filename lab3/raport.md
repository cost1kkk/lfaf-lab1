
# Intro to formal languages. Regular grammars. Finite Automata.
### Course: Formal Languages & Finite Automata
### Author: Baxanean Constantin FAF213
### Variant: 4
## Theory
Def: 
Lexical Analysis and Scanners: for the purposes of this laboratory, lexical analysis means the transformation of a sequence of characters into a series of lexical tokens. The program/algorithm that does this is called the lexer (or scanner), and it is the main character of this here laboratory.

## Screenshots
![Results](/lab3/img2.png "Results")

## Implementation description

The class new 'Lexer' was created, that opens a text file where the code in the given language is.


The particular code that will be used, looks like this:
```
BEGIN
v
INPUT
I 011. Q 011;
OUTPUT
Q 011. M 011;
RAM
CN01.AND I 011. Q 011 . CN04.NOT Q 011. I 011;
I 011 := NOT I 011
END
```
How the algorithm works, is by mapping the grammar into a dictionary:
```
self.grammar = {
            'BEGIN': 'keywords',
            'END': 'keywords',
            'INPUT': 'keywords',
            'OUTPUT': 'keywords',
            'RAM': 'keywords',
            'I': 'variables',
            'Q': 'variables',
            'M': 'variables',
            'AND': 'logic gates',
            'OR': 'logic gates',
            'XOR': 'logic gates',
            'NOT': 'logic gates',
            'CN01': 'contacts',
            'CN02': 'contacts',
            'CN03': 'contacts',
            'CN04': 'contacts',
            ':=': 'operators',
            ';': 'separators',
            '.': 'separators'
        }
```
From the code file, the algorithm separates the code into individual words, by use of the '.split()' method, and splits them again if there are any points or semicolons.

From there on, using the dictionary, the words are tokenized, according to their keyes. If the word is numeric, it also tokenized, despite not being in the dictionary.

If, however, the word is not in the grammar or a numeric one, it is defined as 'unknown'.

The end result, i.e. the token list, for the provided code looks like this:
```
[['keywords', 'BEGIN'], ['unknown', 'v'], ['keywords', 'INPUT'], 
['variables', 'I'], ['numeric', '011'], ['separators', '.'], 
['variables', 'Q'], ['numeric', '011'], ['separators', ';'], 
['keywords', 'OUTPUT'], ['variables', 'Q'], ['numeric', '011'],
['separators', '.'], ['variables', 'M'], ['numeric', '011'], 
['separators', ';'], ['keywords', 'RAM'], ['contacts', 'CN01'], 
['separators', '.'], ['logic gates', 'AND'], ['variables', 'I'], 
['numeric', '011'], ['separators', '.'], ['variables', 'Q'], 
['numeric', '011'], ['separators', '.'], ['contacts', 'CN04'], 
['separators', '.'], ['logic gates', 'NOT'], ['variables', 'Q'], 
['numeric', '011'], ['separators', '.'], ['variables', 'I'], 
['numeric', '011'], ['separators', ';'], ['variables', 'I'], 
['numeric', '011'], ['operators', ':='], ['logic gates', 'NOT'], 
['variables', 'I'], ['numeric', '011'], ['keywords', 'END']]

```
## Conclusion
In conclusion, lexical analysis and scanners are important components of the compiler or interpreter process in programming languages. Lexical analysis involves breaking down the source code into individual tokens, such as keywords, identifiers, literals, and operators. Scanners, also known as lexical analyzers, are responsible for performing this task efficiently.
Lexical analysis plays a vital role in the compilation process as it serves as the first step in translating human-readable source code into machine-readable form. By identifying and categorizing tokens, scanners provide a structured representation of the source code, which is easier for subsequent phases of the compiler to process.
Scanners typically use regular expressions or finite automata to recognize patterns in the input stream and generate tokens accordingly. They handle various tasks, including skipping whitespace and comments, handling escape sequences, and identifying lexical errors.
Overall, lexical analysis and scanners are fundamental elements of programming language processing. Their accurate and efficient operation ensures the proper interpretation and translation of source code, leading to the successful execution of programs.
