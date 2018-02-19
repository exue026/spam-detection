import matplotlib.pyplot as plt

def plot(x_data, y_data, x_label, y_label, title):
    plt.plot(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()