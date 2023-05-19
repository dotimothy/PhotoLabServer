# PhotoLabServer.py: Image Processing Web Server Implemented in Python Flask
# Author: Timothy Do

# Libraries 
from flask import Flask, redirect, url_for, render_template, request, send_file
import os
import PhotoLab


# Creating the app 
app = Flask(__name__)

# Static Variables
engList = {'Python':'pythonop','MATLAB':'matlabop'}
opList = {
	'Python': {'FFT':PhotoLab.fftPy,'Sharpen':PhotoLab.sharpenPy,'Laplacian':PhotoLab.laplacianPy}, 
	'MATLAB':{'FFT':PhotoLab.fftMat,'Sharpen':PhotoLab.sharpenMat,'Laplacian':PhotoLab.laplacianMat}
}

# Landing Page
@app.route("/")
def home():
	return render_template('index.html')

@app.route("/upload",methods=["POST","GET"])
def upload():
	if request.method == "POST": 
		image = request.files['upload']
		name = request.form['filename']
		engine = request.form['engine']
		operation = request.form[engList[engine]]
		if not image or not name:
			return render_template('noimage.html')
		if(not os.path.exists(os.getcwd() + '\\results')):
			os.makedirs(os.getcwd() + '\\results')
		if(operation != "Save"):
			fname,ext = os.path.splitext(name)
			name = f'{fname}_{operation}{ext}'
		path = f'./results/{name}'
		image.save(path)
		if(operation != "Save"):
			abPath = os.getcwd() + f'\\results\\{name}'
			opList[engine][operation](abPath)
		nl = '\n'
		html = f"<h1 style='font-family:Courier'>Your Uploaded Image ({name})</h1>{nl}{nl}"
		html = html + f"<h1 style='font-family:Courier'>Engine: {engine}</h1>{nl}{nl}"
		html = html + f"<h1 style='font-family:Courier'>Operation: {operation}</h1>{nl}<br>{nl}"
		html = html + f"<a href={path}><img width='50%' src={path} title={name}/></a>"
		html = html + f"<h1 style='font-family:Courier'><a href='/'>Return to Homepage</a></h1>{nl}"
		return html
	else:
		return redirect(url_for('home'))

@app.route("/clear")
def clear():
	try:
		for file in os.listdir('./results'):
			os.remove(os.path.join('./results',file))
		nl = '\n'
		return f'<script>{nl}alert("Cleared Results");{nl}window.location.href="/";{nl}</script>'
	except FileNotFoundError:
		return 'No Results'
		
@app.route("/results/<name>")
def results(name):
	path = f'./results/{name}' 
	return send_file(path,mimetype='image/gif')

@app.route("/collage")
def collage():
	images = os.listdir('./results')
	if not images:
		nl = '\n'
		return f'<script>{nl}alert("No Results.");{nl}window.location.href="/";{nl}</script>'
	html = "<h1 style='font-family:Courier'>Collage of Results:</h1>\n<br>"
	for image in os.listdir('./results'):
		path = os.path.join('./results',image)
		nl = '\n'
		html = html + f"<a href={path}><img title={image} src={path} width='10%'/></a>{nl}"
	html = html + "<h1 style='font-family:Courier'><a href='/'>Return to Homepage</a></h1>\n"
	return html


# Debug if the same file as run
if __name__ == "__main__":
	clear()
	app.run(debug=True,host='0.0.0.0',port=8080)
