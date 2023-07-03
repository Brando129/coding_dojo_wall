from flask_app.config.mysqlconnection import connectToMySQL
# Flash messages import
from flask import flash


# Database name
db = "coding_dojo_wall_schema"

# Comment Class
class Comment:
    def __init__ (self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']

    # Classmethod for creating/saving a post.
    @classmethod
    def save_comment(cls, data):
        print("Creating comment...")
        query = """INSERT INTO comments (content, user_id, post_id)
                VALUES (%(content)s, %(user_id)s, %(post_id)s);"""
        print("Saving comment...")
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for deleting a comment.
    @classmethod
    def destroy_comment(cls, post_id):
        print("Destroying the comment...")
        query = "DELETE FROM comments WHERE id = %(id)s"
        connectToMySQL(db).query_db(query, {"id": post_id})
        print("Comment successfully deleted...")
        return post_id

    # Staticmethod for checking if a user's post is blank.
    @staticmethod
    def validate_comment(data):
        print("Validating comment data...")
        is_valid = True
        if len(data['content']) <= 0:
            flash("* Comment content must not be blank", "comment")
            is_valid = False
        print("Validating comment successful...")
        return is_valid