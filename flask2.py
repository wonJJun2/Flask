# fasttext로 벡터 생성 후 플라스크로 내보내기
from flask import Flask
app = Flask(__name__)
@app.route('/vector/<word>')

def make_vector(keyword):

    query = ft_model.wv.get_vector(word) 
    return str(query)

if __name__ == '__main__':
    app.run(debug = False)
