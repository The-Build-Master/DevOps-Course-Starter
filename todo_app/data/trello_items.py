import requests
import os

api_key = os.getenv("APIKey")
api_token = os.getenv("APIToken")
board_id = os.getenv("BoardId")

list_of_cards = []

def get_listid(name):
    """
    Fetches all lists from the trello and find the one that matches the name supplied.

    Returns:
        string: The list id for the specified name.
    """

    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={api_key}&token={api_token}&cards=open&card_fields=id,name")

    listid = ""

    return listid

def get_cards():
    """
    Fetches all cards from the trello which are from the 'To Do' or 'Done' lists.

    Returns:
        list: The list of all relevant.
    """
    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={api_key}&token={api_token}&cards=open&card_fields=id,name,idList")

    print("Got the lists\n")

    list_of_cards.clear()
    
    #now look for the to_do list
    response_json = response.json()

    for trello_list in response_json:
        list_name = trello_list["name"]
        cards = trello_list["cards"]

        print("list_name =",list_name)

        for card in cards:
            # only interested in 'To Do' and 'Done' lists
            if list_name == "To Do" or list_name == "Done":
                item = {
                    "title": card["name"],
                    "id": card["id"],
                    "status": list_name
                }
                list_of_cards.append(item)
    
    print("cards =", list_of_cards )
    print("\nall done")    

    return list_of_cards

def add_card(title):
    """
    Adds a new card with the specified title to the 'To Do' list.

    Args:
        title: The title of the card.

    Returns:
        item: The API response.
    """


    todo_list = "6310892eadf7400069d430f5"

    # set up the necessary card details
    details = "name=" + title
    details = details + "&pos=top"
    details = details + "&desc=This is a new card"

    response = requests.post(f"https://api.trello.com/1/cards?idList={todo_list}&key={api_key}&token={api_token}&{details}")

    status = response.json
    return status

