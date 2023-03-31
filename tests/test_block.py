from src.block import Block
import pytest

@pytest.mark.parametrize('change_by', [1, 2, 3])
def test_generate_hash(change_by):
    for i in range(50):
        block = Block(1, 'prev_hash', 1, 'hash')
        block.hash_block(change_by)
        assert block.hash[-4:] == "0000"


def test_generate_data():
    for i in range(100):
        block = Block(1, 'prev_hash', 1, 'hash')
        assert len(block.data) == 256
