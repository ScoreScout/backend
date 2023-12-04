from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class UserActivationView(APIView):
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        print(post_data)
        print(post_url)
        result = requests.post(post_url, data = post_data)
        print(result)
        content = result.text
        print(result.text)
        return Response(content)