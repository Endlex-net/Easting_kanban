'''
    存放ViewSet中用到的Mixin

    其中:
    权限控制mixin (RbacMixin)
    Rbac开头的为 ViewSet中用到的，权限范围控制mixin
'''
from account.models import Member


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

    @property
    def member_departments(self):
        return self.member.departments.all()

    @property
    def manager_departments(self):
        return self.member.manager_departments.all()

    @property
    def subordinate(self):
        departments = self.manager_departments
        return Member.objects.filter(departments__in=departments)


class RbacMemberMixin(RequestMixin):
    """Member权限范围控制"""
    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return self.queryset

        user_ids = [s.id for s in self.subordinate]
        user_ids.append(self.member.id)
        queryset = self.queryset.filter(id__in=user_ids)
        return queryset


class RbacDepartmentMixin(RequestMixin):
    """Department权限范围控制"""
    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return self.member_departments.all()
        return self.manager_departments.all()

