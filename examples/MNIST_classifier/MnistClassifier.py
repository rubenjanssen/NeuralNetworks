import six.moves.cPickle as pickle
import gzip
import numpy as np

from ann.Layers import LeNetConvPoolLayer, InputLayer, HiddenLayer, LogisticRegressionLayer
from ann.MultiLayerPerceptron import MultiLayerPerceptronClassifier


def load_data(data_set):
    with gzip.open(data_set, 'rb') as f:
        train_set, _, test_set = pickle.load(f)

    return np.asarray([train_set[0].tolist(), train_set[1].tolist()]).T, np.asarray([test_set[0].tolist(), test_set[1].tolist()]).T


def test_mlp(learning_rate=0.1, data_set='mnist.pkl.gz', batch_size=500):
    # Prepare data
    training_set, test_set = load_data(data_set)

    # Create network
    network_specification = [InputLayer([28, 28]),
                             LeNetConvPoolLayer(feature_map=20, filter=(5, 5), pool=(2, 2)),
                             LeNetConvPoolLayer(feature_map=50, filter=(5, 5), pool=(2, 2)),
                             HiddenLayer(500),
                             LogisticRegressionLayer(10)]
    neural_network = MultiLayerPerceptronClassifier(seed=1234, network_specification=network_specification)

    # Train
    neural_network.train(training_set=training_set, learning_rate=learning_rate, batch_size=batch_size, iterations=1)

    # Test
    print "Error rate of {}%".format(neural_network.test(test_set=test_set, batch_size=batch_size))


if __name__ == '__main__':
    test_mlp()
