from django.db import models

# Create your models here.

class NlpReponse(models.Model):
    taskId=models.CharField(u'任务Id', max_length=100, default='no_taskId')
    callId=models.CharField(u'会话Id', max_length=100, default='no_callId')
    timestamp=models.CharField(u'时间戳', max_length=100, default='no_timestamp')
    code=models.IntegerField(u'状态码',max_length=100,default=0)
    msg=models.IntegerField(u'结果',max_length=100,default='')
    def __unicode__(self):
        return '%d: taskId: %s ; callId: %s ; timestamp: %s ; code: %s ; msg: %s ; result: %s' % (self.pk, self.taskId,self.callId,self.timestamp,self.code,self.msg)

    def __init__(self, taskId, callId,timestamp,code,msg):
        # super().__init__(*args, **kwargs)
        # Content is a bytestring. See the `content` property methods.
        self.taskId = taskId
        self.callId = callId
        self.timestamp = timestamp
        self.code = code
        self.msg = msg


class Student(models.Model):
    name = models.CharField(u'姓名', max_length=100, default='no_name')
    sex = models.CharField(u'性别', max_length=50, default='male')
    sid = models.CharField(u'学号', max_length=100, default='0')

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)

from pygments.lexers import get_all_lexers         # 一个实现代码高亮的模块
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())     # 列出所有配色风格


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
