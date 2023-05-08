class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paying {amount} using credit card {self.card_number}")


class PayPalStrategy(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"Paying {amount} using PayPal account {self.email}")


class BankTransferStrategy(PaymentStrategy):
    def __init__(self, account_number, routing_number):
        self.account_number = account_number
        self.routing_number = routing_number

    def pay(self, amount):
        print(f"Paying {amount} using bank transfer from account {self.account_number}")


class Order:
    def __init__(self, amount, payment_strategy):
        self.amount = amount
        self.payment_strategy = payment_strategy

    def process_payment(self):
        self.payment_strategy.pay(self.amount)


if __name__ == "__main__":
    amount = 100
    credit_card_strategy = CreditCardStrategy("1234 5678 9012 3456", "12/24", "123")
    order = Order(amount, credit_card_strategy)
    order.process_payment()
