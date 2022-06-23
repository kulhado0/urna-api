from api.models import Vote
from api.services.validators.vote_validator import VoteValidator


class VoteBuilder:
    def __init__(self):
        self.vote = Vote()

    def with_cpf(self, cpf: str):
        self.vote.cpf = cpf
        return self

    def with_age(self, age: int):
        VoteValidator().validate_age(age)
        self.vote.idade = age
        return self

    def with_president(self, president: str):
        self.vote.presidente = president
        return self

    def with_sex(self, sex: str):
        self.vote.sexo = sex
        return self

    def with_audio(self, audio: str):
        self.vote.audio = audio
        return self

    def with_video(self, video: str):
        self.vote.video = video
        return self

    def build(self):
        self.vote.save()
        return self.vote
