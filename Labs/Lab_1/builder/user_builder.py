from Labs.Lab_1.domain.user import User

class UserBuilder:
    # Builder class for creating User instances with optional details.
    def __init__(self):
        self.name = None
        self.user_id = None

    def set_name(self, name):
        self.name = name
        return self

    def set_user_id(self, user_id):
        self.user_id = user_id
        return self

    def build(self):
        if not self.name or not self.user_id:
            raise ValueError("Name and User ID are required to build a User.")
        return User(self.name, self.user_id)
