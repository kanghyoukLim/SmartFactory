class BOMItem:
    def __init__(self, part_number, quantity, children=None):
        self.part_number = part_number
        self.quantity = quantity
        self.children = children or []

class BOM:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)