from django import forms


class CategoryForm(forms.Form):
    CATEGORY = (
        (1, 'Dodawanie'),
        (2, 'Odejmowanie'),
        (3, 'Mnożenie'),
        (4, 'Dzielenie'),
        (5, 'Ułamki dziesiętne'),
    )
    category = forms.ChoiceField(choices=CATEGORY, widget=forms.widgets.Select(
            attrs={
                "class": "input is-primary",
                "type": "number",
            }
        ),
        label="",
    )


class CategoryDecimalFractionsForm(forms.Form):
    CATEGORY = (
        (1, 'Dodawanie'),
        (2, 'Odejmowanie'),
        (3, 'Mnożenie'),
        (4, 'Dzielenie'),
    )
    category = forms.ChoiceField(choices=CATEGORY, widget=forms.widgets.Select(
            attrs={
                "class": "input is-primary",
                "type": "number",
            }
        ),
        label="",
                                 )
