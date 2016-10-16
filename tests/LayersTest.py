import unittest
from ann.Layers import HiddenLayer, LinearRegressionLayer, LogisticRegressionLayer


class HiddenLayerTest(unittest.TestCase):
    def test_initialization(self):
        # Given
        input_vector = [[0]]
        n_in = 2  # a total of 6 in and out will result into weights between -1 and 1 according to xavier method
        n_out = 4

        # When
        hidden_layer = HiddenLayer(seed=1234, input_stream=input_vector, n_in=n_in, n_out=n_out)

        # Then
        weights = hidden_layer.weights.eval()
        for column in weights:
            for value in column:
                self.assertTrue(-1 <= value <= 1)

        bias = hidden_layer.bias.eval()
        for b in bias:
            self.assertEqual(b, 0)


class LinearRegressionTest(unittest.TestCase):
    def test_error(self):
        # Given
        input_vector = [[0]]
        n_in = 1
        n_out = 1

        # When
        linear_regression_layer = LinearRegressionLayer(seed=1234, input_stream=input_vector, n_in=n_in, n_out=n_out)

        # Then
        error = 2
        sq_error = error * error
        self.assertEqual(sq_error, linear_regression_layer.error([error]).eval())

    def test_prediction(self):
        # Given
        input_vector = [[1]]
        n_in = 1  # a total of 6 in and out will result into weights between -1 and 1 according to xavier method
        n_out = 5

        # When
        linear_regression_layer = LinearRegressionLayer(seed=1234, input_stream=input_vector, n_in=n_in, n_out=n_out)

        # Then
        predictions_vector = linear_regression_layer.predict().eval()[0]
        for prediction in predictions_vector:
            self.assertTrue(-1 <= prediction <= 1)


class LogisticRegressionTest(unittest.TestCase):
    def test_error_same_class(self):
        # Given
        classification = 0
        input_vector = [[classification]]

        logistic_regression_layer = LogisticRegressionLayer(seed=1234, input_stream=input_vector, n_in=1, n_out=1)

        # When
        error = logistic_regression_layer.error([classification]).eval()

        # Then
        difference = 0
        self.assertEqual(error, difference)

    def test_error_different_class(self):
        # Given
        class1 = 0
        class2 = 1
        input_vector = [[class1]]

        logistic_regression_layer = LogisticRegressionLayer(seed=1234, input_stream=input_vector, n_in=1, n_out=1)

        # When
        error = logistic_regression_layer.error([class2]).eval()

        # Then
        difference = 1
        self.assertEqual(error, difference)