from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # 앞에 <meta charset="UTF-8">를 붙여주면 브라우저가 한글을 제대로 인식합니다!
    return '<meta charset="UTF-8"> <h1>도커 실습 성공!</h1> <p>내가 만든 첫 번째 도커 웹페이지입니다.</p>'
    # <meta charset="UTF-8">

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)