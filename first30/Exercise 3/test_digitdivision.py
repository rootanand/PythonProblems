#Test condition for the Digit division:
import digitdivision


def test_canassertTrue():
    assert True
    
def test_digitdivision():
    actual= digitdivision.Digitdivision(123)
    expected=False
    assert actual==expected    

def test_digitdivision1():
    actual = digitdivision.Digitdivision(36)
    expected=True
    assert actual==expected

