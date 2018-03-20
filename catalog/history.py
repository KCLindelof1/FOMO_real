




class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Pull your last 5 products viewed here
        # load out of the session

        # request.session -> Dictionary
        # Get the list of product ids from the session
        # request.session.get(whatever keys (not full products) )
        # convert the product ids into a list of project objects
        # pull the associated objects from the database [cmod.Product.objects.filter(productid=xx)]
        # request.last_five = [...list of products...]





        # In catalog/templates/base_app.htm:
        #     for loop through request.last_five and print the product thumbnails on the right






        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        # Save the id's back to the session
        # save back into the session

        # convert request.last_five into a list of ids (convert product objects back into ids)
        # request.session['...'] = list of ids



        # detail.py
        # product (that they are looking at)
        # remove if current product is already in the list
        # request.last_five.insert(0, product)
        # if length of list > 6 items, remove the last (6)
        # display positions 1 - 5 (so its actually a list of 6)





        return response
