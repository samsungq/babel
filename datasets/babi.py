import os
import tarfile

def load_data():
    fname = 'tasks_1-20_v1-2.tar.gz'
    url = 'http://www.thespermwhale.com/jaseweston/babi/tasks_1-20_v1-2.tar.gz'
    os.system("wget -O {0} {1}".format(fname, url))

    tar = tarfile.open(fname, "r:gz")
    tar.extractall()
    tar.close()

    os.remove(fname)