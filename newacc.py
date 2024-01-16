from substrateinterface import SubstrateInterface
import csv

substrate = SubstrateInterface(url="wss://your_archive_node_rpc")

# DOTA deploy at height: 18681972
# DOTA start minting at height: 18681993
# DOTA end minting at height: 18723993
# New accounts check height: 18681900

beforehash = '0x9065360b55bdd6bdb5205decc31f49e10ae14e317ab77406510d25ff9235c191' #Blockhash of height 18681900
afterhash = '0xc8232a39f494cebcd8b28aee4a6ea9e427508d9547851472c04b6c93ab0a3511' #Blockhash of height 18723993

def before(account):
    account_info_before = substrate.query(
        module='System',
        storage_function='Account',
        params=[account],
        block_hash=beforehash
    )
    balance = int(account_info_before['data']['free'].value)/1e10
    return round(balance,2)

def after(account):
    account_info_after = substrate.query(
        module='System',
        storage_function='Account',
        params=[account],
        block_hash=afterhash
    )
    balance = int(account_info_after['data']['free'].value)/1e10
    return round(balance,2)

# Download the balance distribution csv from https://github.com/DOTA-DOT20/genesis_balance
s=[]
with open('balance_distribution.csv','r') as f:
     reader=csv.reader(f)
     for row in reader:
         s.append(row[0])
s.pop(0)

total=0
counter=0
with open("NewAccount.csv","a") as f:
     for i in s:
        f.write(str(i)+',')
        f.write(str(before(i))+',')
        f.write(str(after(i))+',')
        if before(i)==0 and after(i)>0:
            f.write("New\n")
            counter+=1
        else:
            f.write("Old\n")
        total+=1
        print("New Account: "+str(counter)+"\tof Total: "+str(total))
            
