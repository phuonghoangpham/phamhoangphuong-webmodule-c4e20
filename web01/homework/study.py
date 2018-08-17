from flask import Flask, redirect
app = Flask(__name__)

@app.route('/about-me')
def about_me():
    return "Name: Phạm Hoàng Phương \
    Age: 27 \
    DOB: 12/09/1991 \
    Work title: Recruiter \
    Company: Ematic Solutions \
    Industry: SaaS"

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
