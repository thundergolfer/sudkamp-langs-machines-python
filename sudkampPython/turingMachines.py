# Credit:  http://www.python-course.eu/turing_machine.php

class Tape(object):
    blank_symbol = " "
    def __init__(self, input=""):
        self.__tape = {}
        for i,sym in enumerate(input):
            self.__tape[i] = sym

    def __str__(self): # BUG
        s = ""
        minUsedIndex = min(self.__tape.keys())
        maxUsedIndex = max(self.__tape.keys())
        for i in range(minUsedIndex, maxUsedIndex):
            s += self.__tape[i]
        return s

    def __getItem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return blank_symbol

    def __setItem__(self, pos, char):
        self.__tape[pos] = char


class TuringMachine(object):

    def __init__(self,
                 tape = "",
                 blank_symbol = " ",
                 tape_alphabet = ["0", "1"],
                 initial_state = "",
                 accepting_states = [],
                 final_states = [],
                 transition_function = {}):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        self.__transition_function = transition_function
        self.__tape_alphabet = tape_alphabet
        self.__final_states = final_states

    def showTape(self):
        print(self.__tape)
        return True

    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                 self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]

    def inFinal(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False

if __name__ == "__main__":
    # Test the class
    def quickTest( func, input, expected):
        if func(input) == expected:
            print(input, ": passed!")
        else:
            print(input, ": failed!")

    
