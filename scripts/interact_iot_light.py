from brownie import Contract
from scripts.helpful_scripts import get_account


def interact_iot_light():
    account = get_account()
    print(f"I got account {account} .")
    contract = Contract.from_explorer("0x4733c0262f381E7C6DD061Ab2863c3bF328c7Bb7")
    # iot_light = IotLight
    # rgb_new = iot_light.light()  # get value
    tx = contract.set_light(1, 10, 10, {"from": account})
    rgb = contract.light()
    print(rgb)


def main():
    interact_iot_light()
