# Everything is assuming that there are no errors anywhere.

import requests
import os
from .class_item import Item

def api_key():
    return os.getenv("APIKey")

def api_token():
    return os.getenv("APIToken")

def board_id():
    return os.getenv("BoardId")

def get_idlist(name):
    """
    Fetches all lists from the trello and find the one that matches the name supplied.

    Returns:
        string: The idList id for the specified name.
    """

    response = requests.get(f"https://api.trello.com/1/boards/{board_id()}/lists?key={api_key()}&token={api_token()}&cards=open&card_fields=id,name")

    idlist = ""

    #now look for the to_do list
    response_json = response.json()

    for trello_list in response_json:
        if trello_list["name"] == name:
            idlist = trello_list["id"]
            break

    return idlist

def get_cards():
    """
    Fetches all cards from the trello which are from the 'To Do' or 'Done' lists.

    Returns:
        list: The list of all relevant.
    """
    
    list_of_cards = []

    response = requests.get(f"https://api.trello.com/1/boards/{board_id()}/lists?key={api_key()}&token={api_token()}&cards=open&card_fields=id,name,idList")

    #now look for the to_do list
    response_json = response.json()

    for trello_list in response_json:
        list_name = trello_list["name"]
        cards = trello_list["cards"]

        for card in cards:
            # only interested in 'To Do' and 'Done' lists
            if list_name == "To Do" or list_name == "Done":
                list_of_cards.append(Item.from_trello_card(card, trello_list)) 
                
    return list_of_cards

def add_card(title):
    """
    Adds a new card with the specified title to the 'To Do' list.

    Args:
        title: The title of the card.

    Returns:
        item: The API response.
    """

    todo_list = get_idlist("To Do")

    # set up the card details as required
    body = {
        'name': title,
        'pos': 'top',
        'desc': 'This is a new card',
        'key': api_key,
        'token': api_token,
        'idList': todo_list
    }
    
    response = requests.post("https://api.trello.com/1/cards", data = body)

    status = response.status_code

    return status

def update_card_done(id):
    """
    Updates the card with the specified id to the 'Done' list.

    Args:
        id: The id of the card.

    Returns:
        item: The API response.
    """

    done_list = get_idlist("Done")

    response = requests.put(f"https://api.trello.com/1/cards/{id}?key={api_key()}&token={api_token()}&idList={done_list}")

    status = response.status_code

    return status

def update_card_todo(id):
    """
    Updates the card with the specified id to the 'To Do' list.

    Args:
        id: The id of the card.

    Returns:
        item: The API response.
    """

    todo_list = get_idlist("To Do")

    response = requests.put(f"https://api.trello.com/1/cards/{id}?key={api_key()}&token={api_token()}&idList={todo_list}")

    status = response.status_code

    return status
