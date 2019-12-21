from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('html/js', path)


@app.route('/stypes/<path:path>')
def send_styles(path):
	return send_from_directory('html/styles', path)

@app.route('/blog')
def blog_home_page():
	return render_template(blog_home_page.html)

