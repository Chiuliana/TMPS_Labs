class User:
    # Represents a library user with a name and user ID
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User {self.name} (ID: {self.user_id})"
