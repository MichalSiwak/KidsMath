from django import forms


CATEGORY = (
    (1, 'Dodawanie'),
    (2, 'Odejmowanie'),
    (3, 'Mnożenie'),
    (4, 'Dzielenie'),
    (5, 'Inne'),
)


class CategoryForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY, widget=forms.widgets.Select(
            attrs={
                "class": "input is-primary",
                "type": "number",
            }
        ),
        label="",
    )
