class GeneralList:

    def __init__(self):
        self.items = []

    def addItem(self, item: GeneralItem):
        self.items.append(item)

    def editItem(self, index: int, content: str):

        if index < 0 or index > len(self.items):
            print("Index not in list")

        else:
            self.items[index].content = content

    def ListPrint(self):
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

    def __repr__(self):
        return f'{self.content} | {self.user} | {self.date} | {self.place}'


list = GeneralList()
item1 = GeneralItem("Papa", "Manger :3")
item2 = GeneralItem("Maman", "PQ")

list.addItem(item1)
list.addItem(item2)
list.ListPrint()

list.editItem(0, "J'ai été édité :)")
list.ListPrint()

activity1 = Activity("Papa", "ENORME TEUFFFFF", "05/03/26", "Louvain la neuve")
list.addItem(activity1)
list.ListPrint()

