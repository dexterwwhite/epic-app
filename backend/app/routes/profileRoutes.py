from flask import Blueprint
from ..services import getAllUsers

profileBlueprint = Blueprint('profile', __name__)

@profileBlueprint.route('/profile/getAllProfiles', methods=['GET'])
def getAllProfiles():
    users = getAllUsers()
    for user in users:
        print(user)  # Each user is a dictionary of the row
    return users