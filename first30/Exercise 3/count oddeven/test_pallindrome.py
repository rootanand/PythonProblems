def test_canassertTrue():
    assert True


import pallindrome
def test_pallindrome():
    actual=pallindrome.Ispallindrome(1221)
    expected=True
    assert expected==actual