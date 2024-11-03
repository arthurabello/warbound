"""
This module represents the game board, responsible for managing selectable squares, colors, and the highlighting system.
"""

import pygame
from .graph import BoardGraph

class Board:
    
    """
    Manages the board layout, including the selection of squares, highlighting reachable positions, 
    and drawing the board on the screen.

    Attributes:
        m (int): Number of rows on the board.
        n (int): Number of columns on the board.
        initial_width (int): Initial width of the game window.
        initial_height (int): Initial height of the game window.
        selected_square (tuple or None): The currently selected square on the board, or None if no square is selected.
        graph (BoardGraph): Instance of the BoardGraph class to manage board connectivity.
        reachable_positions (set): Set of squares that are reachable from the selected square.

    Methods:
        get_square_from_click(mouse_pos, screen): Determines which square was clicked based on mouse position.
        select_square(square, movement_points): Selects a square and calculates reachable positions based on movement points.
        draw(screen, selected_square): Draws the board, with highlights for reachable and selected squares.
    """

    COLOR_LIGHT_GREEN = (144, 238, 144)
    COLOR_DARK_GREEN = (0, 100, 0)
    COLOR_RED = (255, 0, 0)
    COLOR_HIGHLIGHT = (255, 255, 0, 180)

    def __init__(self, m, n, initial_width, initial_height) -> None:

        """
        Initializes the board with dimensions and sets up the board graph for connectivity management.

        Args:
            m (int): Number of rows on the board
            n (int): Number of columns on the board
            initial_width (int): Initial width of the game window
            initial_height (int): Initial height of the game window
        """

        self.m = m
        self.n = n
        self.initial_width = initial_width
        self.initial_height = initial_height
        self.selected_square = None
        self.graph = BoardGraph(m, n)
        self.reachable_positions = set()

    def get_square_from_click(self, mouse_pos, screen) -> None:
        
        """
        Determines the board square corresponding to a mouse click based on screen dimensions.

        Args:
            mouse_pos (tuple): The (x, y) position of the mouse click
            screen (pygame.Surface): The game screen surface

        Returns:
            tuple: The (row, column) of the clicked square
        """

        x, y = mouse_pos
        width, height = screen.get_size()
        square_width = width // self.n
        square_height = height // self.m
        column = x // square_width
        row = y // square_height
        return row, column

    def select_square(self, square, movement_points) -> None:

        """
        Selects a square and calculates all reachable positions based on the movement points available.

        Args:
            square (tuple): The (row, column) position of the selected square
            movement_points (int): Number of movement points available for calculating reachable positions
        """

        self.selected_square = square
        if square:
            self.reachable_positions = self.graph.get_reachable_positions(square, movement_points)
        else:
            self.reachable_positions = set()

    def draw(self, screen, selected_square=None) -> None:

        """
        Draws the board on the screen, highlighting reachable positions and the selected square.

        Args:
            screen (pygame.Surface): The game screen surface
            selected_square (tuple, optional): The currently selected square to highlight. Defaults to None.
        """

        width, height = screen.get_size()
        square_width = width // self.n
        square_height = height // self.m

        for row in range(self.m):
            for column in range(self.n):
                color = self.COLOR_LIGHT_GREEN if (row + column) % 2 == 0 else self.COLOR_DARK_GREEN

                pygame.draw.rect(screen, color,(column * square_width, row * square_height, square_width, square_height))

                if (row, column) in self.reachable_positions:
                    highlight_surface = pygame.Surface((square_width, square_height), pygame.SRCALPHA)
                    pygame.draw.rect(highlight_surface, self.COLOR_HIGHLIGHT, (0, 0, square_width, square_height))
                    screen.blit(highlight_surface, (column * square_width, row * square_height))

                if selected_square and (row, column) == selected_square:
                    pygame.draw.rect(screen, self.COLOR_RED, (column * square_width, row * square_height, square_width, square_height), 3)