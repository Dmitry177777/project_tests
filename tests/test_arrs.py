import pytest
from utils import arrs

@pytest.fixture
def list_():
   return [1, 2, 3]

def test_get(list_):
   assert arrs.get(list_, 1, "test") == 2
   assert arrs.get([], 0, "test") == "test"


def test_slice(list_):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(list_, 1) == [2, 3]
    assert arrs.my_slice([], 0,-1) == []
    assert arrs.my_slice([1, 2, 3], -1,0) == []
    assert arrs.my_slice(list_, -4, 0) == []