from django.http import HttpResponse,HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class UserAuthMiddle(MiddlewareMixin):
    def process_request(self, request):
        no_need_login = ['/api/postLogin', '/api/logout']
        if request.path not in no_need_login:
            if request.session.get('is_login') != '1':
                return HttpResponse ('Unauthorized', status=401)
        else:
            return
