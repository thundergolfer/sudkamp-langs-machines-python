<p align="center">
  <img src="images/repo_header_python.png">
</p>

# Sudkamp Languages And Machines - Python 3

All the algorithms from Sudkamp's [Languages and Machines](http://www.amazon.com/Languages-Machines-Introduction-Computer-Science/dp/0321322215) implemented in *Python 3*.

**Note:** If you prefer *Java*, the same work is being done in that language over in [thundergolfer/sudkamp-langs-machines-java](https://github.com/thundergolfer/sudkamp-langs-machines-java).

## Contributing

You are welcome to fork this repo in order to complete unimplemented algorithms or to improve on the existing ones. Please try to stick as close to the pseudo-code from the book.

### Index of Algorithms

| **Page** | **Number** | **Name (in 3<sup>rd</sup> edition)** | **Name (in repository)** | **File**   |
|:----------|:-----------|:-------------------------------------|:-------------------------|:-----------|
| 108       | 4.2.1      | Construction of Set of Nullable Vars | constructSetOfNullableVars()                          |    [contextFree.py](/sudkampPython/grammars/contextFree.py)    |
| 114	      | 4.3.1      | Construction of the Set CHAIN(A)     | chain(A) | [contextFree.py](/sudkampPython/grammars/contextFree.py) |
| 117       | 4.4.2      | Constr. of Set of Vars that Derive Terminal Strings | getVariablesThatDeriveTerminalStrings() | [contextFree.py](/sudkampPython/grammars/contextFree.py) |
| 119       | 4.4.4      | Contruction of Set of Reachable Vars. | constructSetOfReachableVars() | [contextFree.py](/sudkampPython/grammars/contextFree.py)] |
| 126       | 4.6.1      | CYK Algorithm | CYK() | [cyk.py](/sudkampPython/cyk.py) |
| 172       | 5.6.3      | Contruction of DM, a DFA Equiv. to NFA M | | |
| 179       | 5.7.2      | Determination of Equivalent States of DFA | determineEquivelantStatesOfDFA() | [finiteAutomaton.py](/sudkampPython/finiteAutomaton.py) |
| 194       | 6.2.2      | Construction of a Regular Expression from a Finite Automaton | | |
| 543       | 17.4.3     | Recursive Simulation of NonDeterministic Turing Machine | | |
| 558       | 18.2.1     | Breadth-First Top-Down Parser | | |
| 564       | 18.4.1     | Breadth-First Bottom-Up Parser |  | |
| 581       | 19.4.1     | Construction of FIRST<sub>k</sup> Sets | | |
| 583       | 19.5.1     | Construction of FOLLOW<sub>k</sup> Sets | | |
| 588       | 19.7.1     | Deterministic Parser for a Strong LL(k) Grammar | | |
| 591       | 19.8.3     | Deterministic Parser for an LL(k) Grammar | | |
| 600       | 20.2.1     | Parser for an LR(0) Grammar | | |
| 604       | 20.3.3     | Parser Utilizing the Deterministic LR(0) Machine | | |
| 618       | 20.5.4     | Parser for an LR(1) Grammar |  | |


### Index Of Related Algorithms Not Provided In The Textbook

| **Name**                      | **Name (In Repository)**        | **File**         |
|:-------------------------------|:---------------------------------|:---------------|
|  Calculate null closure of finite automaton | nullClosure() | [finiteAutomaton.py](sudkampPython/finiteAutomaton.py)                |
|                                |                                  |                |

### Credits

* Credit to [tyarkoni](https://github.com/tyarkoni) for his [work on finite state machines](https://github.com/tyarkoni/transitions) that formed the foundation for my work in that area.

* Credit to [Sebastian Sardina](https://sites.google.com/site/ssardina/) for being an awesome *Computing Theory* teacher.

## License

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Thundergolfer](http://www.jonathonbelotti.com) has waived all copyright and related or neighboring rights to this work.
