from src.block import Block

class Node:
    block_list = []

    def __init__(self, change_by):
        self.change_by = change_by

    def get_genesis(self):
        block = Block(1, 'first_hash', 1, '')
        block.hash_block(self.change_by)
        return block.get_json_block()

    def receive_block(self, received_block, node_id):
        adding_block = self.__create_new_block_by(received_block)

        if adding_block.index == 1 and len(self.block_list) == 0:
            self.block_list.append(adding_block)
            if self.change_by != int(node_id):
                print(f'Node {self.change_by} save {adding_block.get_json_block()} received from Node {node_id}')
            return True

        if self.block_list[-1].index >= adding_block.index:
            return False

        self.block_list.append(adding_block)
        if self.change_by != int(node_id):
            print(f'Node {self.change_by} save {adding_block.get_json_block()} received from Node {node_id}')
        return True


    def __create_new_block_by(self, received_block):
        new_block = Block(
            int(received_block['index']),
            received_block['prev_hash'],
            int(received_block['nonce']),
            received_block['hash']
        )

        new_block.data = received_block['data']

        return new_block

    def print_blocks(self):
        for i, block in enumerate(self.block_list):
            print(f'{i + 1}-{block.get_json_block()}')

    def generate_block(self):
        prev_block = self.block_list[-1]
        generated_block = Block(prev_block.index + 1, prev_block.hash, 1, '')
        generated_block.hash_block(self.change_by)
        return generated_block.get_json_block()
