#!/usr/bin/env python3
"""This script sets up the UI for Boggle solver"""

from guizero import App, PushButton, Box, Text

def create_board(hand):
    """ Creates the board for the app. Takes a set of 16 dice """
    row = 0
    col = 0
    dice = []
    for num, die in enumerate(hand):
        dice.append(PushButton(dice_box, text=die, command=clicked,
                               args=[die, col, row, num],
                               grid=[col, row], width=2, height=1))
        col = col+1
        if col == 4:
            row = row +1
            col = 0
    return dice


def clicked(data, col, row, num):
    """
    disable the clicked button and all buttons that aren't around the clicked letter
    and haven't been selected already, return the letter to add to the selected word.
    """
    disabled.append(num)
    word.append(data)
    print(data, col, row, 'word: ', word, 'num: ', num, 'disabled: ', disabled)
    for square in board_squares:
        square.disable()
    print(CONNECTED[num])
    for element in CONNECTED[num]:
        board_squares[element].enable()
    for element in disabled:
        board_squares[element].disable()
    current_word.value = (''.join(word))


def submit_word():
    """
    Clears the grid, enables all the dice, checks and scores the word and adds to the word list
    """
    print(''.join(word))
    for square in board_squares:
        square.enable()
    wordlist.append(''.join(word))
    wordlist.append('\n')
    disabled.clear()
    word.clear()
    current_word.value = ''
    # score word, add to list

def clear_word():
    """
    Clears the grid, enables all the dice and clears the word
    """
    for square in board_squares:
        square.enable()
    disabled.clear()
    word.clear()
    current_word.value = ''


CONNECTED = [[1, 4, 5], [0, 2, 4, 5, 6], [1, 3, 5, 6, 7], [2, 6, 7],
             [0, 1, 5, 8, 9], [0, 1, 2, 4, 6, 8, 9, 10],
             [1, 2, 3, 5, 7, 9, 10, 11], [2, 3, 6, 10, 11],
             [4, 5, 9, 12, 13], [4, 5, 6, 8, 10, 12, 13, 14],
             [5, 6, 7, 9, 11, 13, 14, 15], [6, 7, 10, 14, 15],
             [8, 9, 13], [8, 9, 10, 12, 14], [9, 10, 11, 13, 15], [10, 11, 14]]
app = App("Boggle Scorer", layout="grid")
top_box = Box(app, layout='grid', border=1, grid=[0, 0])
rest = Box(app, layout='grid', border=1, grid=[0, 1])
title = Text(top_box, text='Time: ', grid=[0, 0], align='left', width='fill')
title2 = Text(top_box, text='Score: ', grid=[1, 0], align='right', width='fill')
dice_box = Box(rest, layout='grid', grid=[0, 1], border=2)
test_hand = ['A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H',
             'I', 'J', 'Qu', 'L',
             'M', 'N', 'O', 'P']
word = []
disabled = []
board_squares = create_board(test_hand)
word_list = Box(rest, layout='grid', grid=[1, 1], border=2, align='top')
word_box = Box(rest, layout='grid', grid=[0, 2])
wordtitle = Text(word_list, text='Word List', grid=[0, 0])
wordlist = Text(word_list, text='', grid=[0, 1])
current_word_title = Text(word_list, text='Current Word:', grid=[0, 2], align='bottom')
current_word = Text(word_list, text=(''.join(word)), grid=[0, 3])
submit = PushButton(word_box, text='Submit', command=submit_word, grid=[0, 0])
clear = PushButton(word_box, text='Clear', command=clear_word, grid=[1, 0])
app.display()
