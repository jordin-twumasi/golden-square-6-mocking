from lib.secret_diary import SecretDiary
from unittest.mock import Mock


#Shouldve been a raise error - mistake to fix in refactoring
def test_attempts_to_read_locked_diary():
    fake_diary = Mock()
    fake_diary.contents.return_value = 'My diary contents'

    secret_diary = SecretDiary(fake_diary)
    secret_diary.lock()
    assert secret_diary.read() == "Go away!"

def test_attempts_to_read_unlocked_diary():
    fake_diary = Mock()
    fake_diary.contents.return_value = 'My diary contents'
    fake_diary.read.return_value = "My diary contents"
    
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My diary contents"
    
