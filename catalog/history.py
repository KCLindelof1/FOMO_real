from catalog import models as cmod


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        recent_list = request.session.get('last_five', [])
        request.last_five = []
        for p in recent_list:
            request.last_five.append(cmod.Product.objects.get(id=p))
        # Pull your last 5 products viewed here
        # load out of the session

        # request.session -> Dictionary
        # Get the list of product ids from the session
        # request.session.get(whatever keys (not full products) )
        # convert the product ids into a list of project objects
        # pull the associated objects from the database [cmod.Product.objects.filter(productid=xx)]
        # request.last_five = [...list of products...]

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        last_five_ids = []
        for r in request.last_five:
            last_five_ids.append(r.id)

        request.session['last_five'] = last_five_ids
        # Save the id's back to the session
        # save back into the session

        # convert request.last_five into a list of ids (convert product objects back into ids)
        # request.session['...'] = list of ids

        return response
