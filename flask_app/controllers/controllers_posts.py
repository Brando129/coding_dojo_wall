from flask_app import app
from flask import redirect, request
from flask_app.models import models_post

# GET routes
# Route for deleting a post.
@app.route('/posts/delete/<post_id>')
def destroy_post(post_id):
    print("Deleting post - ", post_id)
    models_post.Post.destroy(post_id)
    return redirect('/wall')


# POST routes
# Route for creating a new post.
@app.route('/posts', methods=['POST'])
def create_post():
    print("Create post route...")
    post = models_post.Post.validate_post(request.form)
    if not post:
        return redirect('/wall')
    print(request.form)
    models_post.Post.save_post(request.form)
    return redirect('/wall')

