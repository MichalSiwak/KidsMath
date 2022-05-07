from django import forms


class CategoryForm(forms.Form):
    CATEGORY = (
        (1, 'Liczby całkowite'),
        (2, 'Ułamki zwykle'),
        (3, 'Ułamki dziesiętne'),
    )

    OPERATIONS = (
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
    operations = forms.ChoiceField(choices=OPERATIONS, widget=forms.widgets.Select(
            attrs={
                "class": "input is-primary",
                "type": "number",
            }
        ),
        label="",
                                 )
