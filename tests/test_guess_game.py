from guess_game import check_guess

def test_check_guess():
    assert check_guess(5, 5)
    assert not check_guess(5, 3)
