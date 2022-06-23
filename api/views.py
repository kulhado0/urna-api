import json

from django.core.exceptions import ValidationError
from django.http import HttpResponse

# Create your views here.
from api.services.factories.vote_factory import VoteFactory


def vote(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    try:
        body = json.loads(request.body)
        vote_factory = VoteFactory()
        vote = vote_factory.create_vote(body)
        return HttpResponse(status=200, content={'message': 'Voto efetuado com sucesso.'})
    except IndexError:
        return HttpResponse(status=400, content={"message": 'invalid params'})
    except ValidationError:
        return HttpResponse(status=403)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)
