# Automated testing of guizero applications

This is the code for my talk to the Raspberry Pint group on 26 April 2022.

It's an implementation of Noughts and Crosses (US: tic-tac-toe) using the brilliant `guizero` library.

It contains an automated test which drives the GUI.

The game code is adapted from the example in [Create Graphical User Interfaces in Python](https://magpi.raspberrypi.com/books/create-guis)

I would normally keep source code and test code in separate directories.
In this repository I have kept them in the project root since the test is as important as the source.

## To Install:

In a directory of your choice, run
```git clone https://github.com/romilly/testing-guizero-apps.git```

## To run:

### The game

```python3 tictactoe.py```

### The test

```python3 test-app.py```
