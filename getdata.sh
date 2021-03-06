mkdir data
mkdir result

wget -O data/train-image.gz http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget -O data/train-label.gz http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
wget -O data/test-image.gz http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
wget -O data/test-label.gz http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz

gzip -d data/train-image.gz
gzip -d data/train-label.gz
gzip -d data/test-image.gz
gzip -d data/test-label.gz

