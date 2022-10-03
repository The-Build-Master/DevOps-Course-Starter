from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from todo_app.flask_config import Config

from todo_app.data.trello_items import get_cards, add_card, update_card_done, update_card_todo

from operator import itemgetter, attrgetter

# from todo_app.data.class_item import Item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_cards()
    # sort the items before displaying them
    # items = sorted(items, key=lambda x: x['status'], reverse=True)
    return render_template('index.html', items=items)

@app.route('/additem', methods=['POST'])
def additem():
    title = request.form.get('title')
    add_card(title)
    return redirect(url_for('index'))

@app.route('/completeitem', methods=['POST'])
def completeitem():
    id = request.form.get('id')
    update_card_done(id)
    return redirect(url_for('index'))

@app.route('/uncompleteitem', methods=['POST'])
def uncompleteitem():
    id = request.form.get('id')
    update_card_todo(id)
    return redirect(url_for('index'))

#@app.route('/completecard', methods=['POST'])
#def completecard():
#    id = request.args['id']
#    status = request.args['status']

    # if status == 'To Do':
    #     update_card_done(id)
    # else:
    #     update_card_todo(id)
    
    # return redirect(url_for('index'))