from flask import Flask, request, send_from_directory, render_template
import os
from post import Post

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('html/js', path)


@app.route('/styles/<path:path>')
def send_styles(path):
	return send_from_directory('html/styles', path)

@app.route('/')
def landing_page():
    return send_from_directory('html/landing_page.html')

@app.route('/blog')
def blog_home_page():
    return render_template('blog_home_page.html', post=[ Post(os.path.join('html/post', i)) for i in os.listdir('html/post') ])

@app.route('/resume')
def send_resume():
    pass

if __name__ == '__main__':
    app.run()