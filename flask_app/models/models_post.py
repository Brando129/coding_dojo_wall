from flask_app.config.mysqlconnection import connectToMySQL
# Flash messages import
from flask import flash

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
        query = "SELECT * FROM posts;"
        results = connectToMySQL(db).query_db(query)
        posts = []
        for row in results:
            posts.append(cls(row))
        return posts