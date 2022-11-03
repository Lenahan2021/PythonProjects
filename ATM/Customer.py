class Customer:
    def __init__(self, name, checking, saving, card, pin):
        self.name = name
        self.checking = int(checking)
        self.saving = int(saving)
        self.card = int(card)
        self.pin = int(pin)

    def __str__(self) -> str:
        return self.name + self.card + self.pin

