class ItemDiscretoDiretorio():
    def __init__(self, item, ids):
        self.__item = item
        self.__ids = [ids]

    @property
    def item(self):
        return self.__item
    
    @property
    def ids(self):
        return self.__ids
    
    def add_id(self, id):
        self.__ids.append(id)