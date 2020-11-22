from .models import User

def createUser(params):
    user = User(
        name=params['name'][0],
        email=params['mail'][0],
        contact_no=params['contact'][0],
        city=params['city'][0],
        pin_code=params['pin_code'][0],
        state=params['state'][0],
        country=params['country'][0],
        date_of_birth=params['dob'][0],
    )
    user.save()
