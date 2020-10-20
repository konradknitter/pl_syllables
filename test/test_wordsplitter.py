from pl_syllables import WordSplitter

def test_empty():
    assert WordSplitter("").to_syllables() == []

def test_trójmorze():
    assert WordSplitter("trójmorze").to_syllables() == ["trój", "mo", "rze"]
