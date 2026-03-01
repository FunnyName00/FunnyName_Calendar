from ListFunctions import *

list = GeneralList()
item1 = GeneralItem("Papa", "Manger :3")
item2 = GeneralItem("Maman", "PQ")

list.addItem(item1)
list.addItem(item2)
list.print()

activity1 = Activity("Papa", "ENORME TEUFFFFF", "05/03/26", "Louvain la neuve")
list.addItem(activity1)
list.print()

list.deleteItem(0)

list.print()