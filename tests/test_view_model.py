from todo_app.data.class_item import Item
from todo_app.data.view_model import ViewModel

def test_done_items_property_only_shows_done_items():
    # Arrange
    items = [
        Item(1, "My Todo", "To Do"),
        Item(2, "My Done", "Done")
    ]
    view_model = ViewModel(items)
    
    # Act
    returned_done_items = view_model.done_items
    
    # Assert
    assert len(returned_done_items) == 1
    item = returned_done_items[0]
    assert item.id == 2
    assert item.status == "Done"

def test_done_items_property_only_shows_todo_items():
    # Arrange
    items = [
        Item(1, "My To Do", "To Do"),
        Item(2, "My Done", "Done")
    ]
    view_model = ViewModel(items)
    
    # Act
    returned_todo_items = view_model.todo_items
    
    # Assert
    assert len(returned_todo_items) == 1
    item = returned_todo_items[0]
    assert item.id == 1
    assert item.status == "To Do"
