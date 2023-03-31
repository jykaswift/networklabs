import sys

from node import Node
from process import startProcess

if __name__ == '__main__':
    node_index = int(sys.argv[1])
    node = Node(node_index)
    startProcess(node_index, node)


