# pychain

### PoW blockchain written in python.

#### Feauters
- Uses PoW for mining/adding blocks.
- Decentralized, peer-to-peer.
- A really simple consensus algorithm.
- Mining difficulty is proportional to number of nodes.
- A node updating algorithm that maintains peer-to-peer connections & consensus with all nodes.

#### Setup
- `cd pychain/`
- execute `pip install -r requirements.txt`

#### Example
- run a node of port **8080** with **no peer** by executing following command:<br>
`make serve port=8080 peer=None`
- run 2nd node of port **7575** connecting **peer 8080** by executing following command:<br>
`make serve port=7575 peer=127.0.0.1:8080`
- run 3rd node of port **6969** connecting **peer 7575** by executing following command:<br>
`make serve port=6969 peer=127.0.0.1:7575`
<br>

**that's it, you are running a blockahin of containing three nodes.**<br>
***(add block to see syncing changes)***<br>
you can add more nodes by connecting it to peers of already running chain or simply run another blockchain by peer as **None**.

#### API endpoints
- to see chain `/`
- to add block `/add?nonce=<any-number>/data=<any-data>` (adds block then redirects to `/`)
- to see connected peers `/nodes`
