class base:
    def __init__(self, name=None):
        self.name = name
        self.is_struct = False

    def __str__(self):
        return str(self.value)

    def __getitem__(self, key):
        if key == 1:
            return self.type
        else:
            return self.value

class INTEGER(base):
    def __init__(self, value=0, *args, **kwargs):
        self.value = int(value)
        self.type = 'INTEGER'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        self.value = int(new_value)

class REAL(base):
    def __init__(self, value=.0, *args, **kwargs):
        self.value = float(value)
        self.type = 'REAL'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        self.value = float(new_value)

class STRING(base):
    def __init__(self, value='', *args, **kwargs):
        self.value = str(value)
        self.type = 'STRING'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        self.value = str(new_value)

    def __str__(self):
        return '"' + self.value + '"'

class CHAR(base):
    def __init__(self, value='', *args, **kwargs):
        self.value = str(value)[0]
        self.type = 'CHAR'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        self.value = str(new_value)[0]

    def __str__(self):
        return "'" + self.value + "'"

class BOOLEAN(base):
    def __init__(self, value=True, *args, **kwargs):
        self.value = bool(value)
        self.type = 'BOOLEAN'
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return {True: 'TRUE', False: 'FALSE'}[self.value]

    def set_value(self, new_value):
        self.value = bool(new_value)

class ARRAY(base):
    def __init__(self, value={}, *args, **kwargs):
        self.value = value
        self.type = 'ARRAY'
        super().__init__(*args, **kwargs)

    def get_str(self, v):
        if v[1] == 'ARRAY':
            l = []
            for i in v[0].values():
                l.append(self.get_str(i))
            return '[' + ', '.join(l) + ']'
        else:
            return str(v[0])

    def __str__(self) -> str:
        l = []
        for i in self.value.values():
            l.append(self.get_str(i))
        return '[' + ', '.join(l) + ']'

    def set_value(self, value):
        self.value = value

from enum import Enum
class ENUM(base):
    def __init__(self, *args, **kwargs):
        self.value = None
        self.type = 'ENUM'
        super().__init__(*args, **kwargs)

    def set_value(self, value):
        self.value = Enum(self.name, value)
