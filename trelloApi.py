import requests, json, sys

class Board:
    def __init__(self, boards):
        self.id = boards['id']
        self.name = boards['name']

class List:
    def __init__(self, list):
        self.id = list['id']
        self.name = list['name']

class Card:
    def __init__(self, card):
        self.id = card['id']
        self.name = card['name']

class TrelloApiUtil:
#Boards methods
    @staticmethod
    def printAllBoards():
        obj.getAllBoards()
        counter = 1
        for i in obj.boards_list:
           print(str(counter) + " " + i.name)
           counter += 1
    @staticmethod
    def getBoardByIndex(index):
        return obj.boards_list[index]
    
    @staticmethod
    def getBoardNameById(id):
        for el in obj.boards_list:
            if el.id == TrelloApiUtil.getBoardByIndex(id).id:
                return el.name
        return 0  
#Lists methods
    @staticmethod
    def printLists(id):
        obj.getBoardLists(id)
        counter = 1
        for i in obj.lists_list:
           print(str(counter) + " " + i.name)
           counter += 1
    
    @staticmethod
    def getListByIndex(index):
        return obj.lists_list[index]

    @staticmethod
    def getListNameById(id):
        for el in obj.lists_list:
            if el.id == TrelloApiUtil.getListByIndex(id).id:
                return el.name
        return 0  

#Cards methods
    @staticmethod
    def printCards(id):
        obj.getCardLists(id)
        counter = 1
        for i in obj.cards_list:
           print(str(counter) + " " + i.name)
           counter += 1
    
    @staticmethod
    def getCardByIndex(index):
        return obj.cards_list[index]

#Other methods
    @staticmethod
    def errorMessage():
        print("Unknown Option Selected! Enter number again:")


class TrelloApi:
    apiKey = 'a85dfa592080ce7595b9a4be2849b94f'
    token = '0192ff0f5c5004fd3269dc8b5417915e5310481a15189a1eaccfe2e2b574d33b'
    userId = 'userapi32'
    url = 'https://api.trello.com/1/'
    boards_list = []
    lists_list = []
    cards_list = []
    querystring = {"key": apiKey,"token": token}

