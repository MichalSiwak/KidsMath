from django.contrib import messages


def from_errors_to_list(form, request):
    for field in form:
        for error in field.errors:
            messages.add_message(request, 40, error)

