import math
import random


class EntryNeuron:
    hidden_neurons = []
    hidden_neurons_way = []
    parameter = ""
    parameter_value = None

    def __init__(self, parameter):
        self.parameter = parameter

        # self.neuron_graph = dict(zip(neuron_cost, neurons))

    def send_to_hidden(self):
        for i in range(0, len(self.hidden_neurons)):
            self.hidden_neurons[i].add_input(self.parameter_value, self.hidden_neurons_way[i])


# 1. Hidden Neuron gets input from Entry Neuron with its cost
# 2. Hidden Neuron executes linear combination of input values
# 3. The value is sent to out Neuron
class HiddenNeuron:
    way_to_out_neuron = 0
    function_type = None
    outer_neuron = None

    def __init__(self, function_type):
        self.function = function_type

    def execute(self):
        print "TODO"

    def add_input(self, stat, cost):
        # TODO: function to integrate cost into stat value
        self.input.append(stat)


class OutNeuron:
    def __init__(self):
        pass


def randomize_way_array(array_size, min_value, max_value):
    a = []
    for i in range(0, array_size):
        a.append(random.uniform(min_value, max_value))
    return a


class NeuronNet:
    input_neurons = []
    hidden_neurons = []
    out_neuron = None

    def __init__(self, input_number, input_parameters, hidden_number, neuron_function):
        self.out_neuron = OutNeuron()
        # initializing hidden neurons
        for i in range(0, hidden_number):
            self.hidden_neurons.append(HiddenNeuron(neuron_function))
            self.hidden_neurons[i].outer_neuron = self.out_neuron
        # initializing Entry Neurons
        for i in range(0, input_number):
            self.input_neurons.append(EntryNeuron(input_parameters[i]))
            # adding hidden neurons
            self.input_neurons[i].hidden_neurons = self.hidden_neurons
        self.init_net_ways()

    def execute(self, input_values):
        for neuron in self.input_neurons:
            neuron.parameter = input_values.getKey

    # initializing starting graph-like net
    def init_net_ways(self):
        for neuron in self.input_neurons:
            neuron.hidden_neurons_way = randomize_way_array(3, 1, 10)

        for neuron in self.hidden_neurons:
            neuron.way_to_out_neuron = random.uniform(1, 10)
