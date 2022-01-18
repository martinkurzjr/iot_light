# interact with contract web3 only
from web3 import Web3

# rom solcx import compile_standard, install_solc
# import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

w3 = Web3(
    Web3.HTTPProvider("https://ropsten.infura.io/v3/9cfee390074a4c3e9d08ea3c4938aa99")
)
connection_established = w3.isConnected()
print(f"Connection is established {connection_established}.")


chain_id = 3
my_address = "0x47106e27177592632C9AB08E75EA201b7Cb37e24"
private_key = os.getenv("PRIVATE_KEY")

abi = [
    {
        "inputs": [],
        "name": "light",
        "outputs": [
            {"internalType": "uint256", "name": "red", "type": "uint256"},
            {"internalType": "uint256", "name": "green", "type": "uint256"},
            {"internalType": "uint256", "name": "blue", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_r", "type": "uint256"},
            {"internalType": "uint256", "name": "_g", "type": "uint256"},
            {"internalType": "uint256", "name": "_b", "type": "uint256"},
        ],
        "name": "set_light",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

etherscan_token = os.getenv("ETHERSCAN_TOKEN")

abi_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address=0x4733c0262f381E7C6DD061Ab2863c3bF328c7Bb7&apikey={etherscan_token}"
response = requests.get(abi_url)
abi_json = response.json()
print(abi_json)

iot_light = w3.eth.contract("0x4733c0262f381E7C6DD061Ab2863c3bF328c7Bb7", abi=abi)
# print(iot_light.abi)
rgb = iot_light.functions.light().call()
print(rgb)
