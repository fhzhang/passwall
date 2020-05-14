from django.http import HttpResponse
import redis


def link1(request):
    myHostname = "express.redis.cache.windows.net"
    myPassword = "wmS6BUskvmIV5GhpkjW72oofb+iLdlTLKD4ND7u+CRc="

    r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)
    result = r.ping()
    print("Ping returned : " + str(result))
    result = r.set("Message", "Hello!, The cache is working with Python!")
    print("SET Message returned : " + str(result))

    result = r.get("Message")
    print("GET Message returned : " + result.decode("utf-8"))
    return HttpResponse("Hello, world. You're at the polls index.")