from django.db import models
from django.contrib.auth.models import User, AbstractUser
from djchoices import DjangoChoices, ChoiceItem

from utils.base_models import Abstraction, BaseModel


class Member(AbstractUser, BaseModel):
    class Gender(DjangoChoices):
        female = ChoiceItem(0, '女')
        male = ChoiceItem(1, '男')
        unknown = ChoiceItem(2, '未知')

    name = models.CharField(
        "姓名",
        max_length=15,
        blank=True,
    )
    gender = models.IntegerField(
        '性别',
        default=Gender.unknown,
        choices=Gender.choices,
        help_text=str(Gender.choices),
    )
    avatar = models.URLField("头像", blank=True)
    cellphone_no = models.CharField(
        '手机',
        max_length=20,
        blank=True,
        db_index=True,
    )
    open_id = models.CharField(
        'OPEN_ID',
        max_length=100,
        blank=True,
        db_index=True,
    )
    intro = models.CharField('简介', max_length=1024, blank=True)
    duty = models.CharField('职务', max_length=20, blank=True)

    class Meta(BaseModel.Meta):
        ordering = ('-id',)
        verbose_name = "成员"

    def __str__(self):
        return self.name or self.username or self.cellphone_no


class Department(BaseModel):
    name = models.CharField(
        "名称",
        max_length=100,
        blank=True,
        db_index=True,
    )
    manager = models.ForeignKey(
        Member,
        verbose_name="负责人",
        on_delete=models.PROTECT,
        related_name="manager_departments"
    )
    members = models.ManyToManyField(
        Member,
        verbose_name="成员",
        related_name="departments"
    )
    intro = models.CharField('简介', max_length=1024, blank=True)
    superior = models.ForeignKey(
        'Department',
        verbose_name="上级",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        verbose_name = "部门"