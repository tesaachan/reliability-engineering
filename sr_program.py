from os import path
from sys import stdin
import sr_ex01.sr_ex01 as e1
import sr_ex02.sr_ex02 as e2
import sr_ex03.sr_ex03 as e3

def sr_ex01_util(filename):
    if not path.exists(filename):
        print("\033[93mwrong path or file doesn't exist.\033[39m\n")
        return
    with open(filename, "r", encoding="utf8") as source:
        e1.sr_ex01(source)

def sr_print_manual():
    print(
    "1. input 'run ex01' to run exercise 1\
    \n   then input filename or press 'Enter' if you want stdin\
    \n2. input 'run ex02' to run exercise 2\
    \n3. input 'run ex03' to run exercise 3\n")

if __name__ == "__main__":
    print("\033[39mWelcome to 'ICS reliability' program.\
           \nInput 'exit' to finish the program, 'manual' for help.\n")
    while (True):
        print("\033[36m>> \033[39m", end='')
        command = input()
        if command == "exit":
            print("\033[92mfinished\033[39m")
            exit()
        elif command == "manual":
            sr_print_manual()
        elif command == "run ex01":
            print("filename: ", end='')
            filename = input()
            sr_ex01_util(filename) if filename != "" else e1.sr_ex01(stdin)
        elif command == "run ex02":
            e2.sr_ex02()
        elif command == "run ex03":
            e3.sr_ex03()
