import math
import random


class EntryNeuron:
    hidden_neurons = []
    hidden_neurons_way = []
    parameter = ""
    parameter_value = None

    def set_input_value(self, value):
        self.parameter_value = value
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
    outer_neuron = None
    input_data = []

    def __init__(self):
        pass

    def execute(self):
        print "TODO"

    def add_input(self, stat, cost):
        # TODO: function to integrate cost into stat value
        print ("VALUE TO HIDDEN:", stat, cost)
        self.input_data.append(stat)
        self.outer_neuron.set_from_hidden(stat * cost)


class OutNeuron:
    final_data = []

    def __init__(self):
        pass

    def set_from_hidden(self, value):
        self.final_data.append(value)

    def get_final_data(self):
        return self.final_data


def randomize_way_array(array_size, min_value, max_value):
    a = []
    for i in range(0, array_size):
        a.append(random.uniform(min_value, max_value))
    return a


class NeuronNet:
    input_neurons = []
    hidden_neurons = []
    out_neuron = None

    def __init__(self, input_number, input_parameters, hidden_number):
        self.out_neuron = OutNeuron()
        # initializing hidden neurons
        for i in range(0, hidden_number):
            self.hidden_neurons.append(HiddenNeuron())
            self.hidden_neurons[i].outer_neuron = self.out_neuron
        # initializing Entry Neurons
        for i in range(0, input_number):
            self.input_neurons.append(EntryNeuron(input_parameters[i]))
            # adding hidden neurons
            self.input_neurons[i].hidden_neurons = self.hidden_neurons
        self.init_net_ways()

    def execute(self, input_values):
        for i in range(0, len(self.input_neurons)):
            self.input_neurons[i].set_input_value(input_values[i])
        for x in self.input_neurons:
            x.send_to_hidden()
        print (self.out_neuron.get_final_data())

    def get_input_parameters(self):
        a = []
        for i in self.input_neurons:
            a.append(i.parameter)
        return a

    def get_from_input_to_hidden_ways(self):
        a = []
        for i in self.input_neurons:
            a.append(i.hidden_neurons_way)
        return a

    # initializing starting graph-like net
    def init_net_ways(self):
        # from entry to hidden neurons
        for neuron in self.input_neurons:
            neuron.hidden_neurons_way = randomize_way_array(3, 1, 10)

        # from hidden to output neuron
        for neuron in self.hidden_neurons:
            neuron.way_to_out_neuron = random.uniform(1, 10)
