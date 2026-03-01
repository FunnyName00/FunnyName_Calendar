class ShoppingList:

    def __init__(self):
        self.items = []

    def addTask(self, item: Item):
        self.items.append(item)

class Item:

    def __init__(self, date, content):
        self.date = date
        self.content = content

    def getContent(self):
        return self.content
    
    def getDate(self):
        return self.date



list = ShoppingList()
item1 = Item(5, "coucou")
list.addTask(item1)

print(list.items[0].getContent())
