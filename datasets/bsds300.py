import os
import tarfile

def load_data():
    fname = "BSDS300-images"
    url = "https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300-images.tgz"
    os.system("wget -O {0} {1}".format(fname, url))

    tar = tarfile.open(fname, "r:gz")
    tar.extractall()
    tar.close()

    os.remove(fname)