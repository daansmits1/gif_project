from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop
g = giphypop.Giphy()
import os


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results')
def results(): #needs to be right under the app line
	search = request.values.get('search_terms')
	results = g.search(search)
	return render_template('results.html', search=search, results=results)

@app.route('/about')
def about(): #needs to be right under the app line
	return render_template('about.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)