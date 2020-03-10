"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 管理应用app，统一放到根目录apps文件夹下
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_)-b%&v04!)1)vg#s+n&6pw2-6x)wfofu)+g$5ll7wy+fv&925'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# 允许所有地址访问
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'blog',
    'mdeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.blog.context_processors.global_setting',  # 自定义上下文管理器
            ],
        'builtins': ['django.templatetags.static']  # 可在html模板中取消 {% load static %} 或 {% load staticfiles %}
        },
    },
]

# 分页 views中使用
BLOG_INDEX_PAGINATOR_BY = 10
# 首页滚动条 views中使用 此处可以添加到上下文管理器
BLOG_INDEX_MARQUEE = '本站属个人博客，旨在记录博主的学习和工作，同时传递与分享经验。'
# 上下文管理器内容，context_processors.py 映射
## 标签页标题
BLOG_HEADER_TITLE = "Coffee | HONGWEI's Blog"
## 标签页图标。后面设置后台与其保持一致
BLOG_HEADER_LOGO = "/static/blog/images/favicon.ico"
## 侧边栏标题
BLOG_SIDEBAR_TITLE = "HONGWEI's Blog"
## 侧边栏欢迎信息 空字符代表取消 BLOG_NOTICE = "你好，很高兴见到你欢迎来到我的博客！QQ：289967396 Email：i@zhwei.cn "
BLOG_SIDEBAR_NOTICE = ""

# 归档页 显示项目归档或者自定义 字典key最大长度限制全数字15全中文8全字母12 外站必须使用http或者https开头的完整地址 内站直接使用url内的链接即可
PROJECT_ON = True
PROJECT_TITLE = "项目归档"
PROJECT_ARCHIVES = {'HwTTK-unittest': 'https://github.com/hongweifuture/JzUnit',
                    '关于博客': '/about',
                    '建站日志': '/timeline',
                    '百度': 'http://www.baidu.com',
                    }


WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 修改修数据为Mysql，需要安装mysqlclient，macos需要安装homebrew然后安装brew install mysql-connector-c，貌似新版本安装mysql-client
# https://github.com/PyMySQL/mysqlclient-python
# https://pypi.org/project/mysqlclient/
# 创建mysql5.6数据库： CREATE DATABASE website CHARACTER SET UTF8;
# 创建mysql5.7数据库： CREATE DATABASE website DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website',
        'USER': 'root',
        'PASSWORD': 'zhwei.cn',
        'HOST': 'mysql',
        'PORT': '3306',
        # 避免映射数据库时出现警告
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 添加中文和国际化支持，时间本地化
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 静态文件收集
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# 媒体文件收集
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 网站搜索HAYSTACK
HAYSTACK_CONNECTIONS = {
    'default': {
        #  指定 django haystack 使用的搜索引擎，选择语言解释器为自己更换的结巴分词whoosh_cn_backend
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        # 保存索引文件的地址，选择主目录下，这个会自动生成
        'PATH': os.path.join(BASE_DIR, 'whoose_index'),
    }
}
# 分页，与上下文管理器，index首页分页数相同BLOG_INDEX_PAGINATOR_BY，可自定义
HAYSTACK_SEARCH_RESULTS_PER_PAGE = BLOG_INDEX_PAGINATOR_BY

