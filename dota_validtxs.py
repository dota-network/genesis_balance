# Install the module below first:
# pip install substrate-interface
from substrateinterface import SubstrateInterface
import json
substrate = SubstrateInterface(url="wss://your_archive_node_rpc")

highest = substrate.get_block_number(substrate.get_chain_finalised_head())
#start_block = 18681993
start_block = 18681993
end_block = start_block + 42000


# only keep the first transaction for a certain account
def remove_duplicates(array):
    unique_values = {}
    result = []
    for item in array:
        key = item[0]
        values = item[1:]
        if key not in unique_values:
            unique_values[key] = values
            result.append(item)
    return result

TotalTxs=0
ValidTxs=0

'''
Valid Txs Rules:

1. ['call_function'] = 'batch_all'
2. ['call_module'] = 'Utility'
3. The first call_function = 'transfer_keep_alive'
4. The second call_function ='remark'
5. Remove the spaces in the memo, replace single quotes with double quotes, then convert everything to lowercase
6. The content above should equals to {"p":"dot-20","op":"mint","tick":"dota"}
7. The length of receiver's address >=40 (including SR25519, ED25519 and ECDSA style address)


For a specific account, only the first successful transaction in one block will be accepted.
'''


for block_num in range(start_block, end_block + 1):
    block_hash = substrate.get_block_hash(block_num)
    block = substrate.get_block(block_hash)
    extrinsics = block['extrinsics']
    s=[]
    for extrinsic in extrinsics:
        hash = extrinsic.value['extrinsic_hash']
        text= extrinsic.value['call']
        if (text['call_function'] == 'batch_all' and text['call_module']=='Utility' and len(text['call_args'][0]['value'])==2 and text['call_args'][0]['value'][0]['call_function']=='transfer_keep_alive' and text['call_args'][0]['value'][1]['call_function']=='remark' and text['call_args'][0]['value'][1]['call_args'][0]['value'].replace(" ","").replace("\'","\"").lower()=='{\"p\":\"dot-20\",\"op\":\"mint\",\"tick\":\"dota\"}' and len(text['call_args'][0]['value'][0]['call_args'][0]['value'])>=40):
            s.append([text['call_args'][0]['value'][0]['call_args'][0]['value'],block_num,hash])
    addr=remove_duplicates(s)
    TotalTxs = TotalTxs + len(s)
    ValidTxs = ValidTxs + len(addr)
    with open("validtxs_"+str(start_block)+"-"+str(end_block)+".csv","a") as f:
        unique_addr = len(addr)
        for i in addr:
            f.write(str(i[0])+',')
            f.write(str(i[1])+',')
            f.write(str(i[2])+',')
            f.write(str(int(5000000/unique_addr))+'\n')
    print(str(block_num)+" txs:"+str(len(s))+" valid:"+str(len(addr))+" Totaltxs:"+str(TotalTxs)+" Totalvalid:"+str(ValidTxs))