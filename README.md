# The 2self Programming Language

## Installation
### Linux/MacOS
To compile the program, simply run:
```bash
gcc -c main.c -o 2self.o
gcc 2self.o
```
To run a 2self file:
```bash
./2self -r main.2s
```
## Description
2self is an esoteric programming langauge, its concept is simalar to brainfuck in that it is a Turing Machine emulator. Instead of running the program seprate of memory, 2self loads the program into memory and even lets the program "edit" itself. Each instruction is 8 bits or 2 hexadecimal characters, hence the name 2self.
## How Does it work?
### **The Tape (A fancy array)**
The first thing interpriter does is create a tape, this is so the program can be easly edited. The Tape consists of 3 parts, the genral array (where the program is stored), the pointer array (where pointers such as JP, OP and DP are stored), and cache (where the read/write data is stored).
### **Pointers**
2self has three pointers, JP (Jump Pointer), OP (Operation Pointer) and DP (Data Pointer).<br>
>**`JP`**:<br>
If Conditions are met the *OP* is set to the value of the *JP*.<br>
**`OP`**:<br>
The Operation Pointer references the current command. It increments by 1, unless otherwise instructed.<br>
**`DP`**:<br>
The Data Pointer targets the current data, all read/write operations go 
## Instructions
Instructions have to hexadecimal parts, the first character being the command, the second character being the data/argument.
### **Commands**
>**`0`**:<br>
Move the *OP* by the data amount.<br>
**`1`**:<br>
Move the *DP* by the data amount.<br>
**`2`**:<br>
Writes the data to the target of the *DP*.<br>
**`3`**:<br>
Reads the target of *DP* and write it to data.<br>
**`4`**:<br>
Adds data to target of *DP*.<br>
**`5`**:<br>
Subtracts data from target of *DP*.<br>
**`6`**:<br>
Reads from IO and writes to target of *DP*.<br>
**`7`**:<br>
Writes to IO from target of *DP*.<br>
**`8`**:<br>
Loads from *OP* to *OP*+data to subtape.<br>
**`9`**:<br>
Runs subtape the number of times in data.<br>
**`a`**:<br>
Clears the subtape.<br>
**`b`**:<br>
Writes data to the Operation of the *DP*.<br>
**`c`**:<br>
Jumps to *JP* if data is equal to target of *DP*.<br>
**`d`**:<br>
Sets JP to data.<br>
**`e`**:<br>
Reads from cache to data.<br>
**`f`**:<br>
Writes data to cache.<br>