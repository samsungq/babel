# babel
treat data as code. 

easily load commonly used datasets such as mnist, cifar, imagenet.

## usage
```python
import mnist

# fetch mnist data
train_data, test_data = mnist.load_data()  

# separate train_data into X, y
X_train = train_data[0]
y_train = train_data[1]

# examine
plt.imshow(X_train[0])
```
