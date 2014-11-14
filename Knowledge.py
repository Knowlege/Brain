"""
Brain.Knowledge
by Jakov Mankas
aka. Knowledge
"""


class Knowledge:
    """
    Class for all data in programm.
    0 - integers
    1 - strings
    """
    def __init__(self, filename):
        self.data = {}
        self.filename = filename + '.knw'
        self.save = bytearray()

    def __repr__(self):
        self.ret = ''
        for x in self.data:
            self.ret += str(x)
            self.ret += ' : '
            self.ret += str(self.data[x])
            self.ret += '\n'
        return self.ret

    def add_data(self, key, info):
        self.key = key
        self.info = info
        self.data[self.key] = self.info

    def save_data(self):
        for thing in self.data:
            if type(thing) == str:
                self.save.append(1)
                for l in thing:
                    self.save.append(ord(l))
                self.save.append(1)
            elif type(thing) == int:
                self.save.append(0)
                for x in range(int(thing / 250)):
                    self.save.append(255)
                self.save.append(thing + 5)
                self.save.append(0)
            if type(self.data[thing]) == str:
                self.save.append(1)
                for l in self.data[thing]:
                    self.save.append(ord(l))
                self.save.append(1)
            elif type(self.data[thing]) == int:
                self.save.append(0)
                for x in range(int(self.data[thing] / 250)):
                    self.save.append(255)
                self.save.append(self.data[thing] + 5)
                self.save.append(0)
        with open(self.filename, 'wb') as output:
            output.write(self.save)


def load(filename):
    with open(filename + '.knw', 'rb') as infile:
        a = bytearray(infile.read())
    rez = Knowledge(filename)
    state = 'key'
    thing = None
    key = None
    data = None
    for x in a:
        print(x)
        if thing == 'integer':
            if x == 0:
                thing = None
                if state == 'key':
                    state = 'data'
                else:
                    state = 'key'
                    rez.add_data(key, data)
                    key = None
                    data = None
            else:
                if state == 'key':
                    key += x - 5
                else:
                    data += x - 5
        elif thing == 'string':
            if x == 1:
                thing = None
                if state == 'key':
                    state = 'data'
                else:
                    state = 'key'
                    rez.add_data(key, data)
                    key = None
                    data = None
            else:
                if state == 'key':
                    key += chr(x)
                else:
                    data += chr(x)
        else:
            if x == 0:
                thing = 'integer'
                print(state == 'key', state)
                if state == 'key':
                    key = 0
                else:
                    data = 0
            elif x == 1:
                thing = 'string'
                print(state == 'key', state)
                if state == 'key':
                    key = ''
                else:
                    data = ''
    return rez
