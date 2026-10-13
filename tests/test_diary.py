from lib.diary import Diary

def test_return_empty_contents():
    diary = Diary("")
    assert diary.read() == ""