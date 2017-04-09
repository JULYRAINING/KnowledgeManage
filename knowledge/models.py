from django.db import models
from django import forms
from django.contrib.auth.models import Group
from django.utils import timezone
from django.utils.text import slugify
from django_bootstrap_markdown.widgets import MarkdownInput
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from user.models import User

# Create your models here.
#文档类别
class Category(models.Model):
    #id_define
    name = models.CharField(max_length=100, verbose_name="类别")
    def __str__(self):
        return self.name
    class Meta:
        default_permissions = ()
        verbose_name = '文档类别'
        verbose_name_plural = '文档类别'
        permissions = (
            ("edit_category_prop", "修改文档分类属性"),
        )

# 文档审核状态标志
class DocumentStatus(models.Model):
    # id_define
    status = models.CharField(max_length=100, verbose_name="审核状态")
    def __str__(self):
        return self.status
    class Meta:
        default_permissions = ()
        verbose_name = '文档审核状态标志'
        verbose_name_plural = '文档审核状态标志'
        permissions = (
            ("edit_status_prop", "修改审核状态属性"),
        )

#文档表
class Document(models.Model):
    #id_define
    name = models.CharField(max_length=100, verbose_name="名称", blank=False)
    slug = models.SlugField(max_length=200, default="", blank=True, editable=False)
    description = models.CharField(max_length=100, verbose_name="详细描述", blank=False)
    author = models.CharField(max_length=100, verbose_name="作者", blank=False)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="上传者", blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="类别", blank=True, null=True)
    contains_File = models.BooleanField(blank=False, verbose_name="是否上传文件", default=False)
    file = models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/', verbose_name="文件", null=True)
    is_Markdown = models.BooleanField(blank=False, verbose_name="使用Markdown编辑器", default=False)
    content = models.TextField(blank=True, verbose_name="文档内容")
    markdown_content = MarkdownxField(verbose_name="Markdown", default="", blank=True)
    date = models.DateField(verbose_name="上传时间",default=timezone.now(), blank=False, null = False)
    tag = models.CharField(max_length=2000, verbose_name="标签", blank=True)
    
    status = models.ForeignKey(DocumentStatus, on_delete=models.CASCADE, verbose_name="审核状态", default=None, null=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.markdown_content)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name,allow_unicode = True)

        super(Document, self).save(*args, **kwargs)
    class Meta:
        default_permissions = ()
        verbose_name = '文档'
        verbose_name_plural = '文档'
        permissions = (
            ("read_document", "查看文档"),
            ("add_document", "添加文档"),
            ("edit_document", "编辑文档"),
            ("comment_document", "评论文档"),
        )

#文档审核表
class DocumentAssess(models.Model):
    #id_define
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name="文档")
    assessor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="审核者")
    status = models.ForeignKey(DocumentStatus, on_delete=models.CASCADE, verbose_name="审核状态")
    status_description = models.CharField(max_length=100, verbose_name="审核详细描述")
    def __str__(self):
        return self.status
    class Meta:
        default_permissions = ()
        verbose_name = '文档审核'
        verbose_name_plural = '文档审核'
        permissions = (
            ("assess_document", "审核文档"),
        )

#评论表
class Comment(models.Model):
    #id_define
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name="文档")
    content = models.TextField(verbose_name="内容")
    score = models.CharField(max_length=100, verbose_name="打分值")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="评论者")
    date = models.DateTimeField( verbose_name="时间")
    level = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="评论者角色")
    def __str__(self):
        return self.content
    class Meta:
        default_permissions = ()
        verbose_name = '评论'
        verbose_name_plural = '评论'
        permissions = (
            ("add_comment", "添加评论"),
            ("read_comment", "查看评论"),
            ("edit_comment", "编辑评论"),
        )
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
#订阅表
class Subscribe(models.Model):
    #id_define
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="订阅分类")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="订阅用户")

    class Meta:
        default_permissions = ()
        verbose_name = '订阅'
        verbose_name_plural = '订阅'
        permissions = (
            ("edit_subscrube", "编辑订阅内容"),
        )

#阅读记录
class ReadTrace(models.Model):
    #id_define
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name="文档")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="阅读者")
    class Meta:
        default_permissions = ()
        verbose_name = '阅读记录'
        verbose_name_plural = '阅读记录'
        permissions = (
            ("read_readTrace", "查看阅读记录"),
        )

TOPIC_CHOICES = (
        ('leve1', '差评'),
        ('leve2', '中评'),
        ('leve3', '好评'),
)
#Form
class DocumentForm(forms.Form):
    name = forms.CharField(max_length=100, label='文档标题')
    description = forms.CharField(max_length=100, label='文档描述')
    author = forms.CharField(max_length=100, label='文档作者')
    uploader = forms.CharField(max_length=100, label='上传者')
    category = forms.CharField(max_length=100, label='文档分类')
    file = forms.FileField(label='文件')
    content = forms.Textarea()
    topic = forms.ChoiceField(choices=TOPIC_CHOICES,label='选择评分')
    markdown = forms.CharField(widget=MarkdownInput)

class DocumentModelForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('name', 'description', 'author','is_Markdown','content','markdown_content', 'tag','contains_File','file',  )

class SubscribeModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('subscribe_category', 'subscribe_user')


