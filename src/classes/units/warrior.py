"""
Warrior unit implementation. Warriors are the main combat units with
greater mobility than Kings but less strategic importance.
"""

from .base_unit import BaseUnit
from .constants import Colors

class Warrior(BaseUnit):

    """
    Represents a Warrior piece on the game board.
    
    Warriors are the main combat units with extended movement range
    and the ability to attack enemies.
    
    Attributes:
        Inherits all attributes from BaseUnit
        attack_bonus (int): Additional attack strength for this warrior
    """
    
    def __init__(self, initial_position, player):

        """
        Initialize a new Warrior unit.
        
        Args:
            initial_position (tuple): Starting position (row, col)
            player (int): Player number (1 or 2)
        """

        super().__init__(
            initial_position=initial_position,
            player=player,
            movement_range=3,
            unit_char='W'
        )
        
        self.attack_points = 10
        self.defense_points = 5
        self.remaining_units = 256

        self.attack_bonus = 1
        
        self.primary_color = (Colors.PLAYER1_SECONDARY if player == 1 
                            else Colors.PLAYER2_SECONDARY)
    
    def can_move_to(self, position, board, all_units):

        """
        Check if the warrior can move to a given position.
        
        Warriors can move up to three squares in any direction, but cannot
        move through or onto other units.
        
        Args:
            position (tuple): Target position to check
            board (Board): Game board instance
            all_units (list): List of all units on the board
            
        Returns:
            bool: True if the move is valid, False otherwise
        """

        if not self.is_alive:
            return False

        reachable = board.graph.get_reachable_positions(
            self.position, 
            self.movement_range
        )
        if position not in reachable:
            return False

        for unit in all_units:
            if (unit != self and unit.is_alive and 
                unit.position == position):
                return False

        return True
    
    def attack(self, target):

        """
        Enhanced attack method for Warriors.
        Warriors get an attack bonus when attacking.
        
        Args:
            target: The unit being attacked
        """

        if not self.is_alive or not target.is_alive or target.player == self.player:
            return
            
        try:
            self.attack_sound.play()
        except Exception as e:
            print(f"Failed to play warrior attack sound in units/warrior: {str(e)}")
            
        target.is_alive = False