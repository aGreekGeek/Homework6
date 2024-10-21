# Homework 5

## Purpose
This project involves developing a command-line application that functions as a basic calculator, performing addition, subtraction, multiplication, and division operations. The app is built using the command pattern and incorporates a plugin architecture to allow for extensibility.

## Objectives
1. Set up a Read-Evaluate-Print Loop (REPL) for user interaction.
2. Ensure comprehensive testing and code coverage.
3. Implement a flexible plugin architecture for modularity and future enhancements.

## Bonus Objectives
1. Add a menu command to enhance user interaction within the REPL.
2. Explore and potentially implement multi-processing capabilities for improved performance.

## Functionality
The application allows users to perform basic arithmetic operations via a command-line interface. Upon launching, the app enters a REPL where users can input commands to:

- Add two numbers.
- Subtract two numbers.
- Multiply two numbers.
- Divide two numbers (with safeguards against division by zero).

Additionally, the app uses a plugin architecture, making it possible to extend its functionality by adding new operations or commands without altering the core codebase. The REPL structure provides a responsive, interactive experience, continuously evaluating and processing user inputs until an exit command is given.

Optional enhancements include a menu system to guide users through available commands and multi-processing support to handle more complex calculations efficiently.
