# import the necessary packages
from pyimagesearch.nn.conv import lenet
from keras.utils import plot_model
# initialize LeNet and then write the network architecture
# visualization graph to disk
model = lenet.LeNet.build(28, 28, 1, 10)
plot_model(model, to_file="lenet.png", show_shapes=True)
