from django import forms


class CursoFormulario(forms.Form):

    grado = forms.IntegerField()


