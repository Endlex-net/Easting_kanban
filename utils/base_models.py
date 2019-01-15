from django.db import models


class Abstraction(models.Model):
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True


class SoftDeletedManager(models.Manager):
    def filter(self, *args, **kwargs):
        defaults = {'deleted': False}
        defaults.update(kwargs)
        return self.get_queryset().filter(*args, **defaults)

    def exclude(self, *args, **kwargs):
        defaults = {'deleted': True}
        defaults.update(kwargs)
        return self.get_queryset().exclude(*args, **defaults)


class DeletedMixin(models.Model):
    deleted = models.BooleanField(
        '已删除',
        default=False,
        blank=True,
    )

    def hard_delete(self):
        return super().delete()

    def delete(self):
        self.deleted = True
        self.save()

    def recover(self):
        self.deleted = False
        self.save()

    class Meta:
        abstract = True


class BaseModel(DeletedMixin, models.Model):
    create_time = models.DateTimeField(
        '创建时间',
        null=True,
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        '更新时间',
        null=True,
        auto_now=True,
    )
    objects = SoftDeletedManager()

    class Meta:
        abstract = True
        ordering = ['-id']

