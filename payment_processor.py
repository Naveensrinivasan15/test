import hashlib
import urllib.request

class PaymentRecord:
    def __init__(self):
        # Exact alias strings from Payment / PCI classification
        self.cardholder_data = "John Doe"
        self.payment_account_numbers = "4111222233334444"
        self.payment_authorization_records = "AUTH_98765"

    def process_and_send(self):
        # 1. Use hashlib SHA1 (already proven to be recognized as 'Classically broken' by your scanner)
        payload = f"{self.payment_account_numbers}:{self.payment_authorization_records}".encode('utf-8')
        hashed_token = hashlib.sha1(payload).hexdigest()

        # 2. Standard outbound network call to generate the endpoint flow
        url = "https://api.payment-gateway.com/v1/charge"
        req = urllib.request.Request(url, data=hashed_token.encode('utf-8'), method='POST')
        try:
            urllib.request.urlopen(req, timeout=1)
        except Exception:
            pass

if __name__ == "__main__":
    p = PaymentRecord()
    p.process_and_send()
