class Queue():


    def __init__(self):
        self.__q__ = list()

    def enqueue(self, data):
        self.__q__.append(data)

    def dequeue(self):
        if (len(self.__q__) == 0):
            return None
        return self.__q__.pop(0)


