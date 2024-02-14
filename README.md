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


<head>
    <style>
        .myButton {
            display: inline-block;
            padding: 8px 16px;
            font-size: 16px;
            text-align: center;
            text-decoration: none;
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .myButton:hover {
            background-color: #2980b9;
        }

        .infoBox {
            padding: 24px;
            border-radius: 12px;
            margin: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);

            position: relative;
            text-align: center;
            width: fit-content;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>
<body>
    <div class="infoBox">
        <p>加入官群：<br><a href="https://qm.qq.com/q/ZOvfOoGQqQ" class="myButton">点击这里</a></p>
    </div>
</body>
