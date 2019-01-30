from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class DebugDisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        """测试环境下 关闭csrf检测"""
        if settings.DEBUG == True:
            setattr(request, '_dont_enforce_csrf_checks', True)
