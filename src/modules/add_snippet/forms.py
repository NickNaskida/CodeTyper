from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField


class AddSnippetForm(FlaskForm):
    code = CodeMirrorField(language='python')
