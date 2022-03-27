
class Token:

    def get_secret_key(self):
        return "func1: secret_key"

    @classmethod
    def encode(cls):
        print( "func1: classmethod: Token.encode is called")
        return cls.get_secret_key(cls)

