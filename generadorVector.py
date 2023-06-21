import random

class VectorGenerator:
    def generate_vector(self, size):
        return random.sample(range(1, size + 1), size)
