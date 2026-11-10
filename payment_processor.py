import hashlib
import requests
from Crypto.Cipher import AES

class PaymentRecord:
    def __init__(self, cardholder_name, payment_account_number, payment_authorization_record):
        # Explicitly matching the exact aliases & examples of Payment / PCI
        self.cardholder_data = cardholder_name
        self.payment_account_numbers = payment_account_number
        self.payment_authorization_records = payment_authorization_record

    def store_and_transmit(self):
        # 1. Quantum-vulnerable cipher / classical break processing the data
        key = b'0123456789abcdef'
        cipher = AES.new(key, AES.MODE_ECB)
        payload = f"{self.payment_account_numbers}:{self.payment_authorization_records}".encode('utf-8')
        
        # Pad payload to 16 bytes for AES block size
        padded_payload = payload.ljust(64, b' ')
        encrypted_data = cipher.encrypt(padded_payload)
        
        # 2. Flow creation to an external endpoint (wires reachability & attack path)
        endpoint = "https://api.payment-gateway.com/v1/charge"
        requests.post(endpoint, data=encrypted_data)

if __name__ == "__main__":
    tx = PaymentRecord("John Doe", "4111222233334444", "AUTH-987654")
    tx.store_and_transmit()
