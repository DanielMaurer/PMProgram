
class Order():

    # Order constructor
    def __init__(self, orderNumber, parts, subcontractor):
        self.orderNumber = orderNumber
        self.parts = parts
        self.subconstractor = subcontractor

    # Functions for the order
    def editOrderNumber(self, orderNumber):
        self.orderNumber = orderNumber

    def editOrderParts(self, parts):
        self.parts = parts