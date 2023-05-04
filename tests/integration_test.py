from enums import Player
from ai_engine import chess_ai
from unittest.mock import patch, Mock
from Piece import Knight
from Piece import Rook
from Piece import Bishop
import Piece

def test_get_valid_piece_moves():

    # Mock Knight instance
    mock_knight = Mock()

    mock_knight.get_valid_peaceful_moves.side_effect = [[(1, 2), (2, 5)]]
    mock_knight.get_valid_piece_takes.side_effect = [[(1, 4), (4, 1)]]

    result = Knight.get_valid_piece_moves(mock_knight, Mock())

    assert result == [(1, 2), (2, 5), (1, 4), (4, 1)]

def is_valid_piece(row :int, col :int) -> bool:
    return True if col == 2 or row == 5 else False
def get_piece(row :int, col :int) -> bool:
    if col == 2:
        return Rook("my_rook", row, col, Player.PLAYER_1)
    if row == 5:
        return Bishop("my_bishop", row, col, Player.PLAYER_2)

def get_piece_value(piece :Piece, player: Player) -> int:
    if piece.get_player() == Player.PLAYER_1:
        return 50
    return -30
def test_evaluate_board():

    mock_ai_engine = Mock()
    mock_ai_engine.get_piece_value.side_effect = get_piece_value

    mock_game_state = Mock()
    mock_game_state.is_valid_piece.side_effect = is_valid_piece
    mock_game_state.get_piece.side_effect = get_piece

    result = chess_ai.evaluate_board(mock_ai_engine, mock_game_state, Player.PLAYER_1)

    assert result == 190

