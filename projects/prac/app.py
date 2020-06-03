from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')   
def home():
   return render_template('index.html')

@app.route('/mypage') 
def mypage():
   return '마이페이지 화면이다.'

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
#post요청은 ajax에서 밖에 못함

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   author_receive = request.args.get('author_give')
   print(title_receive, author_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
# http://localhost:5000/test?title_give=제목&author_give=감독


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
#0000을 localhost 로 변경해도됨 ,, 서버를 실행하는 문장
