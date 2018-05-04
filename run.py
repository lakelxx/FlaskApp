#
"""
    run.py
    ~~~~~~~~~~~

    Run of the Flask app

    :copyright: lakelxx
    :license:
"""

from FlaskApp import app, db
from FlaskApp.models import User, Post

"""
How to start the flask app
Powershell:
$env:FLASK_APP = "run.py" in powershell
CMD:
set FLASK_APP = run.py
BASH:
export FLASK_APP = run.py
"""

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run(debug=True)
