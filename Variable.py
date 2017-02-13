class Variable:
    def __init__(self, id, type):
        self.id = id
        self.val = None
        self.type = type
    def get_type(self):
        return self.type
    def get_id(self):
        return self.id
    def set_val(self, val):
        self.val = val
    def get_val(self):
        return self.val
    
def init_var(id, type):
    return Variable(id, type)    
    
