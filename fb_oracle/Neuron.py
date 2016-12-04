class EntryNeuron:
    neuron_graph = []

    def __init__(self, parameter, parameter_value, neurons, neuron_cost):
        self.parameter = parameter
        self.parameter_value = parameter_value
        self.neurons = neurons
        self.neuron_graph = dict(zip(neuron_cost, neurons))

    def send_to_hidden(self):
        for cost, neuron in self.neuron_graph.iteritems():
            neuron.add_input(self.parameter_value, cost)


# 1. Hidden Neuron gets input from Entry Neuron with its cost
# 2. Hidden Neuron executes linear combination of input values
# 3. The value is sent to out Neuron 
class HiddenNeuron:
    way_to_out_neuron = 0

    def __init__(self, function_type, out_neuron, cost_to_out):
        self.input = None
        self.function = function_type
        self.output = out_neuron
        self.way_to_out_neuron = cost_to_out

    def execute(self):
        print "TODO"

    def add_input(self, stat, cost):
        # TODO: function to integrate cost into stat value
        self.input.append(stat)


class OutNeuron:
    def __init__(self):
        pass
