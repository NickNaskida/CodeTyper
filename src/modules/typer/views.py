from flask import Blueprint, render_template, abort

from src.crud import snippet

typer_blueprint = Blueprint(
    'typer',
    __name__,
    template_folder='templates/typer',
    url_prefix="/snippet"
)


@typer_blueprint.route('/<int:snippet_id>', methods=['GET'])
def typer(snippet_id: int):
    snippet_obj = snippet.get(_id=snippet_id)

    if not snippet_obj:
        abort(418)  # LOL :D

    return render_template('typer.html', snippet=snippet_obj)

