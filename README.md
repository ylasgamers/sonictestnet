- If You Want Reshare, Please Dont Forget Add @ylasgamers Thanks!
- First You Need Like This
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/6iDuOGpDRFCoGCWE4XRXmQ.png)](https://github.com/ylasgamers/sonictestnet)

- After Need Install Extension Python Like This
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/tjRxiDmZSpCQB4qoBPZO8A.png)](https://github.com/ylasgamers/sonictestnet)

- Next Install Requirements On Terminal And Enter
```
python -m pip install -r requirements.txt
```
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/E7Xsc27PQwmpgdiUZNuMVA.png)](https://github.com/ylasgamers/sonictestnet)

- Next Need Edit & Add RPC Url https://devnet.sonic.game On client.py Solathon Package
```
Go File txmultisol.py and Look at from solathon import Client
right click and click go to declaration automatic will go file cleint.py
```
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/6JdOxSgzRPCG6tAVUwIzjg.png)](https://github.com/ylasgamers/sonictestnet)
```
find line 17 and you will found this
ENDPOINTS = (
    "https://api.mainnet-beta.solana.com",
    "https://api.devnet.solana.com",
    "https://api.testnet.solana.com",
)
edit/add rpc https://devnet.sonic.game like this below
ENDPOINTS = (
    "https://api.mainnet-beta.solana.com",
    "https://api.devnet.solana.com",
    "https://api.testnet.solana.com",
    "https://devnet.sonic.game",
)
```
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/VUH4ItHgRryh0Un08j1k-A.png)](https://github.com/ylasgamers/sonictestnet)

- Add List Privatekey On pvkeylist.txt
- Now You Can Run With Command python txmultisol.py On Terminal
- If Success You Will Get Result Like Below
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/BUejC074SjSW4-q1wrZxsQ.png)](https://github.com/ylasgamers/sonictestnet)
