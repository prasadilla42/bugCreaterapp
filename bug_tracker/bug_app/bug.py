from bson import json_util, ObjectId
from flask import url_for, redirect

from bug_tracker.config import bug_tracker_db


class Bug:

    def __init__(self) -> None:
        self.bug_tracker_collection = bug_tracker_db["bug"]

    def create_bug(self, bug):
        self.bug_tracker_collection.insert_one(bug)
        return redirect(url_for('view_bug'))

    def close_bug(self, query) -> None:
        self.bug_tracker_collection.delete_one(query)
        return "bug deleted successfully"

    def list_bug(self) -> None:
        return self.bug_tracker_collection.find()

    def get_bug(self, ):
        return {"bug_id": "1", "bug_name": "demo_bug"}

    def change_user(self, username, bugid):
        self.bug_tracker_collection.update_one(
            {"_id": ObjectId(bugid)},
            {"$set": {"username": username}}
        )
        return redirect(url_for('view_bug'))
