import os
import tarfile

def load_data():
	out_image = 'tasks_1-20_v1-2.tar.gz'
	url = 'http://www.thespermwhale.com/jaseweston/babi/tasks_1-20_v1-2.tar.gz'
	os.system("wget -O {0} {1}".format(out_image, url))

    tar = tarfile.open(out_image, "r:gz")
    tar.extractall()
    tar.close()