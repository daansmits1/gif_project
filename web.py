from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop
g = giphypop.Giphy()

@app.route('/')
def index():
	search = request.values.get('search')
	return render_template('index.html')

@app.route('/results')
def results(): #needs to be right under the app line
	results = g.search('search')
	return render_template('results.html')

@app.route('/about')
def about(): #needs to be right under the app line
	return render_template('about.html')

app.run(debug=True)