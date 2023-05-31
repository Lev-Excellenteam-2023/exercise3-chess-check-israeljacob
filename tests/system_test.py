import chess_engine


def test_system():
    """
    This function tests a chess game engine by running the Fool's mate and checking the result.
    If the black player wins, the test passes. If the assertion is false, the test fails.
    """
    # setup
    game_state = chess_engine.game_state()
    game_state.move_piece((1, 2), (2, 2), False)
    game_state.move_piece((6, 3), (4, 3), False)
    game_state.move_piece((1, 1), (3, 1), False)
    game_state.move_piece((7, 4), (3, 0), False)

    # test
    checkmate = game_state.checkmate_stalemate_checker()

    # Assert
    assert checkmate == 0
