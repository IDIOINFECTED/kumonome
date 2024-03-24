import random
class Query:
    def __init__(self,length):
        self.length = length
    def rand_qgen(self):
        chars = "abcdefghijklnopqrstuvwxyz1234567890_-"
        link = ""
        for i in range(self.length):
            link += random.choice(chars)
        query = f"inurl:{link}"
        return query