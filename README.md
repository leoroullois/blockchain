# Fake Blockchain implementation

## Installation

Clone the repository :

```bash
git clone https://github.com/leoroullois/blockchain.git && cd blockchain
```

Start the server on your machine :
```bash
docker compose up -d
```

The server will listen on `http://localhost:5000`.

## API

There is different routes to interact with the blockchain :

- **POST** `/mine_block`: Mine a block
![Mine block](./images/mine_block_body.png)
![Mine block](./images/mine_block.png)


- **GET** `/get_chain` : returns all the blocks of the blockchain
![Get chain](./images/get_chain.png)


- **GET** `/valid` : Checks if the blockchain is valid
![Valid](./images/valid.png)


- **GET** `/create-fake-block` : Create a fake non-valid block
![Create fake block](./images/create-fake-block.png)

- **GET** `/peers` : Show number of peers
![Peers](./images/peers.png)

## MCL

**MCL** library and his python wrapper is installed by default in the docker container. 

For testing if the library is successfully installed, run this command :

```bash
cd /app/mcl && chmod +x tests.sh && ./tests.sh
```

Before importing something from the library, you need to set this code :
```python
import sys
sys.path.insert(1, "/lib/mcl-python/")
```


## Development

After making changes in the codebase you need to restart the server with this command:

```bash
docker compose restart
```

To see container logs, type :

```bash
docker compose logs -f blockchain
```
