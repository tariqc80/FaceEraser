# fceEraser.py

import fire


class Erase():

    def __init__(self):
        pass

    def posts(self, since, to):
        print('deleting posts')


class Actions:

    def __init__(self):
        self.erase = Erase()


if __name__ == '__main__':
    fire.Fire(Actions)
