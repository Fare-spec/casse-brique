import os, yaml, murdebrique

class FileHandler(object):

    def __init__(self):

        path = os.getcwd() + '/levels.yml'
        with open(path, 'r') as fichier:
            self.file = yaml.safe_load(fichier)
        self.current_level = 0

    def next_level(self):
        if self.current_level >= len(self.file):
            return None
        bricks = self.file[self.current_level]
        self.current_level += 1

        return bricks


if __name__ == '__main__':

    handler = FileHandler()
    handler.next_level()