# 添加此项，当数据库改变时，会自动更新索引，非常方便，1.x版本是haystack.indexes.RealTimeSearchIndex，已经取消
# https://django-haystack.readthedocs.io/en/master/migration_from_1_to_2.html
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# django-mdeditor富文本编译器支持markdown，实时预览
MDEDITOR_CONFIGS = {
    'default':{
        'width': '90% ',  # Custom edit box width  宽度，整个页面的百分之多少
        'heigth': 500,  # Custom edit box height   高度，单位为px
        'toolbar': ["undo", "redo", "|",
                    "bold",  "italic", "quote", "ucwords", "uppercase", "lowercase", "del", "|",
                    "h1", "h2", "h3", "h4", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "image", "link", "reference-link", "code", "preformatted-text", "code-block", "table", "datetime", "|",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info", "|",
                    "preview", "watch", "fullscreen"],  # custom edit box toolbar   工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type  允许上传的图片 的格式，不在这个里面的格式将不允许被上传
        'image_floder': 'editor',  # image save the folder name   上传图片后存放的目录，BASE_DIR/MEDIA_ROOT/editor
        'theme': 'default',  # edit box theme, dark / default  mdeditor主题，dark/default两种
        'preview_theme': 'default',  # Preview area theme, dark / default  内容显示区主题 dark/default
        'editor_theme': 'default',  # edit area theme, pastel-on-dark / default   文本编辑区主题  pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement  是否打开搜索替换
        'emoji': True,   # whether to open the expression function  是否允许使用emoji表情
        'tex': True,  # whether to open the tex chart function   是否打开tex图表功能
        'flow_chart': True,  # whether to open the flow chart function   是否打开流程图功能
        'sequence': True  # Whether to open the sequence diagram function   是否打开序列图函数
    }
}
# admin后台管理
BLOG_ADMIN_SITE_TITLE = "HONGWEI 博客管理系统"
BLOG_ADMIN_SITE_HEADER = "博客后台系统"
# 当前后台不支持 INDEX_TITLE
BLOG_ADMIN_INDEX_TITLE = ""
# simpleui配置
# 关闭登录页粒子动画，默认开启，省资源可以关闭
# SIMPLEUI_LOGIN_PARTICLES = False

# 后台登陆后“首页”配置，可选项，不配置“首页”显示快捷操作、最近动作、快速访问等信息
## 后台首页配置
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
## 首页标题
# SIMPLEUI_HOME_TITLE = '百度一下你就知道'
## 首页图标, 支持element - ui和fontawesome的图标，参考https: // fontawesome.com / icons图标
# SIMPLEUI_HOME_ICON = 'fa fa-user'

## simpue版权信息
SIMPLEUI_HOME_INFO = False
## 快速访问
SIMPLEUI_HOME_QUICK = True
## 最近动作
SIMPLEUI_HOME_ACTION = True
# 分析上传，保护隐私不上传
SIMPLEUI_ANALYSIS = False

# 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取,页面选择后查看源码，在theme.js里面可查主题
SIMPLEUI_DEFAULT_THEME = 'e-blue-pro.css'
# 设置simpleui 点击首页图标跳转的地址，不设置为“/”
# SIMPLEUI_INDEX = 'https://www.88cto.com'

# 自定义SIMPLEUI的Logo
SIMPLEUI_LOGO = BLOG_HEADER_LOGO
# SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'
# 离线模式，不采用cdn
SIMPLEUI_STATIC_OFFLINE = True

# 自定义菜单栏   图标地址 https://fontawesome.com/icons?d=gallery&q=b&m=free
SIMPLEUI_CONFIG = {
    'system_keep': False,   #系统默认的菜单，默认为False，不保留。 如果改为True，自定义和系统菜单将会并存
    'menu_display': ['博文相关', '友链', '时间轴', '关于博客', '权限认证'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': False,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [{
        'name': '博文相关',
        'icon': 'fas fa-code',
        'models': [ {
            'name': '分类',
            'icon': 'fas fa-list',
            'url': 'blog/category/'
        }, {
            'name': '标签',
            'icon': 'fas fa-tags',
            'url': 'blog/tag/'
        },{
            'name': '文章',
            'icon': 'fas fa-book-open',
            'url': 'blog/article/'
        }]
    }, {
        'name': '时间轴',
        'icon': 'fas fa-bars',
        'url': 'blog/timeline/'
    },  {
        'name': '友链',
        'icon': 'fas fa-link',
        'url': 'blog/friendlink/'
    }, {
        'name': '关于博客',
        'icon': 'fas fa-bold',
        'url': 'blog/about/'
    }, {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }, {
            'name': '组',
            'icon': 'fas fa-users-cog',
            'url': 'auth/group/'
        }]
    }]
}