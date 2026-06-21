
import configparser
import os

def load_config(filename="config.ini"):
    config = configparser.ConfigParser()
    if not os.path.exists(filename):
        config["Settings"] = {
            "rpc_url": "https://arb1.arbitrum.io/rpc",
            "wallet_address": "0xYourWalletAddress",
            "private_key": "your_private_key",
            "telegram_bot_token": "your_bot_token",
            "telegram_chat_id": "your_chat_id",
            "min_profit": "0.5",
            "slippage": "0.5",
            "scan_interval": "10"
        }
        with open(filename, "w") as f:
            config.write(f)
    else:
        config.read(filename)
    return config["Settings"]
