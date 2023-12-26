## Valid Txs Rules:

1. ['call_function'] = 'batch_all'
2. ['call_module'] = 'Utility'
3. The first call_function = 'transfer_keep_alive'
4. The second call_function ='remark'
5. Remove the spaces in the memo, replace single quotes with double quotes, then convert everything to lowercase
6. The content above should equals to {"p":"dot-20","op":"mint","tick":"dota"}
7. The length of receiver's address >=40 (including SR25519, ED25519 and ECDSA style address)


For a specific account, only the first successful transaction in one block will be accepted.


## How to use the script

1. Deploy a polkadot archive node or use [quicknode rpc endpoint](https://dashboard.quicknode.com/endpoints/new/DOT/dot-mainnet)
2. Copy your WSS Provider and replace the code **"wss://your_archive_node_rpc"** in line 5
3. Install the polkadot python SDK with command **pip install substrate-interface**
4. Run **python dota_validtxs.py** to get the raw transaction data


## Data Sample

**validtxs_18681993-18723993.csv**

| Address                     | BlockNumber | Txhash                                                              | BlockReward |
|-----------------------------|-------------|---------------------------------------------------------------------|-------------|
| 13T28S52mt9aJeoQpzHHxq1LEcwDaK9iTMERJsdK2Tqvftfo | 18681993    | 0x095d41d1065009f9fdac2cecd53a25cc777fce3d199758032d32cb13125fe323 | 1250000     |
| 13zxn7P47i7DdqoWpEtBpzXbRCuoWPkKFeeK3ybrJJ2Sf9ZB | 18681993    | 0x36d53056b1efd1965b897e7483c1188ef841748c2cdfcf32174ffdea1badef0c | 1250000     |
| 12hCcj6gkKC1LJPQG2AKU2Xp8VRypEAyLnrkjnxSaxpbqVbr | 18681993    | 0x080edf4694d64f026ddbd600749d2a3de97a01d17caf4a12dabeaeb7edbf1211 | 1250000     |
| 1HoogQbGJgwTvb4remDCP3r4aqavs9kc7AvoNKTFQUWiMLj | 18681993    | 0xb0f5f2412354e2ddbae246b52d5682241a0efc97b11e7f400b6c9403b2de8800 | 1250000     |


## Data Analysis

**txs_distribution.csv**

| Address                      | Txs   |
|------------------------------|-------|
| 14run12UGeiHbKUqyjWpimrcZVbHTqRmgRQFsNnb2gCBbKL4 | 25792 |
| 12gmSc1vsBP9R7HHJ7SCLH1vNf6VX9idPS34hVU2Ebf8f5xr | 25765 |
| 14p9Q8XRbHDDfQeRoTUiNirUfCNfobUpV31R9R1YKzdDRoh4 | 22350 |
| 14MoEZEfDFT288j32zc2mFtYfjAZ4GHC9FGufNG77Xo35U7W | 22276 |
| 13g9eihumxbGCzsJ9KjwstbcsTgYiCNxznLVL5fvkjhqwU1D | 21785 |
| 15yeTtooRJkDHmC893x4g2dJP24UjFcE3LUDUkbr8NBQp335 | 21527 |
| 1jTTwqGQBn3MZ8XXAQsoW1ojMBWAvAoLTPwnZHv9uDdi17Z | 20903 |
| 16ZoEQ5ehQTX4Nmy83VUrSwJRzX1MSA9ACd57CSro8kmJpUx | 20187 |
| 16LmQ2SA61meahghcVtyd5MfLhH9mgGxJSukH5AmeLkSP7DS | 20074 |


**balance_distribution.csv**

| Address                      | Tick | Reward    |
|------------------------------|------|-----------|
| 1HBw3uYqzmFXnxjrKtrAHURfJSDG5rU4j3KFR5FgchBiGmR | DOTA | 383233600 |
| 12gmSc1vsBP9R7HHJ7SCLH1vNf6VX9idPS34hVU2Ebf8f5xr | DOTA | 306645802 |
| 14run12UGeiHbKUqyjWpimrcZVbHTqRmgRQFsNnb2gCBbKL4 | DOTA | 305979642 |
| 14p9Q8XRbHDDfQeRoTUiNirUfCNfobUpV31R9R1YKzdDRoh4 | DOTA | 280908195 |
| 13g9eihumxbGCzsJ9KjwstbcsTgYiCNxznLVL5fvkjhqwU1D | DOTA | 268995758 |
| 14MoEZEfDFT288j32zc2mFtYfjAZ4GHC9FGufNG77Xo35U7W | DOTA | 265659878 |
| 15yeTtooRJkDHmC893x4g2dJP24UjFcE3LUDUkbr8NBQp335 | DOTA | 260518793 |
| 1HoogQbGJgwTvb4remDCP3r4aqavs9kc7AvoNKTFQUWiMLj | DOTA | 256077434 |
