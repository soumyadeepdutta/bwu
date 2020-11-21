from .models import User

def createUser(params):
    user = User(
        name=params['name'][0],
        email=params['mail'][0]
    )
    user.save()
