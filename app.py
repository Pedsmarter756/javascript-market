import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask_bcrypt import bcrypt


app = Flask(__name__)



app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')



mongo = PyMongo(app)

# MongoDB collections

users_collection = mongo.db.users
posts_collection = mongo.db.posts
categories_collection = mongo.db.categories



# Routes

@app.route('/', methods=['POST', 'GET'])
def home():
    categories = list(categories_collection.find())
    posts = posts_collection.find().sort('_id', pymongo.DESCENDING)
    return render_template('home.html',
                        posts=posts,
                        categories=categories)


@app.route('/<category_name>', methods=['GET'])
def filter_list(category_name):
    categories = list(categories_collection.find())
    category_name = categories_collection.find_one(
        {'category_name': category_name})
    posts = posts_collection.find()
    return render_template(
        'filter.html',
        categories=categories,
        category_name=category_name,
        posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        existing_user = users_collection.find_one(
            {'name': request.form.get('username')})
        if existing_user:
            session['username'] = request.form.get('username')
            return redirect('/loggedin/' + session['username'])
        return redirect(url_for('signup'))
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        existing_user = \
            users_collection.find_one(
                {'name': request.form.get('username')})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form.get('password')
                                    .encode('utf-8'), bcrypt.gensalt())
            users_collection.insert(
                {'name': request.form.get('username'), 'password': hashpass})
            session['username'] = request.form.get('username')
            return redirect('/loggedin/' + session['username'])
    return render_template('signup.html')


@app.route('/loggedin/<username>', methods=['GET', 'POST'])
def loggedin(username):
    posts = \
        posts_collection.find({'added_by': session['username']})\
        .sort('name', pymongo.ASCENDING)
    return render_template(
        'profile.html',
        username=session['username'],
        posts=posts
        )


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/add_post')
def add_post():
    return render_template('addpost.html',
                        categories=categories_collection.find())


@app.route('/insert_post', methods=['POST'])
def insert_post():
    posts= posts_collection 
    posts.insert_one({
        'category': request.form.get('category_name'),
        'name': request.form.get('name'),
        'make': request.form.get('makes'),
        'year_modal': request.form.get('year'),
        'quantity': request.form.get('quantity'),
        'image': request.form.get('image'),
        'added_by': session['username'],
        'technics': request.form.getlist('technic'),
        'contact': request.form.get('contact'),
        'condition': request.form.get('condition'),
        'price':request.form.get('price')
        })
    return redirect(url_for('loggedin', username=session['username']))


@app.route('/update_post/<post_id>', methods=['POST'])
def update_post(post_id):
    posts_collection.update({'_id': ObjectId(post_id)}, {
        'category': request.form.get('category_name'),
        'name': request.form.get('name'),
        'make': request.form.get('makes'),
        'year_modal': request.form.get('year'),
        'image': request.form.get('image'),
        'quantity': request.form.get('quantity'),
        'technics': request.form.getlist('technic'),
        'contact': request.form.get('contact'),
        'condition': request.form.get('condition'),
        'price':request.form.get('price'),
        'added_by': session['username'],
        })
    return redirect(url_for('loggedin', username=session['username']))


@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    posts_collection.remove({'_id': ObjectId(post_id)})
    return redirect(url_for('loggedin', username=session['username']))


@app.route('/post/<post_id>')
def post(post_id):
    post = posts_collection.find_one({'_id': ObjectId(post_id)})
    return render_template('post.html', post=post)


@app.route('/categories')
def categories():
    categories = \
        categories_collection.find().sort('category_name', pymongo.ASCENDING)
    return render_template('categories.html',
                        categories=categories)


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form['category_name']}
    categories_collection.insert_one(category_doc)
    return redirect(url_for('categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    categories_collection.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))

@app.route('/edit_post/<post_id>')
def edit_post(post_id):
    post = posts_collection.find_one({'_id': ObjectId(post_id)})
    _categories = categories_collection.find()
    category_list = [category for category in _categories]
    return render_template('editpost.html', post=post,
                        categories=category_list)


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                        category=categories_collection.find_one(
                            {'_id': ObjectId(category_id)}
                            ))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories_collection.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form['category_name']})
    return redirect(url_for('categories'))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=False)


