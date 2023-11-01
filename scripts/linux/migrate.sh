export FLASK_APP=main
flask db migrate
flask db upgrade