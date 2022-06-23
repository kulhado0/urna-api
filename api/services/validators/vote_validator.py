from django.core.exceptions import ValidationError

from api.models import Vote
from api.services.builders.vote_builder import VoteBuilder


class VoteValidator:
    def __init__(self):
        pass

    def validate_age(self, age: int):
        if age >= 16:
            return
        raise ValidationError(message='age')
