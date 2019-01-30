'''
    存放ViewSet中用到的Mixin

    其中:
    权限控制mixin (RbacMixin)
    Rbac开头的为 ViewSet中用到的，权限范围控制mixin
'''


class RequestMixin(object):
    @property
    def _request(self):
        return getattr(self, 'request', None) or self.context.get('request')

    @property
    def member(self):
        return self._request.user

    @property
    def method(self):
        return self._request.method


class RbacMemberMixin(RequestMixin):
    """Member权限范围控制"""
    def get_queryset(self):
        print(self.action)
        user_ids = []
        user_ids.append(self.member.id)
        queryset = self.queryset.filter(id__in=user_ids)
        return queryset

