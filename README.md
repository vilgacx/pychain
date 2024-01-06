# pychain

#### PoW blockchain written in python.

##### Example
- `cd pychain`
- run a node of port **8080** with **no peer** by following command:<br>
`make serve port=8080 peer=None`
- run a 2nd node of port **7575** connecting **peer 8080** by following command:<br>
`make serve port=7575 peer=127.0.0.1:8080`
- run a 3rd node of port **6969** connecting **peer 7575** by following command:<br>
`make serve port=6969 peer=127.0.0.1:7575`

**that's it, you are running a blockahin of containing three nodes.**<br>
*(add block to see syncing changes)*<br>
you can add more nodes by connecting it to peers of already running chain or simply run another blockchain by peer as **None**.

##### API endpoints
- to see chain `/`
- to add block `/add?nonce=<any-number>/data=<any-data>`
- to see connected peers `/nodes`
