from time import sleep

import numpy as np
import sympy as sp
from sympy import Matrix
import logging
import time
logging.basicConfig(level=logging.DEBUG)
logging.debug("This will get logged.")
import time
def read_parameters_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        q = int(lines[0])
        m, n, k = map(int, lines[1].split())
        index = 2
        A = [list(map(int, lines[i].split())) for i in range(index, index + n)]
        index += n
        B = [list(map(int, lines[i].split())) for i in range(index, index + k)]
        index += k
        C = [list(map(int, lines[i].split())) for i in range(index, index + n)]
        index += n
        D = [list(map(int, lines[i].split())) for i in range(index, index + k)]
        return q, m, n, k, A, B, C, D

class LinearAutomaton:
    def __init__(self, q, m, n, k, A, B, C, D):
        self.q = q
        self.m = m
        self.n = n
        self.k = k
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.start = []

    def set_initial_state(self, start):
        if len(start) != self.n:
            raise ValueError("Размер начального состояния не соответствует n")

        self.start = start




    def process_input(self, input_vector, start):
        if len(input_vector) != self.m:
            raise ValueError("Размер входного вектора не соответствует m")
        logging.info(A)
        logging.info(B)
        logging.info(C)
        logging.info(D)
        sleep(1)
        new_start = np.add(np.dot(np.array(self.start), np.array(A)), np.dot(np.array(input_vector), np.array(B))) % self.q
        output = np.add(np.dot(np.array(self.start), np.array(C)), np.dot(np.array(input_vector), np.array(D))) % self.q
        self.start = new_start
        return output

    def run(self):
        while True:
            try:
                raw_input = input(f"Введите входной вектор через пробел(размерность {m} * {1}): ")
                input_vector = list(map(int, raw_input.split()))
                output = self.process_input(input_vector, self.start)
                print("Выходной вектор:", output)
            except Exception as e:
                print("Ошибка:", e)
                break

sleep(1)
parameters_file = "data.txt"
print(read_parameters_from_file(parameters_file))
q, m, n, k, A, B, C, D = read_parameters_from_file(parameters_file)
automat = LinearAutomaton(q, m, n, k, A, B, C, D)

raw_start = input(f"Введите стартовое состояние через пробел(размернось {n} * {1}): ")
start_vector = list(map(int, raw_start.split()))
automat.set_initial_state(start_vector)
automat.run()













