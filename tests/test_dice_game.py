from dice_game import roll_dice

def test_roll_dice_range():
    result = roll_dice()
    assert 1 <= result <= 6
