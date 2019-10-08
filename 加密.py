import hashlib


# 注册
username = 'zhouwei'
password = '123456'
h = hashlib.sha256()
h.update(password.encode())
pwd = h.hexdigest()
print(h.hexdigest())

#登录
pwd1 = '123456'
h1 = hashlib.sha256()
h1.update(pwd1.encode())
pwd2 = h1.hexdigest()
print(pwd2)
if pwd2 == pwd:
    print('登录成功')
else:
    print('登录失败')

# 加盐加密
import random
# 生成一个随机字符串，加到密码前面或者后面
s = '123134642561@#$%$#^%*&#$%TGSDFHDTYKZXFGADSFG'
y = random.sample(s,5)
y = ''.join(y)
pwd = '123456'
pwd = pwd+y
pwd1 = '123456'
h1 = hashlib.sha256()
h1.update(pwd1.encode())
h = hashlib.sha256()
h.update(pwd.encode())
print(h1.hexdigest())
print(h.hexdigest())

# 如果数据库中没有空白字段
# 全世界用户共吃一口盐