from flask import Flask, render_template
app = Flask(__name__) #create a server/app


@app.route('/')
def index():
    posts = [
        {
        "title": "Thơ con ếch",
        "content": "Nội dung bài thơ",
        "author": "Tuấn Anh",
        "author_sex": 1
    },
        {
        "title": "Thơ con chó",
        "content": "Nội dung bài thơ",
        "author": "Thái",
        "author_sex": 1
    },
        {
        "title": "Thơ con mèo",
        "content": "Nội dung bài thơ",
        "author": "Chi",
        "author_sex": 0
    },
        {
        "title": "Thơ con cua",
        "content": "Nội dung bài thơ",
        "author": "Phương",
        "author_sex": 0
    }
    ]

    return render_template('index.html', posts = posts)

@app.route('/hello') #route must be unique
def say_hello():
    return "Hello from the other side"

@app.route('/say-hi/<name>/<age>') #<>: request parameters
def say_hi(name, age):
    return "Hi {}, you're {} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>') #gui 2 parameters dang integer, or default = string
def calc(x,y):
    return str(x+y)
    
if __name__ == '__main__': #if file app chay truc tiep
  app.run(debug=True)
 
#127.0.0.1: local host