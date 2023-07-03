from flask_app.config.mysqlconnection import connectToMySQL
# Flash messages import
from flask import flash
# Import the User class
from flask_app.models import models_user

# Database name
db = "coding_dojo_wall_schema"

# Posts class
class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        """We make a user object so every time a post
        is made we store the user object rather than the user id"""
        self.user = data['user']

    # Classmethod for creating/saving a post.
    @classmethod
    def save_post(cls, data):
        print("Creating post...")
        query = """INSERT INTO posts (content, user_id)
                VALUES (%(content)s, %(user_id)s);"""
        print("Saving post...")
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for deleting a post.
    def destroy(cls, post_id):
        print("Destroying the post...")
        query = "DELETE FROM posts WHERE id = %(id)s"
        connectToMySQL(db).query_db(query, {"id": post_id})
        return post_id

    #Classmethod for getting all the posts.
    @classmethod
    def get_all_posts(cls):
        print("Getting all the posts...")
        query = """SELECT * FROM posts
                JOIN users on posts.user_id = users.id;"""
        results = connectToMySQL(db).query_db(query)
        all_posts = []
        # Iterate over raw data list of post dictionaries
        for row in results:
            posting_user = models_user.User({
                "id": row['user_id'],
                "email": row['email'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "password": row['password'],
            })
            # Make post instance with a user object
            new_post = Post({
                "id": row['id'],
                "content": row['content'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user": posting_user
            })
            # Add post to all_posts list
            all_posts.append(new_post)
        return all_posts