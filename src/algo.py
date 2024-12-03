import numpy as np

class Relu:
    def ReluAlgo(self):
        print('I hate math')

    def relu(x):
        return np.maximum(0, x)

# Generate a random array of inputs
    def generate_random_array(size, low=-10, high=10):
        return np.random.uniform(low, high, size)

# Example usage
    if __name__ == "__main__":
        size = 10  # Number of elements in the array
        random_inputs = generate_random_array(size)
        print("Random Inputs:", random_inputs)

        relu_outputs = relu(random_inputs)
        print("ReLU Outputs:", relu_outputs)