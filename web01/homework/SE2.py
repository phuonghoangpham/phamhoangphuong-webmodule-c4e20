from flask import Flask, render_template
app = Flask(__name__)

@app.route('/users/<username>')
def index(username):
    users = {
        "Quan": {"name": "Nguyen Anh Quan",
                "age": "16",
                "hobby": "football",
                "gender": "male"},
                
        "Tuan Anh": {"name": "Huynh Tuan Anh",
                "age": "23",
                "hobby": "tennis",
                "gender": "male"},

        "Phuong": {"name": "Pham Hoang Phuong",
                "age": "27",
                "hobby": "reading books",
                "gender": "female"},

        "Chi": {"name": "Pham Quynh Chi",
                "age": "27",
                "hobby": "singing",
                "gender": "female"}
    }
    if username in users:
        return render_template('index.html', username = users[username])
    else: 
        return "User not found"

if __name__ == '__main__': 
  app.run(debug=True)