#Boards methods
    # Get all boards
    def getAllBoards(self):
        self.boards_list = []
        url =  self.url+ 'members/' + self.userId
        querystring = self.querystring
        querystring.update({"boards": 'all'})
        response = requests.request("GET", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for b in json_data['boards']:
                self.boards_list.append(Board(b))
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Create a new board: name - name of the board, defaultLists - determines whether to add the default set of lists to a board
    def createBoard(self, name, defaultLists: True):
        url = self.url + 'boards/'
        querystring = self.querystring
        if defaultLists == False:
            querystring['defaultLists'] = 'false'
        querystring['name'] = name
        response = requests.request("POST", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            self.boards_list.append(Board(json_data))
            print("The board '" + name + "' has been successfully created.")
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Update a board: id - the id of the board to update, name - the new name of the board
    def updateBoard(self, id, name):
        url = self.url + 'boards/' + id
        querystring = self.querystring
        querystring['name'] = name
        response = requests.request("PUT", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for i in self.boards_list:
                if i.id == id:
                    i.name = json_data['name']
                    print("The board '" + name + "' has been successfully updated.")
                    break
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Delete a board: id - the id of the board to delete
    def deleteBoard(self, id):
        url = self.url + 'boards/' + id
        json.dumps(self.querystring)
        response = requests.request("DELETE", url, params=self.querystring)
        if response.status_code == 200:
            for i in self.boards_list:
                if i.id == id:
                    name = i.name
                    self.boards_list.remove(i)
                    print("The board '" + name + "' has been successfully removed.")
                    break
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))
#Lists methods
    # Get board's lists: id - the id of the board
    def getBoardLists(self, id):
        self.lists_list = []
        url = self.url + 'boards/' + id + '/lists'
        querystring = self.querystring
        querystring['filter'] = 'open'
        response = requests.request("GET", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for l in json_data:
                self.lists_list.append(List(l))
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Create a new list in the board: name - the name of the list, idBoard -  the id of the board
    def createList(self, name, idBoard):
        url = self.url + 'lists/'
        querystring = self.querystring
        querystring['idBoard'] = idBoard
        querystring['name'] = name
        response = requests.request("POST", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            self.lists_list.append(List(json_data))
            print("The list '" + name + "' has been successfully created.")
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Update a list: id - the id of the board to update, name - the new name of the board
    def updateList(self, id, name):
        url = self.url + 'lists/' + id
        querystring = self.querystring
        querystring['name'] = name
        response = requests.request("PUT", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for i in self.lists_list:
                if i.id == id:
                    i.name = json_data['name']
                    print("The list '" + name + "' has been successfully updated.")
                    break
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Archive a list: id - the id of the list to archive
    def archiveList(self, id):
        url = self.url + 'lists/' + id
        querystring = self.querystring
        querystring['closed'] = 'true'
        response = requests.request("PUT", url, params=self.querystring)
        if response.status_code == 200:
            for i in self.lists_list:
                if i.id == id:
                    name = i.name
                    self.lists_list.remove(i)
                    print("The list '" + name + "' has been successfully achived.")
                    break
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

#CardsMethods
    # Get list's cards: id - the id of the list
    def getCardLists(self, id):
        self.cards_list = []
        url = self.url + 'lists/' + id + '/cards'
        querystring = self.querystring
        response = requests.request("GET", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for c in json_data:
                self.cards_list.append(Card(c))
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Create a new card in the list: name - the name of the card, idList -  the id of the List
    def createCard(self, name, idList):
        url = self.url + 'cards/'
        querystring = self.querystring
        querystring['idList'] = idList
        querystring['name'] = name
        response = requests.request("POST", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            self.cards_list.append(List(json_data))
            print("The card '" + name + "' has been successfully created.")
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Update a card: id - the id of the card to update, name - the new name of the card
    def updateCard(self, id, name):
        url = self.url + 'cards/' + id
        querystring = self.querystring
        querystring['name'] = name
        response = requests.request("PUT", url, params=querystring)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for i in self.cards_list:
                if i.id == id:
                    i.name = json_data['name']
                    print("The list '" + name + "' has been successfully updated.")
                    break
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))

    # Delete a card: id - the id of the card to delete
    def deleteCard(self, id):
        url = self.url + 'cards/' + id
        response = requests.request("DELETE", url, params=self.querystring)
        if response.status_code == 200:
            for i in self.lists_list:
                if i.id == id:
                    name = i.name
                    self.cards_list.remove(i)
                    print("The list '" + name + "' has been successfully achived.")
                    break
        else:
            print('Error: ' + response.text + ". Code: " + str(response.status_code))


#Create an object of TrelloApi Class
obj = TrelloApi()

mainMenu = {}
mainMenu['1']="Show all boards" 
mainMenu['2']="Create a board"
mainMenu['3']="Update a board name"
mainMenu['4']="Delete a board"
mainMenu['5']="Exit"

createBoardMenu = {}
createBoardMenu['1']="Create a board with default lists(To do, Doing, Done)"
createBoardMenu['2']="Create an empty board"
createBoardMenu['3']="Back to Main Menu"
createBoardMenu['4']="Exit"

ListMenu = {}
ListMenu['1']="Show all lists of the board"
ListMenu['2']="Create an empty list"
ListMenu['3']="Update a list name"
ListMenu['4']="Archive a list"
ListMenu['5']="Return to change a board"
ListMenu['6']="Exit"

CardMenu = {}
CardMenu['1']="Show all cards of the list"
CardMenu['2']="Create a card"
CardMenu['3']="Update a card"
CardMenu['4']="Delete a card"
CardMenu['5']="Return to change a list"
CardMenu['6']="Exit"

# List of boards
def boardsList():
    print("Select a board to work with lists:")
    TrelloApiUtil.printAllBoards()
    if len(obj.boards_list) == 0:
        input("You don't have any boards. Press any key to Quit.\n")
        main()
    else:
        print(len(obj.boards_list) + 1, "Return to the Main Menu")
        print(len(obj.boards_list) + 2, "Quit")
        while(True):
            try:
                board=int(input("Enter a number:"))
                print("")
                if board <= len(obj.boards_list) and board >= 1:
                    listsMenu(board-1)
                elif board == len(obj.boards_list) + 1:
                    main()
                elif board == len(obj.boards_list) + 2:
                    sys.exit(0)
                else:
                    TrelloApiUtil.errorMessage()
            except SystemExit:
                sys.exit(1)
            except:
                TrelloApiUtil.errorMessage()

# Menu Create a board
def createBoard():
    print("*****Create a Board Menu*****")
    options=createBoardMenu.keys()
    sorted(options)
    for entry in options: 
        print(entry, createBoardMenu[entry])
    try:
        selection=int(input("Please Select:"))
        print("")
        if selection == 1: 
            createBoardWithLists()
        elif selection == 2:
            createBoardWithoutLists()
        elif selection == 3:
            main()
        elif selection == 4:
            sys.exit(0)
        else: 
            TrelloApiUtil.errorMessage()
    except SystemExit:
            sys.exit(1)
    except:
        TrelloApiUtil.errorMessage()

# Create a board with default lists
def createBoardWithLists():
    name=input("Please enter a name of the board:")
    obj.createBoard(name, True)
    createBoard()

# Create an empty board
def createBoardWithoutLists():
    name=input("Please enter a name of the board:")
    obj.createBoard(name, False)
    createBoard()

# Update a board
def updateBoard():
    print("Select a board to change a name:")
    TrelloApiUtil.printAllBoards()
    if len(obj.boards_list) == 0:
        input("You don't have any boards. Press any key to Quit.\n")
        main()
    else:
        print(len(obj.boards_list) + 1, "Return to the Main Menu")
        print(len(obj.boards_list) + 2, "Quit")
        while(True):
            try:
                board=int(input("Enter a number:"))
                if board <= len(obj.boards_list) and board >= 1:
                    obj.updateBoard(TrelloApiUtil.getBoardByIndex(board-1).id, input("Please enter a name of the Board:"))
                    print("")
                    main()
                elif board == len(obj.boards_list) + 1:
                    print("")
                    main()
                elif board == len(obj.boards_list) + 2:
                    print("")
                    main()
                else:
                    TrelloApiUtil.errorMessage()
            except:
                TrelloApiUtil.errorMessage()

# Delete a board            
def deleteBoard():
    print("Select a board to delete:")
    TrelloApiUtil.printAllBoards()
    if len(obj.boards_list) == 0:
        input("You don't have any boards. Press any key to Quit.")
        main()
    else:
        print(len(obj.boards_list) + 1, "Return to the Main Menu")
        print(len(obj.boards_list) + 2, "Quit")
        while(True):
            try:
                board=int(input("Enter a number:"))
                print("")
                if board <= len(obj.boards_list) and board >= 1:
                    obj.deleteBoard(TrelloApiUtil.getBoardByIndex(board-1).id)
                    main()
                elif board == len(obj.boards_list) + 1:
                    main()
                elif board == len(obj.boards_list) + 2:
                    sys.exit(0)
                else:
                    TrelloApiUtil.errorMessage()
            except SystemExit:
                sys.exit(1)
            except:
                TrelloApiUtil.errorMessage()

# Main menu
def main():
    print("*****Main Menu*****")
    options=mainMenu.keys()
    sorted(options)
    for entry in options: 
        print(entry, mainMenu[entry])
    while(True):
        try:
            selection=int(input("Please Select:"))
            print("")
            if selection == 1: 
                boardsList()
            elif selection == 2:
                createBoard()
            elif selection == 3:
                updateBoard()
            elif selection == 4:
                deleteBoard()
            elif selection == 5:
                sys.exit(0)
            else: 
                TrelloApiUtil.errorMessage()
        except SystemExit:
            sys.exit(1)
        except:
            TrelloApiUtil.errorMessage()


# ---------------------Work with Lists---------------------
#Lists menu
def listsMenu(indexBoard):
    print("Lists of the '" + TrelloApiUtil.getBoardNameById(indexBoard) + "' board:")
    options=ListMenu.keys()
    sorted(options)
    for entry in options: 
        print(entry, ListMenu[entry])
    try:
        selection=int(input("Please Select:"))
        print("")
        if selection == 1: 
            listsActions(indexBoard, 0)
        elif selection == 2:
            createList(indexBoard)
        elif selection == 3:
            listsActions(indexBoard, 1)
        elif selection == 4:
            listsActions(indexBoard, 2)
        elif selection == 5:
            boardsList()
        elif selection == 6:
            sys.exit(0)
        else: 
            TrelloApiUtil.errorMessage()
    except SystemExit:
            sys.exit(1)
    except:
            TrelloApiUtil.errorMessage()

#General lists method: 0 - Get All lists in the board, 1 - update name of the list, 2 - archive a list
def listsActions(indexBoard, option = 0):
    title = ''
    if option == 0:
        title = 'work with cards'
    elif option == 1:
        title = 'update:'
    elif option == 2:
        title = 'archive:'
    print("Board '"+ TrelloApiUtil.getBoardByIndex(indexBoard).name + "'. Select a list to " + title)
    TrelloApiUtil.printLists(TrelloApiUtil.getBoardByIndex(indexBoard).id)
    listLen = len(obj.lists_list)
    if listLen == 0:
        input("You don't have any lists. Press any key to return to the boards list.\n")
        boardsList()
    else:
        
        print(listLen + 1, "Return to the List Menu")
        print(listLen + 2, "Return to the boards list")
        print(listLen + 3, "Return to the Main Menu")
        print(listLen + 4, "Quit")
        while(True):
            try:
                l = int(input("Enter a number:"))
                if l <= listLen and l >= 1:
                    if option == 0:
                        cardsMenu(l - 1, indexBoard)
                        print("")
                    elif option == 1:
                        obj.updateList(TrelloApiUtil.getListByIndex(l-1).id, input("Please enter a name of the List:"))
                        print("")
                        listsMenu(indexBoard)
                    elif option == 2:
                        obj.archiveList(TrelloApiUtil.getListByIndex(l-1).id)
                        print("")
                        listsMenu(indexBoard)
                    
                elif l == listLen + 1:
                    listsMenu(indexBoard)
                elif l == listLen + 2:
                    boardsList()
                elif l == listLen + 3:
                    main()
                elif l == listLen + 4:
                    sys.exit(0)
                else:
                    TrelloApiUtil.errorMessage()
            except SystemExit:
                sys.exit(1)
            except:
                TrelloApiUtil.errorMessage()

#Create a list
def createList(indexBoard):
    name=input("Please enter a name of the List:")
    obj.createList(name, TrelloApiUtil.getBoardByIndex(indexBoard).id)
    print("")
    listsMenu(indexBoard)

#Cards menu
def cardsMenu(indexList, indexBoard):
    print("Cards of the '" + TrelloApiUtil.getListNameById(indexList) + "' list.")
    options=CardMenu.keys()
    sorted(options)
    for entry in options: 
        print(entry, CardMenu[entry])
    try:
        selection=int(input("Please Select:"))
        print("")
        if selection == 1: 
            cardsActions(indexList, indexBoard, 0 )
        elif selection == 2:
            createCard(indexList, indexBoard)
        elif selection == 3:
            cardsActions(indexList,indexBoard, 1)
        elif selection == 4:
            cardsActions(indexList,indexBoard, 2)
        elif selection == 5:
            listsActions(indexBoard, 0)
        elif selection == 6:
            sys.exit(0)
        else: 
            TrelloApiUtil.errorMessage()
    except SystemExit:
        sys.exit(1)
    except:
        TrelloApiUtil.errorMessage()

#General lists method: 0 - Get All lists in the board, 1 - update name of the list, 2 - archive a list
def cardsActions(indexList, indexBoard, option = 0):
    if option == 0:
        print("Cards of the '" + TrelloApiUtil.getListNameById(indexList) + "' list:")
    elif option == 1:
        print("Select a list to update:")
    elif option == 2:
        print("Select a list to delete:")
    
    TrelloApiUtil.printCards(TrelloApiUtil.getListByIndex(indexList).id)
    listLen = len(obj.cards_list)
    if listLen == 0:
        input("You don't have any cards. Press any key to return to the lists list.\n")
        listsActions(indexBoard, 0)
    else:
        
        print(listLen + 1, "Return to the Cards Menu")
        print(listLen + 2, "Return to the Lists list")
        print(listLen + 3, "Return to the Main Menu")
        print(listLen + 4, "Quit")
        while(True):
            try:
                l = int(input("Enter a number:"))
                if l <= listLen and l >= 1:
                    if option == 0:
                        print("")
                        cardsMenu(indexList, indexBoard)
                    elif option == 1:
                        obj.updateCard(TrelloApiUtil.getCardByIndex(l-1).id, input("Please enter a name of the Card:"))
                        print("")
                        cardsMenu(indexList, indexBoard)
                    elif option == 2:
                        obj.deleteCard(TrelloApiUtil.getCardByIndex(l-1).id)
                        print("")
                        cardsMenu(indexList, indexBoard)
                    
                elif l == listLen + 1:
                    cardsMenu(indexList, indexBoard)
                elif l == listLen + 2:
                    listsActions(indexBoard, 0)
                elif l == listLen + 3:
                    main()
                elif l == listLen + 4:
                    sys.exit(0)
                else:
                    TrelloApiUtil.errorMessage()
            except SystemExit:
                sys.exit(1)
            except:
                TrelloApiUtil.errorMessage()

#Create a list
def createCard(indexList, indexBoard):
    name=input("Please enter a name of the Card:")
    obj.createCard(name, TrelloApiUtil.getListByIndex(indexList).id)
    print("")
    cardsMenu(indexList, indexBoard)

#Main method
if __name__ == "__main__":
    main()