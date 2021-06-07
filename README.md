# Python Computer

author: Rebecca Brunner
<br>
date: 28 August 2020

## Description

A 16-bit virtual computer written in Python based on only two primitives, the nand_gate function and the Bit class.  This computer and its architecture are based on the HACK computer from the nand2tetris free online class.

## References

- nand2tetris: https://www.nand2tetris.org/

## Motivation

- Continual improvement
- Push towards CS mastery
- Gain better understanding of several classic CS courses

## Notes

This project was meant as a learning exercise.  As such the computer performs terribly.  Many functions could simply be implemented using python, however, this computer implements them by recursing down to nand_gates.  Programs that render screen input update the screen pixel by pixel instead of all at once.  The recursive RAM memory makes writing output to RAM take a noticeable amount of time, and builds up quickly in more complex programs.  RAM issues could be resolved in the future by changing to use an array instead of classes.  Even in the actual course, the only reason why games such as the pong example are actually playable is because the CPU emulator provided skips rendering to the screen pixel by pixel.

Out of respect for the makers of this course and their desire to not have answers posted online, I have decided not to post source code for any chip that is part of one of their assignments.  Even though I have implemeted the chips in python instead of the HDL used in the nand2tetris course, I still feel the python code provides too much insight.  Especially for the first and second projects.

Instead, I intended on posting stubs for each chip along with notes describing each chip's functionality to serve as documentation and for future reference of chips that were challenging to implement (*cough* cpu *cough*) I will be pushing my screen, keyboard, and rom source code though, because these chips were not covered in nand2tetris.  I will also be compiling a binary executable of the final computer.

<!-- The binaries have been compiled on Windows 10 Pro v1709 and Ubuntu 18.04.3.  The compiled binary includes an application that renders a line to the screen when a key is pressed.  The key must be pressed down until the command that checks the keyboard is executed again, which could take a few seconds.  Releasing the key beforehand will reset the keyboard back to its unpressed state and will not render anything to the screen.  A display driver is necessary to run the application - the app will crash otherwise. -->

Additionally:

- The screen & keyboard are processed using pygame.  Numpy is used for the screen memory map.
- tf_to_01 translates a program for this computer written completely in True and False into regular 0 and 1s
- Likewise zero_to_false does the opposite
- A simple program demonstrating input and output is included, pressing a key input down will render a line to the screen

### Updated 1/24/2021 with VM translator (pt 1)

Added an initial vm translator that operates on a stack architecture.  Implements arithmetic and logical operators, as well as push and pop operations across 8 virtual segments (architecture described in nand2tetris book).  Also added example vm program and its generated outputs.

### Updated 2/26/2021 with VM translator (pt 2) and Optimized RAM

Added full implementation of vm translator including generation of bootstrap code, program flow, and call & return.  Added FAST_RAM and FAST_REGISTER.  FAST_RAM provides a significant boost to reading/writing from RAM, however, has not been implemented into builds yet.

### Updated 4/13/2021 with Compiler Stage 1

Added first stages of a compiler.  The current compiler consists of a tokenizer and parser but no code generation.  The compiler produces an xml file that contains the structure for a given input file's parse tree.

### Updated 6/6/2021 with Compiler Stage 2

Finished compiler with code generation.

Current Workflow:

Write a .jack program -> call `compiler.py` -> call `vmtranslator.py filename` -> call `assembly.py filename` -> call `computer.py`

## Future Work

- Create an OS (nand2tetris pt2)
- Create a compiler (nand2tetris pt2)
