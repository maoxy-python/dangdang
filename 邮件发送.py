import os
from django.core.mail import send_mail,EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE']='dangdang.settings'

if __name__ == '__main__':
    # send_mail()
    html_content = '<html><a href="http://www.baidu.com">葫芦娃葫芦娃，一根藤上七朵花，风吹雨打，都不怕，啦啦啦啦</a></html>'
    msg = EmailMultiAlternatives(subject='你好我是葫芦娃',body=html_content,from_email='ijioijikk@163.com',to=['yydssb@126.com'])
    msg.attach_alternative(html_content,"text/html")
    msg.send()



# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #邮件发送所要调用的后端模块，必须的
# EMAIL_HOST = 'smtp.163.com' #SMTP地址
# EMAIL_PORT = 25 #SMTP端口
# EMAIL_HOST_USER = 'xxxxxxxxxxx@163.com' #发送邮件的邮箱
# EMAIL_HOST_PASSWORD = 'xxxxxxxxx'  # 授权码
# EMAIL_SUBJECT_PREFIX = '[当当网] ' #为邮件Subject-line前缀,默认是'[django]'