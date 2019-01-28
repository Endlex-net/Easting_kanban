from django.db import models
from django.forms import model_to_dict
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from djchoices import DjangoChoices, ChoiceItem

from utils.base_models import Abstraction, BaseModel
from utils import common_utils, django_utils

from account.models import Member


class Project(BaseModel):
    class ProjectStatus(DjangoChoices):
        close = ChoiceItem(0, "关闭")
        open = ChoiceItem(1, "打开")

    class ProjectSource(DjangoChoices):
        new = ChoiceItem(0, "新建")
        part = ChoiceItem(1, "任务拆分")

    name = models.CharField(
        "用户名",
        max_length=20,
        blank=True,
        db_index=True,
    )
    members = models.ManyToManyField(
        Member,
        verbose_name="成员",
    )
    intro = models.CharField('简介', max_length=1024, blank=True)
    status = models.IntegerField(
        default=ProjectStatus.open,
        choices=ProjectStatus.choices,
        help_text=str(ProjectStatus.choices),
    )
    source = models.IntegerField(
        choices=ProjectSource.choices,
        default=ProjectSource.new,
        help_text=str(ProjectSource.choices)
    )

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        ordering = ('-id',)
        verbose_name = "项目"


class ProjectManager(BaseModel):
    agent = models.ForeignKey(
        Member,
        on_delete=models.PROTECT,
        verbose_name="成员",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        verbose_name="项目"
    )

    class Meta(BaseModel.Meta):
        verbose_name = "项目管理员"

    def __str__(self):
        return "{}, {}".format(self.agent.username, self.project.name)


class Task(BaseModel):
    class TaskPriority(DjangoChoices):
        lowest = ChoiceItem(0, "最低")
        low = ChoiceItem(1, "低")
        normal = ChoiceItem(2, "中")
        high = ChoiceItem(3, "高")
        highest = ChoiceItem(4, "最高")

    class TaskStatus(DjangoChoices):
        todo = ChoiceItem(0, "TODO")
        doing = ChoiceItem(10, "进行中")
        done = ChoiceItem(200, "结束")
        cancel = ChoiceItem(400, "取消")
        fail = ChoiceItem(500, "失败")

    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        verbose_name="项目",
    )
    status = models.IntegerField(
        "项目状态",
        default=TaskStatus.todo,
        choices=TaskStatus.choices,
        help_text=str(TaskStatus.choices),
    )
    priority = models.IntegerField(
        "优先级",
        default=TaskPriority.normal,
        choices=TaskPriority.choices,
        help_text=str(TaskPriority.choices),
    )
    title = models.CharField(
        "标题",
        max_length=250,
        blank=True,
    )
    manager = models.ForeignKey(
        Member,
        verbose_name="负责人",
        on_delete=models.PROTECT,
        related_name="manager_tasks"
    )
    workers = models.ManyToManyField(
        Member,
        verbose_name="执行者",
        related_name="tasks",
    )
    todo_time = models.DateTimeField(
        "添加至TODO的时间"
    )
    start_time = models.DateTimeField(
        "开始时间"
    )
    finish_time = models.DateTimeField(
        "结束时间"
    )
    deadline = models.DateTimeField(
        "deadline"
    )

    class Meta(BaseModel.Meta):
        verbose_name = "任务"

    def __str__(self):
        return self.name
