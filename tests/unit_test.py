from enums import Player
from unittest.mock import patch, Mock
from Piece import Knight
from Piece import Pawn


# Test functions to create mock game state for testing
def empty_board(row: int, col: int) -> Player:
    """
    Returns empty board
    """
    return Player.EMPTY


def piece_in_all_possibilities(row: int, col: int) -> Player:
    """
    Returns board with a pawn at Player.PLAYER_2
    """
    return Pawn("my_pawn", row, col, Player.PLAYER_2)


def piece_in_most_possibilities(row: int, col: int) -> Player:
    """
    Returns board with a pawn at Player.PLAYER_2, except at (1, 2)
    """
    return Player.EMPTY if (row, col) == (1, 2) else Pawn("my_pawn", row, col, Player.PLAYER_2)


def piece_of_player2(row: int, col: int) -> Player:
    """
    Return a Pawn belonging to Player.PLAYER_1 at (1,2) and a Pawn belonging to Player.PLAYER_2 at all other positions
    """
    return Pawn("my_pawn", row, col, Player.PLAYER_1) if (row, col) == (1, 2) else Pawn("my_pawn", row, col,
                                                                                        Player.PLAYER_2)


def there_is_not_a_piece(row: int, col: int) -> bool:
    """
    Return False to indicate that there is no piece at the given position
    """
    return False


def there_is_a_piece(row: int, col: int) -> bool:
    """
    Return True to indicate that there is a piece at the given position
    """
    return True


def test_get_valid_peaceful_moves_empty_board():
    """
    Test case for the get_valid_peaceful_moves method of the Knight class
    when the knight is surrounded by empty squares.

    Expected Result: List of valid peaceful moves for the Knight.
    Expected Output: [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]
    """

    mock_game_state = Mock()
    mock_knight = Mock()
    mock_knight.get_row_number.return_value = 3
    mock_knight.get_col_number.return_value = 3
    mock_game_state.get_piece.side_effect = empty_board

    result = Knight.get_valid_peaceful_moves(mock_knight, mock_game_state)

    assert result == [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]


def test_get_valid_peaceful_moves_all_pieces():
    """
    Test case for the get_valid_peaceful_moves method of the Knight class
    when the knight is surrounded by opponent pieces.

    Expected Result: List of valid peaceful moves for the Knight.
    Expected Output: []
    """

    mock_game_state = Mock()
    mock_knight = Mock()
    mock_knight.get_row_number.return_value = 3
    mock_knight.get_col_number.return_value = 3
    mock_game_state.get_piece.side_effect = piece_in_all_possibilities

    result = Knight.get_valid_peaceful_moves(mock_knight, mock_game_state)

    assert result == []


def test_get_valid_peaceful_moves_mixed_pieces():
    """
    Test case for the get_valid_peaceful_moves method of the Knight class
    when the knight is surrounded by a mix of opponent and friendly pieces.

    Expected Result: List of valid peaceful moves for the Knight.
    Expected Output: [(1, 2)]
    """

    mock_game_state = Mock()
    mock_knight = Mock()
    mock_knight.get_row_number.return_value = 3
    mock_knight.get_col_number.return_value = 3
    mock_game_state.get_piece.side_effect = piece_in_most_possibilities

    result = Knight.get_valid_peaceful_moves(mock_knight, mock_game_state)

    assert result == [(1, 2)]


def test_get_valid_piece_takes_alone():
    """
    Test case for the get_valid_piece_takes method of the Knight class
    when the knight is alone on the board.

    Expected Result: List of valid piece take moves for the Knight.
    Expected Output: []
    """

    mock_game_state = Mock()
    mock_knight = Mock()
    mock_knight.get_row_number.return_value = 3
    mock_knight.get_col_number.return_value = 3
    mock_knight.get_player.return_value = Player.PLAYER_1
    mock_game_state.get_piece.side_effect = empty_board
    mock_game_state.is_valid_piece.side_effect = there_is_not_a_piece

    result = Knight.get_valid_piece_takes(mock_knight, mock_game_state)

    assert result == []


def test_get_valid_piece_takes_all_pieces():
    """
    Test case for the get_valid_piece_takes method of the Knight class
    when the knight is surrounded by opponent pieces.

    Expected Result: List of valid piece take moves for the Knight.
    Expected Output: [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]
    """

    mock_game_state = Mock()
    mock_knight = Mock()
    mock_knight.get_row_number.return_value = 3
    mock_knight.get_col_number.return_value = 3
    mock_knight.get_player.return_value = Player.PLAYER_1
    mock_game_state.get_piece.side_effect = piece_in_all_possibilities
    mock_game_state.is_valid_piece.side_effect = there_is_a_piece

    result = Knight.get_valid_piece_takes(mock_knight, mock_game_state)

    assert result == [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]

def test_get_valid_piece_takes_mixed_pieces():
    """
    Test case for the get_valid_piece_takes method of the Knight class
    when the knight is surrounded by opponent pieces except for one friendly piece.

    Expected Result: List of valid piece take moves for the Knight.
    Expected Output: [(1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]
    """

    mock_game_state = Mock()
    mock_knight = Mock()
    mock_knight.get_row_number.return_value = 3
    mock_knight.get_col_number.return_value = 3
    mock_knight.get_player.return_value = Player.PLAYER_1
    mock_game_state.get_piece.side_effect = piece_of_player2
    mock_game_state.is_valid_piece.side_effect = there_is_a_piece

    result = Knight.get_valid_piece_takes(mock_knight, mock_game_state)

    assert result == [(1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]