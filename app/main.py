from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
    <body style="text-align:center; margin-top:100px; font-family:Arial">
        <h1>🚀 Hello GitLab CI!</h1>
        <p>版本：v1.0</p>
        <p>构建号：{build}</p>
    </body>
    </html>
    '''.format(build="dev")

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
