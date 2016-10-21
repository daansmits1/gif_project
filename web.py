from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop

@app.route('/')
def index():
	search = request.values.get('search')
	return render_template('index.html')

app.run(debug=True)