#!/usr/bin/env python3
"""This script returns a valid Boggle board"""

import random

CLASSIC_DICE = ['AACIOT', 'ABILTY', 'ABJMOQ', 'ACDEMP',
                'ACELRS', 'ADENVZ', 'AHMORS', 'BIFORX',
                'DENOSW', 'DKNOTU', 'EEFHIY', 'EGKLUY',
                'EGINTV', 'EHINPS', 'ELPSTU', 'GILRUW']
NEW_DICE = ['AAEEGN', 'ABBJOO', 'ACHOPS', 'AFFKPS',
            'AOOTTW', 'CIMOTU', 'DEILRX', 'DELRVY',
            'DISTTY', 'EEGHNW', 'EEINSU', 'EHRTVW',
            'EIOSST', 'ELRTTY', 'HIMNUQ', 'HLNNRZ']

def get_dice(input_dice):
    """
    Returns a list of Boggle dice (a list of letters), either Classic or New Boggle Dice
    """
    dice = []
    for die in input_dice:
        choice = random.choice(die)
        if choice == 'Q':
            dice.append('QU')
        else:
            dice.append(choice)
    return dice


if __name__ == '__main__':
    print(get_dice(CLASSIC_DICE))
