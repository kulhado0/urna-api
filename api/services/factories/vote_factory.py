from django.core.exceptions import ValidationError

from api.services.builders.vote_builder import VoteBuilder


class VoteFactory:
    def __init__(self):
        self.vote = VoteBuilder()

    def create_vote(self, body: dict):
        if 'cpf' in body and type(body['cpf']) == str:
            self.vote.with_cpf(body['cpf'])

        if 'presidente' in body and type(body['presidente']) == str:
            self.vote.with_president(body['presidente'])

        if 'idade' in body and type(body['idade']) == int:
            age = body['idade']
            if age < 16:
                raise ValidationError(message='age')
            self.vote.with_age(age)

        if 'sexo' in body and type(body['sexo']) == str:
            self.vote.with_sex(body['sexo'])

        if 'audio' in body and type(body['audio']) == str:
            self.vote.with_audio(body['audio'])

        if 'video' in body and type(body['video']) == str:
            self.vote.with_video(body['video'])

        return self.vote.build()