from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair
from solathon.utils import clean_response, lamport_to_sol, sol_to_lamport
import time
import secrets
import random

#client = Client("https://rpc.solscan.com") #mainnet
#client = Client("https://api.testnet.solana.com") #testnetㅤ
#client = Client("https://api.devnet.solana.com") #devnet
client = Client("https://devnet.sonic.game")

def getbal(sender):
    balance = client.get_balance(sender)
    tosol = lamport_to_sol(balance)
    print("Your Balance : ",tosol, "SOL")
    print("")

def tx_sol(sender, keysender, receiver, value):
    instruction = transfer(
        from_public_key=sender,
        to_public_key=receiver, 
        lamports=int(value) #https://www.solconverter.com/
    )

    transaction = Transaction(instructions=[instruction], signers=[keysender])

    result = client.send_transaction(transaction)
    print(sender," Send ",lamport_to_sol(value)," SOL To ",receiver)
    print("Transaction ID : ", result)
    getbal(sender)
    print("Transaction Will Continue For 3 Second...")
    time.sleep(3)

print("Auto Send Random Solana To Random Address | @ylasgamers")
loop = input("How Many You Want To Transaction ? : ")
for i in range(0,int(loop)):
    with open('pvkeylist.txt', 'r') as file:
        local_data = file.read().splitlines()
        for pvkeylist in local_data:
            # Requires you to have some SOLs to pay for transaction fees
            keysender = Keypair().from_private_key(pvkeylist)
            sender = keysender.public_key
            keyreceiver = Keypair() #generate random pvkey
            receiver = keyreceiver.public_key
            inputval = random.uniform(0.001, 0.005)
            value = sol_to_lamport(inputval)
            tx_sol(sender, keysender, receiver, value)
