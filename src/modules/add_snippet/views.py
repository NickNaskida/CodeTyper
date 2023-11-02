from flask import Blueprint, render_template, flash

from src import crud
from src.models.snippet import SnippetModel
from src.modules.add_snippet.forms import AddSnippetForm

add_snippet_blueprint = Blueprint(
    'add_snippet',
    __name__,
    template_folder='templates/add_snippet',
)


@add_snippet_blueprint.route('/add-snippet', methods=['GET', 'POST'])
def index():
    form = AddSnippetForm()

    if form.validate_on_submit():
        snippet = SnippetModel(code=form.code.data)
        crud.snippet.create(obj_new=snippet)
        flash('Snippet added successfully', 'success')
        return render_template('add_snippet.html', form=form)

    return render_template('add_snippet.html', form=form)
