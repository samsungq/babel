# babel
manage data as code. 

import commonly used datasets such as mnist, [cifar](https://www.cs.toronto.edu/~kriz/cifar.html), imagenet, [bAbI](https://research.fb.com/downloads/babi/), [bsds300](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/) and [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/).

## usage
```python
from datasets import mnist

# fetch mnist data
train_data, test_data = mnist.load_data()  

# separate train_data into X, y
X_train = train_data[0]
y_train = train_data[1]

# examine
plt.imshow(X_train[0])
```
