from flask import Flask, request, send_from_directory, render_template
import os
from post import Post
from markdown2 import Markdown as mdwn

# Create a Flask object named app
app = Flask(__name__)

# Decorators are denoted by @decorator
# This does some strange things in the
# python virtual machine.
# In the case of flask it basically says
# whenever someone trys to access this page, run this function.
# If our website has the domain www.elliemae.pw
# then when someone types in www.elliemae.pw/js/javascript.js
# this will run the send_js function. One of the cool things about
# flask is it allows us to pass varibales from the url to the function.
# in the send_js function, we tell flask that anything after the js/ should be
# assigned to a variable called path (as in path to file) and
# passed to the send_js function

# I recommend looking at 
# https://www.youtube.com/watch?v=eesqK59rhGA

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('html/js', path)


@app.route('/post/<path:path>')
def postReturner(path):
    fl = f'html/post/{path}.md'
    post = Post(fl)
    return render_template('blog_post.html', post=post)


@app.route('/styles/<path:path>')
def send_styles(path):
    return send_from_directory('html/styles', path)


@app.route('/')
def landing_page():
    return send_from_directory('html', 'landing_page.html')


@app.route('/blog')
def blog_home_page():
    return render_template('blog_home_page.html',
                           post=sorted(
                           [
                               Post(os.path.join('html/post', i))
                               for i in os.listdir('html/post')
                           ], key=lambda x: x.date, reverse=True))


@app.route('/resume')
def send_resume():
    pass


if __name__ == '__main__':
    app.run()
