# JYp
## JYp简介
1. JYp基于Python所写，有用flask库
2. JYp一个简单的云盘服务端程序
3. JYp官方的QQ交流群：822726278
4. JYp只是一个简单的云盘服务端程序，完善度并不高你可以尝试进行修改，以达到更加高效的服务，但是你2改的服务端程序务必开源，感谢支持

## 运行命令如下

### Termux运行
1. 首先更新一下软件源，确保在之后的步骤中不会报错（不怕报错的话，你就跳过这一步）
```ruby
pkg update
```

2. 安装必备软件，没有他们的话，可能会导致您的运行出现错误，必须执行
```ruby
pkg install -y python vim python-pip git
```

3. 克隆本仓库，也就是获取源代码
```ruby
git clone https://github.com/Beiyang5325/JYp
```

4. 安装Python库，确保能正常执行这个脚本
 （我嫌弃慢的话可以换一下pip源）
```ruby
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
<br>
```ruby
pip install flask
```

5. 进入目录
```ruby
cd JYp
```

6. 运行脚本，启动服务
```ruby
python jyp.py
```

<br><br><br>


### 其他linux发行版远行
1. 首先更新一下软件源，确保在之后的步骤中不会报错（不怕报错的话，你就跳过这一步）
```ruby
apt update
```

2. 安装必备软件，没有他们的话，可能会导致您的运行出现错误，必须执行
```ruby
apt install -y python vim git
```

3. 克隆本仓库，也就是获取源代码
```ruby
git clone https://github.com/Beiyang5325/JYp
```

4. 安装Python库，确保能正常执行这个脚本
```ruby
pip install flask
```

5. 进入目录
```ruby
cd JYp
```

6. 运行脚本，启动服务
```ruby
python jyp.py
```