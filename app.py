from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

#Setup pymongo DB
app.config["MONGO_URI"] = "mongodb://localhost:27017/postsDatabase"
mongo = PyMongo(app)

@app.route('/')
def greeting_posts():
    #This is rendering the home html and also getting all the posts from the posts database to show on the home page.
    posts = mongo.db.posts.find()

    return render_template('home.html', posts=posts)

@app.route('/new_post', methods=['GET', 'POST']) #This function is going to be used for the user to make a new post and save it into the database
def create():
    if request.method == 'POST':
        post_title = request.form.get('post_title')
        
        #This is getting the data from the form to store into the collection for posts
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

@app.route('/about') #This function is going to render the about.html file 
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)