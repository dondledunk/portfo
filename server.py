from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    # show the user profile for that user
    return render_template('index.html')



@app.route('/<string:page_name>')
def html_page(page_name):
    # show the user profile for that user
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data ["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', 'a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data ["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('/thankyou.html')
    else:
    	return 'something went wrong'




# @app.route('/index.html')
# def my_index():
#     # show the user profile for that user
#     return render_template('index.html')

# @app.route('/works.html')
# def my_works():
#     # show the user profile for that user
#     return render_template('works.html')
# @app.route('/contact.html')
# def my_contact():
#     # show the user profile for that user
#     return render_template('contact.html')

# @app.route('/components.html')
# def my_components():
#     # show the user profile for that user
#     return render_template('components.html')

