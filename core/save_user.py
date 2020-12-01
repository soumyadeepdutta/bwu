from .models import User, Response

def createUser(params):

    def getAddress(params):
        addr = ''
        for key, value in params['address'].items():
            if value:
                addr += (value + ', ')
        return addr

    user = User(
        name=params['name'] + ' ' + params['last_name'],
        email=params['email'],
        address=getAddress(params),
        contact_no=params['contact'],
        city=params.get('city') or None,
        pin_code=params.get('pin_code') or None,
        state=params.get('state') or None,
        country=params.get('country') or None,
        date_of_birth=params.get('dob') or None,
    )
    user.save()
    return user.get_pk()

def createResponse(params, user_pk, action):
    prop = Response(
        user = User.objects.get(pk=user_pk),
        query=action.split('.')[0],
        age = params.get('propage') or None,
        bhk = params.get('bhk') or None,
        typ = params.get('proptype') or None,
        price = params.get('price') or None,
        budget = params.get('budget_range') or None,
        specifications = params.get('specification') or None,
        limitations = params.get('limitations') or None,
    )
    prop.save()
   
