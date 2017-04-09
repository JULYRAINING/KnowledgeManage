from django.urls import reverse
from django.urls import reverse_lazy
#用户密码
#resurgam root1234
#katherine heaven.hell
parameter = {
    'title':'知识管理系统',
    'about':'关于',
    'about_detail':'关于（详情）',
    'contact':'',
    'menu':{
            
#           '审核':{'管理文档':reverse_lazy('knowledge:document_list')},
#           '订阅':{'管理我的订阅':reverse_lazy('knowledge:subscribe')},
            '文档':{'上传文档':reverse_lazy('knowledge:upload_document'),
#            '管理我的文档':'url'
            }
            },
    'user_profile':{
        'user':{'退出登录':reverse_lazy('user:logout')}
    },
    'guest':{
        '游客':{'登录/注册':reverse_lazy('user:login')}
    },
    'login_url':reverse_lazy('user:login'),
    'signup_url':reverse_lazy('user:signup'),
    'read_more':'阅读更多',
    'previous':'上一页',
    'next':'下一页',
    'search':'搜索',
    'category_label':'分类',
    'categorys':{'category1':'url','category2':'url','category3':'url'}



}

