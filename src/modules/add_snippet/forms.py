from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from flask_codemirror.fields import CodeMirrorField

from src.config import settings


language_choices = (
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("go", "Go")
)


class AddSnippetForm(FlaskForm):
    name = StringField()
    language = SelectField(choices=language_choices)
    code = CodeMirrorField(language='python')
