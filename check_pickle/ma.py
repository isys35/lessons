import pickle


class Object:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info(self):
        print(self.name)


if __name__ == '__main__':
    objects = [Object(i, 'object name') for i in range(10)]
    print(objects)
    with open('data', 'wb') as f:
        pickle.dump(objects, f)
    with open('data', 'rb') as f:
        objects = pickle.load(f)
    for object in objects:
        print(object.id)