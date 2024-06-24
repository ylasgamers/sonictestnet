from solathon import Client, Transaction, PublicKey, Keypair
#log to txt file
def log(txt):
    f = open(__file__ + '.log', "a")
    f.write(txt + '\r\n')
    f.close()
  
keyreceiver = Keypair() #generate random privatekey
log('Address : '+keyreceiver.public_key) #log address
log('Privatekey : '+keyreceiver.private_key) #log privatekey
print('Address : ',keyreceiver.public_key) #print address
print('Privatekey : ',keyreceiver.private_key) #print privatekey
