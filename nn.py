import random
import math

class NeuralNetwork:
	LEARNING_RATE = 0.5

	def __init__(self, num_inputs, num_hidden, num_outputs, hidden_layer_weights = None, hidden_layer_bias = None, output_layer_weight = None, output_layer_bias = None):
		self.num_inputs = num_inputs

		self.hidden_layer = NeuronLayer(num_hidden, hidden_layer_bias)
		self.output_layer = NeuronLayer(num_outputs, output_layer_bias)

		self.init_weights_from_inputs_to_hidden_layer_neurons(hidden_layer_weights)
		self.init_weights_from_hidden_layer_neurons_to_output_layer_neurons(output_layer_weight)

	def init_weights_from_inputs_to_hidden_layer_neurons(self, hidden_layer_weights):
		weight_num = 0
		for h in range(len(self.hidden_layer.neurons)):
			for i in range(self.num_inputs):
				if not hidden_layer_weights:
					self.hidden_layer.neurons[h].weights.append(random.random())
				else:
					self.hidden_layer.neurons[h].weights.append(hidden_layer_weights[weight_num])
				weight_num += 1

	def init_weights_from_hidden_layer_neurons_to_output_layer_neurons(self, output_layer_weights):
		weight_num = 0
		for o in range(len(self.output_layer.neurons)):
			for h in range(len(self.hidden_layer.neurons)):
				if not output_layer_weights:
					self.output_layer.neurons[o].weights.append(random.random())
				else:
					self.output_layer.neurons[o].weights.append(output_layer_weights[weight_num])
				weight_num += 1

	def inspect(self):
		print('------')
		print('* Inputs: {}'.format(self.num_inputs))
		print('------')
		print('Hidden Layer')
		self.hidden_layer.inspect()
		print('------')
		print('* Output Layer')
		self.output_layer.inspect()
		print('------')

	def feed_forward(self,inputs):
		print()










