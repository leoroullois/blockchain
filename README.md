# Fake Blockchain implementation

## Installation

Clone the repository :

```bash
git clone .... && cd blockchain
```

Start the server :
```bash
python3 main.py
```

The server will listen on `http://localhost:5000`.

There is different routes :

- `/mine_block` : Mine a block
![Mine block](./images/mine_block.png)
- `/get_chain` : returns all the blocks of the blockchain
![Get chain](./images/get_chain.png)
- `/valid` : Checks if the blockchain is valid
![Valid](./images/valid.png)
- `/create-fake-block` : Create a fake non-valid block
![Create fake block](./images/create-fake-block.png)