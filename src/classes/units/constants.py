
"""
This module contains constants used for rendering units in the game.
"""

import os

class Colors:

    """
    Colors used for rendering units and board elements.
    """

    PLAYER1_PRIMARY = (255, 0, 0)    #bright red for player 1 main units
    PLAYER2_PRIMARY = (0, 0, 255)    #bright blue for player 2 main units
    PLAYER1_SECONDARY = (200, 0, 0)  #darker red for player 1 secondary units
    PLAYER2_SECONDARY = (0, 0, 200)  #darker blue for player 2 secondary units
    BORDER = (255, 255, 255)         #white borders
    TEXT = (0, 0, 0)                 #black text

class Paths:

    """
    Paths to assets used for rendering units.
    """

    ASSETS_DIR = os.path.join('..', 'assets')
    SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
    MOVE_SOUND = os.path.join(SOUNDS_DIR, 'movement.wav')
    ATTACK_SOUND = os.path.join(SOUNDS_DIR, 'attack.wav')

class UnitDefaults:

    """
    Default values for unit properties.
    """

    FONT_SIZE = 36
    MOVE_SOUND_VOLUME = 0.7
    ATTACK_SOUND_VOLUME = 0.8
    UNIT_SCALE = 0.8  #unit size scaling factor