

class Property(object):

    def __init__(self, content):
        self._content = content

    def __str__(self):
        return self._content

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return str(self) == str(other)