from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_post

# GET routes
@app.route('/posts/delete/<post_id>')
def destroy_post(post_id):
    print("Deleting post - ", post_id)
    # Post.destroy(post_id)
    return redirect('/wall')


# POST routes
@app.route('/posts', methods=['POST'])
def create_post():
    print("Create post route...")
    print(request.form)
    # Post.save(request.form)
    return redirect('/wall')

