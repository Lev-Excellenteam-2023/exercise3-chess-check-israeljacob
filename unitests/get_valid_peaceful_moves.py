from enums import Player
from unittest.mock import patch, Mock
from Piece import Knight
from Piece import Pawn

# Test functions to create mock game state for testing
def test_1_mock_game_board(row: int, col: int) -> Player:
    """
    Returns empty board
    """
    return Player.EMPTY

def test_2_mock_game_board(row: int, col: int) -> Player:
    """
    Returns board with a pawn at Player.PLAYER_2
    """
    return Pawn("my_pawn", row, col, Player.PLAYER_2)

def test_3_mock_game_board(row: int, col: int) -> Player:
    """
    Returns board with a pawn at Player.PLAYER_2, except at (1, 2)
    """
    return Player.EMPTY if (row, col) == (1, 2) else Pawn("my_pawn", row, col, Player.PLAYER_2)

def test_get_valid_peaceful_moves():
    """
    Tests Knight's get_valid_peaceful_moves method
    """

    mock_game_state = Mock()

    # Mock Knight instance
    mock_knight = Mock()
    mock_knight.get_row_number.return_value = 3
    mock_knight.get_col_number.return_value = 3

    # TC01: Knight is alone on board

    # Setup
    mock_game_state.get_piece.side_effect = test_1_mock_game_board

    # Test
    result = Knight.get_valid_peaceful_moves(mock_knight, mock_game_state)

    # Assert
    assert result == [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]

    # TC02: Knight is surrounded by opponent pawns

    # Setup
    mock_game_state.get_piece.side_effect = test_2_mock_game_board

    # Test
    result = Knight.get_valid_peaceful_moves(mock_knight, mock_game_state)

    # Assert
    assert result == []

    # TC03: Knight is surrounded by opponent pawns except for one friendly pawn
    
    # Setup
    mock_game_state.get_piece.side_effect = test_3_mock_game_board

    # Test
    result = Knight.get_valid_peaceful_moves(mock_knight, mock_game_state)

    # Assert
    assert result == [(1, 2)]
