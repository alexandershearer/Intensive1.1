from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def greeting_posts():

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)