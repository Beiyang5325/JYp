from flask import Flask, request, send_file
import os

app = Flask(__name__)

# 检查并创建上传目录
def check_upload_folder():
    uploads_dir = 'uploads'
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)

# 获取上传目录中的文件列表
def get_uploaded_files():
    uploads_dir = 'uploads'
    if os.path.exists(uploads_dir):
        files = os.listdir(uploads_dir)
        return files
    return []

# 上传文件的页面和显示文件列表
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    check_upload_folder()  # 检查并创建上传目录

    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            uploaded_file.save(os.path.join('uploads', uploaded_file.filename))
            return '<h1>文件上传成功！</h1> <a href="/">去主页查看</a>'
    
    files = get_uploaded_files()  # 获取上传目录中的文件列表
    file_list = '<h1>已上传的公开文件列表：</h1><ul>'
    for file in files:
        #file_list += f'<li><a href="/在线预览或下载/{file}">在线预览文件或下载文件 - {file}</a></li>'
        #<p><a href="https://jdy.hucl.link" class="myButton">点击前往简单云（可以作为后台）</a></p>
        file_list += f'<li><a href="/在线预览或下载/{file}"  class="myButton">在线预览文件或下载文件 - {file}</a></li>'
    file_list += '</ul>'
    
    return f'''
    <!doctype html>
    <!-- 全屏相关 -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-touch-fullscreen" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="full-screen" content="yes">
    <meta name="browsermode" content="application">
    <meta name="x5-fullscreen" content="true">
    <meta name="x5-page-mode" content="app">

    <html>
    <head>
        <title>飓云盘-简单云</title>
        <link rel="shortcut icon" href="http://www.hucl.link/Logo/logo.png" type="image/x-icon">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 50px;
                text-align: center;
            }}
            h1 {{
                color: #333;
            }}
            form {{
                margin-top: 30px;
            }}
            input[type=file], input[type=submit] {{
                padding: 10px;
                margin-top: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            input[type=submit] {{
                background-color: #4CAF50;
                color: white;
                cursor: pointer;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
                margin: 0;
            }}
            li {{
                margin-bottom: 10px;
            }}
            a {{
                text-decoration: none;
                color: #000;
            }}
            a:hover {{
                text-decoration: underline;
            }}

    .myButton {{
        display: inline-block;
        padding: 10px 25px;
        font-size: 16px;
        text-align: center;
        text-decoration: none;
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }}

    .myButton:hover {{
        background-color: #2980b9;
    }}

    .infoBox {{
        padding: 20px;
        border-radius: 10px;
        margin: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
        </style>
    </head>
    <!-- <div class="infoBox"> -->
    <body>
        <h1>飓云盘-简单云</h1>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <br>
            <input type=submit value=上传>
        </form>
        {file_list}
    </body>
    <!-- </div> -->

    </html>
    '''

# 预览上传的文件
@app.route('/在线预览或下载/<filename>')
def view_file(filename):
    uploads_dir = 'uploads'
    file_path = os.path.join(uploads_dir, filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    return '找不到文件'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2266)