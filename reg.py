from pathlib import Path
import logging
import time
from time import sleep

logging.basicConfig(level=logging.DEBUG)
logging.debug("This will get logged.")
def read_shift_register_params(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())  # Длина регистра
    psi = list(map(int, lines[2].split()))  # Табличное задание функции ψ
    phi = list(map(int, lines[4].split()))  # Табличное задание функции φ
    logging.info(n)
    logging.info(psi)
    logging.info(phi)
    return n, psi, phi


def shift_register(n, psi, phi, initial_state, input_bits):
    state = initial_state.copy()
    output_bits = []

    for bit in input_bits:
        output_bit = phi[int("".join(map(str, state)), 2)]  # Выходной бит
        output_bits.append(output_bit)
        new_bit = psi[int("".join(map(str, state)), 2)] ^ bit  # Новый бит
        state.pop(0)
        state.append(new_bit)

    return output_bits


if __name__ == "__main__":
    file_path = Path("shift_register_params.txt")  # Путь к файлу с параметрами
    sleep(1)
    n, psi, phi = read_shift_register_params(file_path)

    # Ввод начального состояния
    initial_state = list(map(int, input(f"Введите {n} бит начального состояния: ").split()))

    # Ввод входных бит
    while True:

        input_bits = list(map(int, input("Введите входные биты через пробел: ").split()))

        # Запуск регистра сдвига
        output_bits = shift_register(n, psi, phi, initial_state, input_bits)

        print("Выходные биты:", " ".join(map(str, output_bits)))
