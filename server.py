from flask import Flask, render_template, url_for ,request,redirect
import csv


app = Flask(__name__)


# @app.route("/<username>")
# def hello_world(username = None):
#     return render_template('./index.html', name = username)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')





@app.route("/")
def home():
    return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt' , mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name},{email},{subject},{message}')


def write_to_csv(data):
     with open('database.csv' , newline="", mode='a') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter= ",",quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() 
            write_to_csv(data)     
            return redirect('./thankyou.html')
        except:
            return 'something wrong'   
    return 'Something wrong '

# @app.route("/index.html")
# def home2():
#     return render_template('./index.html')
# @app.route("/generic.html")
# def blog():
#     return render_template('./generic.html')
# @app.route("/projects.html")
# def projects():
#     return render_template('./projects.html')
