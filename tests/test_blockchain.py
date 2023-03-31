import pytest
from src.node import *
from src.process import *


def test_blockchain_genesis():
    node1 = Node(1)
    server1 = threading.Thread(target=startProcess, args=(1, node1))
    node2 = Node(2)
    server2 = threading.Thread(target=startProcess, args=(2, node2))
    node0 = Node(0)
    server3 = threading.Thread(target=startProcess, args=(0, node0))
    server1.setDaemon(True)
    server2.setDaemon(True)
    server3.setDaemon(True)
    server1.start()
    server2.start()
    server3.start()

    while len(node1.block_list) < 1 or len(node0.block_list) < 1 or len(node2.block_list) < 1:
        time.sleep(0.1)

    assert node1.block_list[0] == node2.block_list[0] == node0.block_list[0]


@pytest.mark.parametrize('blocks', [10, 30, 55])
def test_blockchain_integrity(blocks):
    node1 = Node(1)
    server1 = threading.Thread(target=startProcess, args=(1, node1))
    node2 = Node(2)
    server2 = threading.Thread(target=startProcess, args=(2, node2))
    node0 = Node(0)
    server3 = threading.Thread(target=startProcess, args=(0, node0))
    server1.setDaemon(True)
    server2.setDaemon(True)
    server3.setDaemon(True)
    server1.start()
    server2.start()
    server3.start()

    while len(node1.block_list) < blocks or len(node0.block_list) < blocks or len(node2.block_list) < blocks:
        time.sleep(0.1)

    for i in range(blocks):
        assert node1.block_list[i] == node2.block_list[i] == node0.block_list[i]
