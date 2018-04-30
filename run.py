#
"""
    run.py
    ~~~~~~~~~~~

    Run of the Flask app

    :copyright: lakelxx
    :license:
"""

from FlaskApp import app

"""
How to start the flask app
Powershell:
$env:FLASK_APP = "run.py" in powershell
CMD:
set FLASK_APP = run.py
BASH:
export FLASK_APP = run.py
"""

if __name__ == '__main__':
    app.run(debug=True)
