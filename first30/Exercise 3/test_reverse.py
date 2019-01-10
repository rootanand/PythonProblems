#Test condition for reverse:
import reverse
def test_canassertTrue():
    assert True

def test_reverseofdigits():
    actual=reverse.Reverseint(1234)
    expected=4321
    assert actual==expected