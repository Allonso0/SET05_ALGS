import random

class HashTable:
    def __init__(self, size, probing, c1 = 1, c2 = 1, c3 = 1):
        self.size = size
        self.table = [None] * size
        self.probing = probing
        self.c1, self.c2, self.c3 = c1, c2, c3

    def hash(self, key, i):
        if self.probing == 'q':
            return (key + self.c1 * i + self.c2 * i**2) % self.size
        elif self.probing == 'c':
            return (key + self.c1 * i + self.c2 * i**2 + self.c3 * i**3) % self.size

    def insert(self, key):
        i = 0
        while True:
            index = self.hash(key, i)
            if self.table[index] is None:
                self.table[index] = key
                return i
            i += 1
            if i >= self.size:
                raise Exception("Таблица заполнена")

def simulate(probing, size, num_keys):
    collisions = 0
    ht = HashTable(size, probing)
    for _ in range(num_keys):
        key = random.randint(0, 10**6)
        collisions += ht.insert(key)
    return collisions

size = 10000
n_keys = 8000
n_runs = 50

quad_results = []
cube_results = []

for _ in range(n_runs):
    quad_results.append(simulate('q', size, n_keys))
    cube_results.append(simulate('c', size, n_keys))

average_collisions_quad = sum(quad_results) / n_runs
average_collisions_cube = sum(cube_results) / n_runs

print("===================================================")
print("Результаты:")
print(f"Квадратичное пробирование: {average_collisions_quad:.2f} коллизий")
print(f"Кубическое пробирование: {average_collisions_cube:.2f} коллизий")
print("===================================================")
