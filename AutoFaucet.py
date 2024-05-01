import random
import time
import requests

# Define the list of accounts for rotation
accounts = [
    "0x8ba89572a84b851b8e015d3921bb32686f66b7c2",
    "0x88192b0a7f8c63099774a646a46e8886e2332233",
    "0x917ad046e24daec3196610d8a2c5f2b9f0b6360f"
]

# Function to send POST request
def faucet_request(account):
    url = "https://mevm.devnet.m1.movementlabs.xyz/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://faucet.movementlabs.xyz",
        "Referer": "https://faucet.movementlabs.xyz",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_faucet",
        "params": [account]
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Main loop to execute the function every 5 seconds, rotating accounts randomly
try:
    while True:
        selected_account = random.choice(accounts)
        result = faucet_request(selected_account)
        print(f"Requested for account {selected_account}: {result}")
        time.sleep(0.5)  # Wait for 5 seconds before the next request
except KeyboardInterrupt:
    print("Program terminated by user.")
except Exception as e:
    print(f"An error occurred: {e}")
