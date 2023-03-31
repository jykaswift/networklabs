import json
import logging
import os
import threading
import time
import grequests
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request
from gevent import monkey

monkey.patch_all()
load_dotenv(find_dotenv())


def startProcess(process_id, node):
    process = Flask(__name__)

    all_ports = [os.environ.get("PORT1"), os.environ.get("PORT2"), os.environ.get("PORT3")]
    node_port = all_ports[process_id]

    host = os.environ.get("HOST")
    logging.getLogger('werkzeug').disabled = True

    urls = [f'http://{host}:{all_ports[0]}/', f'http://{host}:{all_ports[1]}/', f'http://{host}:{all_ports[2]}/']

    def generateBlock():
        while True:
            if len(node.block_list) != 0:
                generated_block = node.generate_block()
                req = (grequests.post(u, json=generated_block, headers={"port": str(process_id)}) for u in urls)
                grequests.map(req)
            time.sleep(0.1)

    @process.route("/", methods=['POST'])
    def block_handler():

        port = request.headers['port']
        received_block = request.get_json()
        dictionary_block = json.loads(received_block)
        if not node.receive_block(dictionary_block, port):
            return "This block already exist"
        return "Block was inserted"

    server = threading.Thread(target=process.run, args=(host, node_port))
    generator = threading.Thread(target=generateBlock)
    server.setDaemon(False)
    generator.setDaemon(False)
    server.start()
    generator.start()

    if process_id == 0:
        time.sleep(2)
        genesis = node.get_genesis()
        rs = (grequests.post(u, json=genesis, headers={"port": str(process_id)}) for u in urls)
        grequests.map(rs)
