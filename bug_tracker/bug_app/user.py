from bson import ObjectId
from flask import url_for, redirect

from bug_tracker.config import bug_tracker_db


class User:

    def __init__(self) -> None:
        self.user_tracker_collection = bug_tracker_db["user"]

    def create_user(self, user) -> None:
        print(user)
        self.user_tracker_collection.insert_one(user)
        return redirect(url_for('view_bug'))

    def delete_user(self) -> None:
        pass

    def get_user(self) -> None:
        pass

    def list_user(self) -> None:
        return self.user_tracker_collection.find()

    def update_user(self, userid, newuser) -> None:
        self.user_tracker_collection.update_one(
            {"_id": ObjectId(userid)},
            {"$set": {"username": newuser}}
        )
        return redirect(url_for('view_bug'))
