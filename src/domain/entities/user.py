class User:
    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def save(self, dynamodb):
        users_table = dynamodb.Table('Users')
        users_table.put_item(
            Item={
                'username': self.username,
                'email': self.email,
                'password': self.password,  # hash the password before storing it
                'is_admin': self.is_admin
            }
        )

    def is_client(self):
        return not self.is_admin

    def is_administrator(self):
        return self.is_admin
