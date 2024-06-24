from solathon import Client, Transaction, PublicKey, Keypair
#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()

print("Auto Generate Wallet Solana With Privatekey | @ylasgamers")
loop = input("How Many You Want To Generate Wallet ? : ")
for i in range(0,int(loop)):
    keyreceiver = Keypair() #generate random privatekey
    log('Address : '+keyreceiver.public_key) #log address
    log('Privatekey : '+keyreceiver.private_key) #log privatekey
    log('-------------------'+str(i)+'-------------------')
    print('Address : ',keyreceiver.public_key) #print address
    print('Privatekey : ',keyreceiver.private_key) #print privatekey
    print('-------------------',str(i),'-------------------')
