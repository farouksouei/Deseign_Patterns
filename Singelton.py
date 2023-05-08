class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("You cannot create more than one instance of Singleton class.")
        else:
            Singleton.__instance = self
