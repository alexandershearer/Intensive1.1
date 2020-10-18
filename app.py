from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

#Setup pymongo DB
app.config["MONGO_URI"] = "mongodb://localhost:27017/postsDatabase"
mongo = PyMongo(app)

@app.route('/')
def greeting_posts():

    posts = mongo.db.posts.find()

    return render_template('home.html', posts=posts)

@app.route('/new_post', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        post_title = request.form.get('post_title')
        
        new_post = {
            'title': post_title,
            'post_description': request.form.get('post_description'),
            'style': request.form.get('style'),
            'picture_url': request.form.get('picture_url'),
            'date_created': request.form.get('date_created')
        }

        result = mongo.db.posts.insert_one(new_post)
        return redirect(url_for('greeting_posts'))

    else:
        return render_template('new_post.html') 

if __name__ == '__main__':
    app.run(debug=True)