#!/usr/bin/env python3
"""This script sets up the UI for Boggle solver"""

from guizero import App, PushButton

def create_board(hand):
    """ Creates the UI for the app. Takes a set of 16 dice """
    app = App(layout="grid")
    dice = []
    row = 0
    col = 0
    for die in hand:
        dice.append(PushButton(app, text=die, command=clicked,
                               args=[die, col, row], grid=[col, row]))
        col = col+1
        if col == 4:
            row = row +1
            col = 0
    app.display()

def clicked(data, col, row):
    """
    does something when we click a button
    """
    print(data, col, row)

def disable_buttons():
    """
    disable all buttons
    """

if __name__ == '__main__':
    create_board(['A', 'B', 'C', 'D',
                  'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P'])
