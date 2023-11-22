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


# @index_blueprint.route('/github', methods=['GET'])
# def github_redirect():
#     """Redirects users to github repository or rick rolls them :D"""
#     if random.choices([True, False], [0.5, 0.5])[0]:
#         return redirect('https://github.com/NickNaskida/CodeTyper')
#     else:
#         return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

