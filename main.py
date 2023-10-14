from api.api import Api
from blockchain.Blockchain import Blockchain
from blockchain.Node import Node

def main():
    blockchain = Blockchain()

    NB_OF_NODES = 3
    nodes = [Node(blockchain, i) for i in range(NB_OF_NODES)]

    api = Api(blockchain, nodes)
    api.start()

if(__name__ == "__main__"):
    main()
