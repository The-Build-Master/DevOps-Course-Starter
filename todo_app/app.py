from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/additem', methods=['POST'])
def additem():
    title = request.form.get('title')
    add_item(title)
    return redirect(url_for('index'))
