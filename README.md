### Trello Api
Trello API is a python console-based application that allows you to perform basic operations in your Trello.com account: Boards, Lists, Cards actions. It has an intuitive menu that is easy to use. It is designed with extensibility in mind. 
### Features
1. Boards functionality:
1.1. Create a board
1.2. Update board name
1.3. Delete a board
1.4. Show all boards
2. Lists functionality:
2.1. Create a list in the board
2.2. Update a list name in the board
2.3. Archive a list in the board
2.4. Show all lists in the board
3. Cards functionality:
3.1. Create a card in the list
3.2. Update a card in the list
3.4. Delete a card from the list
3.5. Show all cards in the list
### Getting Started
To run the application you should have installed **python 3.6** or newer and installed packages: **requests, json, sys** or [python online interpreter](https://repl.it/languages/python3).
To install packages use commands:
```
pip install requests
pip install json
pip install sys
```
To run the application use a command:
`python pathToTheFile\trelloApi.py`
For the demonstration, the application uses pre-created Trello account with a prefilled test data: 
```
User: treelloapi102719@gmail.com
Password: umT^c8#{F\e35mL[
```
Using Trello API required to have API-key and token. This information has been received from the website https://developers.trello.com. These parameters and a user id should be determined in the trelloApi.py:
```
apiKey = 'a85dfa592080ce7595b9a4be2849b94f'
token = '0192ff0f5c5004fd3269dc8b5417915e5310481a15189a1eaccfe2e2b574d33b'
userId = 'userapi32'
```
