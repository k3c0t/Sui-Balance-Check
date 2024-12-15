from multiprocessing.dummy import Pool
from sui_python_sdk.wallet import SuiWallet
import os
import sys
import json
import requests
class bingo:
    @staticmethod
    def toFile(text):
        with open("all.txt", "a+") as file:
                file.write(text)
def main(seed):
    try:
        
        my_wallet = SuiWallet(mnemonic=seed)
        a = my_wallet.get_address()
        url = "https://api.blockvision.org/v2/sui/account/coins?account="+ a
        headers = {
    "accept": "application/json",
    "x-api-key": "YOUR-API-KEY-FROM-BLOCKVISION"
}
        response = requests.get(url, headers=headers)
        #print(response.text)
        users = json.loads(response.text)
            
        for dt in users["result"]['coins']:
                dtt = dt["balance"]
                ct = dt['coinType']
                all = f"{seed}\n{a}\n{ct} : {dtt}\n\n\n"
                if '0x0000000000000000000000000000000000000000000000000000000000000002::sui::SUI' in dt['coinType']:
                    dtt = dt["balance"]

                    balances = int(dtt) / 100000000
                    print(f"\n\033[91m [+] \033[97m=====================================================\033[91m [+]")
                    print(f"\033[92m   ┌──[+]\033[93m SUI ")
                    print(f"\033[92m   └─$\033[93m {balances} | {dtt}") 
                    with open("sui.txt", "a") as wr:
                        wr.write(all + "\n")
            
                if '0x506a6fc25f1c7d52ceb06ea44a3114c9380f8e2029b4356019822f248b49e411::memefi::MEMEFI' in dt['coinType']:
                    dtt = dt["balance"]

                    balances = int(dtt) / 100000000
                    print(f"\n\033[91m [+] \033[97m=====================================================\033[91m [+]")
                    print(f"\033[92m   ┌──[+]\033[93m MEMEFI ")
                    print(f"\033[92m   └─$\033[93m {balances} | {dtt}")
                    with open("memefi.txt", "a") as wr:
                        wr.write(all + "\n")
                if '0xa8816d3a6e3136e86bc2873b1f94a15cadc8af2703c075f2d546c2ae367f4df9::ocean::OCEAN' in dt['coinType']:
                    dtt = dt["balance"]

                    balances = int(dtt) / 100000000
                    print(f"\n\033[91m [+] \033[97m=====================================================\033[91m [+]")
                    print(f"\033[92m   ┌──[+]\033[93m OCEAN ")
                    print(f"\033[92m   └─$\033[93m {balances} | {dtt}")
                    with open("ocean.txt", "a") as wr:
                        wr.write(all + "\n")



                bingo.toFile(f"{seed}\n{a}\n{ct} : {dtt}\n\n\n")
    except Exception as e:
        print(str(e))
        #pass

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r', encoding="utf8", errors='ignore').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <'+path[len(path)-1] + '> <sites.txt>')
mp = Pool(10)
mp.map(main, target)
mp.close()
mp.join()
