class User():

    __id: int
    __user_name: str
    __email: str
    __key: str

    def __init__(self, user_name, email, key):
        self.__user_name = user_name
        self.__email = email
        self.__key = key

    def __repr__(self):
        return f'{self.__id}, {self.__user_name}, {self.__email},{self.__key}'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @user_name.deleter
    def user_name(self):
        del self.__user_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @key.deleter
    def key(self):
        del self.__key
