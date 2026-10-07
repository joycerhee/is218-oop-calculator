# OOP Calculator

A command-line calculator written in Python using object-oriented programming. It can add and subtract, and it keeps a history of the calculations made during a session.

## Installation

You need Python 3.11 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

If the python command fails or points to a different Python, use .venv/bin/python instead.
```

## Running

```bash
python -m calculator
```

The commands are add, subtract, history, remove, help, and exit.

```text
> add
First number: 10
Second number: 5
Result: 15
> history
Calculation History

1. Add: 10, 5 = 15
> exit
Goodbye!
```

## Testing

```bash
python -m pytest
```

There are 42 tests. The test run also checks coverage and fails if it is under 100%, for both lines and branches.

## Design choices

Calculation is an abstract class. Add and Subtract both store two numbers, so that part lives in the parent class instead of being copied. Each subclass only writes its own get_result method.

History owns the list of calculations. Other code has to go through its add, get_history, and remove methods. get_history returns a copy, so changing the returned list does not change the real history.

The CLI looks up the typed command in a dictionary to get the right class, so there is no separate if statement for each operation.

Numbers are checked before a calculation is added to history. If the input is invalid, the program prints a message and nothing is saved.

## Reflection

To add Multiply, I would create a Multiply class in calculation.py that inherits from Calculation and has its own get_result method. Then I would import it in cli.py, add it to the operations dictionary, add a line for it in the help text, and write tests for it. History would not need any changes because it only stores calculation objects and never does the math itself.

Email and text message notifications could share a contract where both have a send() method that delivers a message. The code calling send() would not need to know which type of notification it has. This is the same idea as Add and Subtract both having get_result().

The design ideas would transfer to another language, like giving each class one job, using a parent class as a shared contract, and letting one object manage its own data. What I would still need to learn is how that language writes classes and inheritance, how its types work, and how it handles errors. For example, Java has interfaces and JavaScript uses prototypes underneath its classes.