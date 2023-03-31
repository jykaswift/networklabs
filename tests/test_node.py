import json

import pytest

from src.node import Node
from src.block import Block



@pytest.mark.parametrize('change_by', [1, 2, 3])
def test_get_genesis(change_by):
    node = Node(change_by)
    node.get_genesis()
    assert json.loads(node.get_genesis())['hash'][-4:] == '0000'


@pytest.mark.parametrize('change_by', [1, 2, 3])
def test_generate_block(change_by):
    node = Node(change_by)
    node.block_list.append(Block(1, 'prev_hash', 1, 'aedasfawsfwaefwafewafsadfsaefewasf'))
    generated_block = json.loads(node.generate_block())
    assert generated_block['hash'][-4:] == '0000'
    assert generated_block['prev_hash'] == node.block_list[-1].hash


@pytest.mark.parametrize('is_asc, expected_result', [(True, 1001), (False, 1)])
def test_receive_block(is_asc, expected_result):
    node = Node(1)
    node.block_list = []
    node.block_list.append(Block(1, 'prev_hash', 1, 'aedasfawsfwaefwafewafsadfsaefewasf'))
    dict_blocks = []
    for i in range(1000):
        block = {
            'prev_hash': 'prev_hash',
            'nonce': 1,
            'hash': 'hash',
            'data': 'data'
        }

        if is_asc:
            block['index'] = i + 2
        else:
            block['index'] = 0 - i

        dict_blocks.append(block)

    for block in dict_blocks:
        node.receive_block(block, 1)

    assert len(node.block_list) == expected_result
