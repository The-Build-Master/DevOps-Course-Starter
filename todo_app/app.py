from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from todo_app.flask_config import Config

from todo_app.data.trello_items import get_cards, add_card, update_card

from operator import itemgetter, attrgetter

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_cards()
    # sort the items before displaying them
    items = sorted(items, key=lambda x: x['status'], reverse=True)
    return render_template('index.html', items=items)

@app.route('/additem', methods=['POST'])
def additem():
    title = request.form.get('title')
    add_card(title)
    return redirect(url_for('index'))

@app.route('/completeitem', methods=['POST'])
def completeitem():
    id = request.form.get('id')
    update_card(id)
    return redirect(url_for('index'))


