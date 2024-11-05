import numpy as np
import matplotlib.pyplot as plt

def calculate_sinus(angle):
    """Возвращает синус угла в радианах."""
    return np.sin(angle)

def calculate_cosinus(angle):
    """Возвращает косинус угла в радианах."""
    return np.cos(angle)

def plot_trigonometric_functions():
    """Строит графики синуса и косинуса."""
    angles = np.linspace(0, 2 * np.pi, 100)
    sine_values = calculate_sinus(angles)
    cosine_values = calculate_cosinus(angles)

    plt.figure(figsize=(10, 5))
    plt.plot(angles, sine_values, label='Синус', color='blue')
    plt.plot(angles, cosine_values, label='Косинус', color='red')
    plt.title('Графики синуса и косинуса')
    plt.xlabel('Угол (радианы)')
    plt.ylabel('Значение')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_trigonometric_functions()
