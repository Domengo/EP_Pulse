"""_summary_

    Returns:
        _type_: _description_
    """
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('index.html', title='EPL Pulse',
                           heading='Welcome', content='This is my first epl!',
                           host="0.0.0.0", port=3006)


@app.route('/users/<username>')
def show_user_profile(username):
    return 'User %s' % username
