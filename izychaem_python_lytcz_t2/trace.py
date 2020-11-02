class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace: {}'.format(attrname))
        return getattr(self.wrapped, attrname)


if __name__ == '__main__':
    a = Wrapper([1, 2, 3])
    a.append(5)
    print(a.wrapped)