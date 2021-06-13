def post(function):
    def wrapped(*args, **kwargs):
        print(args[0])
        return function(*args, **kwargs)
    return wrapped

@post
def send_post(request):
    return request['method']


print(send_post({'method':'POST'}))
