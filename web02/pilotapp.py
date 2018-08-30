from flask import *
import mlab
from mongoengine import *
from models.Service import Service

app = Flask(__name__)
mlab.connect()

#design pattern (MVC, MVP)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(
        gender=g,
        )
    return render_template(
        'search.html',
        all_service=all_service
        )

@app.route("/admin")
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service=all_service)

@app.route("/delete/<service_id>")
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id) 
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for("admin"))
    else:
        return "Not Found"

@app.route("/new-service", methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("new-service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        gender = form["gender"]

        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender
        )
        new_service.save()
        return redirect(url_for("admin"))

@app.route("/search/detail/<service_id>")
def detail(service_id):
    detailed_service = Service.objects.with_id(service_id)
    if detailed_service is not None:
        return render_template("detail.html", detailed_service=detailed_service)
    else:
        return "Not Found"

@app.route('/update-service/<service_id>', methods = ['GET', 'POST'])
def update_service(service_id):
    service_to_update = Service.objects.with_id(service_id)
    if request.method == 'GET':
        return render_template('update.html', service_to_update = service_to_update)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        service_to_update.name = name
        service_to_update.yob = yob
        service_to_update.phone = phone
    
        service_to_update.save()
        
        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
 