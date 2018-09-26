from django.core.exceptions import ValidationError


CATEGORIES = ['Indian', 'Chinese Surinamese', 'Chinese', 'Thai', 'Mexican']


def validate_category(value):
    cat = value.capitalize()
    if value not in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category")