from main import main
from utils import utils, Class


def test_code():
    assert len(utils.sort_by_date(6)) == 6
    assert utils.right_input("6") == 6

