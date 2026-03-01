class GeneralList:

    def __init__(self):
        self.items = []

    def addItem(self, item: GeneralItem):
        self.items.append(item)

    def editItem(self, index: int, content: str):

        if index < 0 or index >= len(self.items):
            print("Index not in list")

        else:
            self.items[index].content = content

    def deleteItem(self, index: int):

        if index < 0 or index >= len(self.items):
            print("Index not in list")
        else:
            self.items.pop(index)

    def print(self):
        print("----------------------------")
        for i in self.items:
            print(i)


class GeneralItem:

    def __init__(self, user, content: str):
        self.user = user
        self.content = content

    def getContent(self):
        return self.content
    
    def getUser(self):
        return self.user

    def __repr__(self):
        return f'{self.getContent()} | {self.getUser()}'


class Activity(GeneralItem):

    def __init__(self, user, content, date, place):
        self.user = user
        self.content = content
        self.date = date
        self.place = place

    def getDate(self):
        return self.date
    
    def getPlace(self):
        return self.place
    
    def __repr__(self):
        return f'{self.getContent()} | {self.getUser()} | {self.getDate()} | {self.getPlace()}'


