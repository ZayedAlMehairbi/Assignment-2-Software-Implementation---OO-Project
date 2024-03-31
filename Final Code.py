# Define the Visitor class
class Visitor:
    def __init__(self, name, age, nationality, id_number):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.id_number = id_number

# Define the Ticket class
class Ticket:
    def __init__(self, visitor, event, price):
        self.visitor = visitor
        self.event = event
        self.price = price

# Define the TicketPurchase class
class TicketPurchase:
    def __init__(self):
        self.tickets = []

    def purchaseTicket(self, visitor, event, price):
        ticket = Ticket(visitor, event, price)
        self.tickets.append(ticket)

    def generatePaymentReceipt(self):
        total_price = sum(ticket.price for ticket in self.tickets)
        receipt = "Payment Receipt:\n"
        for ticket in self.tickets:
            receipt += f"Visitor: {ticket.visitor.name}, Event: {ticket.event}, Price: {ticket.price:.2f} AED\n"
        receipt += f"Total: {total_price:.2f} AED\n"
        return receipt

# Define test cases
def runTestCases():
    # Create instances for test cases
    visitor1 = Visitor("John Doe", 30, "American", "1234567890")
    visitor2 = Visitor("Jane Doe", 25, "British", "0987654321")
    ticket_purchase = TicketPurchase()

    # Test case 1: Purchase tickets
    ticket_purchase.purchaseTicket(visitor1, "Renaissance Art Exhibition", 63.00)
    ticket_purchase.purchaseTicket(visitor2, "Musical Concert", 100.00)

    # Test case 2: Generate payment receipt
    receipt = ticket_purchase.generatePaymentReceipt()
    assert "John Doe" in receipt
    assert "Jane Doe" in receipt
    assert "Renaissance Art Exhibition" in receipt
    assert "Musical Concert" in receipt
    assert "163.00" in receipt

    print("All test cases passed successfully!")

def main():
    # Run test cases
    runTestCases()

if __name__ == "__main__":
    main()
