import random

from flask import Blueprint, render_template, redirect

from src.crud import snippet

index_blueprint = Blueprint(
    'index',
    __name__,
    template_folder='templates/index',
)


@index_blueprint.route('/', methods=['GET'])
def index():
    snippets = snippet.get_multi()
    return render_template('index.html', snippets=snippets)

