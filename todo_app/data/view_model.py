from todo_app.data.class_item import Item
from typing import List

class ViewModel:
    def __init__(self, items: List[Item]):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        list_of_items = []
        for item in self._items:
            if item.status == "To Do":
                list_of_items.append(item)
        
        return list_of_items


    @property
    def done_items(self):
        list_of_items = []
        for item in self._items:
            if item.status == "Done":
                list_of_items.append(item)
        
        return list_of_items

