export FLASK_APP=main
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade