# Everything s assuming that there are no errors anywhere.

import requests
import os

api_key = os.getenv("APIKey")
api_token = os.getenv("APIToken")
board_id = os.getenv("BoardId")

list_of_cards = []

def get_idlist(name):
    """
    Fetches all lists from the trello and find the one that matches the name supplied.

    Returns:
        string: The idList id for the specified name.
    """

    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={api_key}&token={api_token}&cards=open&card_fields=id,name")

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
    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={api_key}&token={api_token}&cards=open&card_fields=id,name,idList")

    list_of_cards.clear()

    #now look for the to_do list
    response_json = response.json()

    for trello_list in response_json:
        list_name = trello_list["name"]
        cards = trello_list["cards"]

        for card in cards:
            # only interested in 'To Do' and 'Done' lists
            if list_name == "To Do" or list_name == "Done":
                item = {
                    "title": card["name"],
                    "id": card["id"],
                    "status": list_name
                }
                list_of_cards.append(item)
    
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
    details = "name=" + title
    details = details + "&pos=top"
    details = details + "&desc=This is a new card"

    response = requests.post(f"https://api.trello.com/1/cards?idList={todo_list}&key={api_key}&token={api_token}&{details}")

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

    response = requests.put(f"https://api.trello.com/1/cards/{id}?key={api_key}&token={api_token}&idList={done_list}")

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

    done_list = get_idlist("To Do")

    response = requests.put(f"https://api.trello.com/1/cards/{id}?key={api_key}&token={api_token}&idList={done_list}")

    status = response.status_code

    return status
