import mnist

def loadmnistTrain():
    imgs, labels = mnist.load_mnist(dataset="training", path='../shared_data')
    N=imgs.shape[0]
    x=imgs.reshape(N,-1)
    y=labels.reshape(N,-1)
    print('\'x\' has shape of ' + str(x.shape))
    print('\'y\' has shape of ' + str(y.shape))
    return x, y

def loadmnistTest():
    imgs, labels = mnist.load_mnist(dataset="testing", path='../shared_data')
    N=imgs.shape[0]
    x=imgs.reshape(N,-1)
    y=labels.reshape(N,-1)
    print('\'x\' has shape of ' + str(x.shape))
    print('\'y\' has shape of ' + str(y.shape))
    return x, y
