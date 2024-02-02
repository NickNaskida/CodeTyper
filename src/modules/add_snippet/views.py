from flask import Blueprint, render_template, flash, redirect, url_for

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
        if form.code.data == "":
            flash("Code field can't be empty", "error")
            return render_template('add_snippet.html', form=form)

        snippet = SnippetModel(
            name=form.name.data,
            language=form.language.data,
            code=form.code.data
        )
        crud.snippet.create(obj_new=snippet)
        flash('Snippet added successfully', 'success')

        return redirect(url_for("index.index"))

    return render_template('add_snippet.html', form=form)
