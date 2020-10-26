from pl_syllables import WordSplitter

def test_empty():
    assert WordSplitter("").to_syllables() == []

def test_trójmorze():
    assert WordSplitter("trójmorze").to_syllables() == ["trój", "mo", "rze"]

def test_konstatynopol():
    assert WordSplitter("konstantynopol").count_sylables() == 5
    assert WordSplitter("konstantynopol").to_syllables() == ["kon", "stan", "ty", "no", "pol"]
