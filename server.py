from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index.html')
def hello_home():
    return render_template('index.html')
@app.route('/about.html')
def about_me():
    return render_template('about.html')
@app.route('/works.html')
def works():
    return render_template('works.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/components.html')
def components():
    return render_template('components.html')
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
def write_to_file(data):
    with open('database.txt',mode='a') as file:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file.write(f'\n{email} {subject} {message}')
def write_to_csv(data):
    with open('database.csv',mode='a') as filecsv:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csvwriter= csv.writer(filecsv, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data=request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again !'
