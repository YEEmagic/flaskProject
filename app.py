from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return '홈페이지 테스트'

@app.route('/send')
def send():  # send endpoint
    return '/send'


if __name__ == '__main__':
    app.run()
