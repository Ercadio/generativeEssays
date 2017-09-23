import tensorflow as tf

class DeepNetwork:
    def __init__(self, inputLen, outputLen, layers):
        self._layers = list()
        lastLength = inputLen
        for l in layers:
            self._layers.push({"weights": tf.Variable(tf.random_normal([lastLength,l])), "biases": tf.Variable(tf.random_normal([l]))})
            lastLength = l
        self._output = {"weights": tf.Variable(tf.random_normal([lastLength, outputLen])), "biases": tf.Variable(tf.random_normal([outputLen]))}
    def run(self, input):
        state = input
        for l in self._layers:
            state = tf.add(tf.matmul(l["weights"], state), l["biases"])
            state = tf.nn.relu(state)
        state = tf.add(tf.matmul(self._output["weights"], state), self._output["biases"])
        return tf.nn.relu(state)
    def train(self, input):
        prediction = self.run(input)
        cost = tf.reduce_mean()