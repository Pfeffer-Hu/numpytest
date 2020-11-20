import numpy as np


def load_file(examples_list_file):
    # with the function "np.genfromtxt" we can split every line from a file across delimeter
    lines = np.genfromtxt(examples_list_file, delimiter=" ", dtype=[('col1', 'S120'), ('col2', 'i8')])
    examples = []
    labels = []
    for example, label in lines:
        examples.append(example)
        labels.append(label)
    return np.asarray(examples), np.asarray(labels), len(lines)


train_file = 'datei_np_genfromtxt'
examples, labels, examples_num = load_file(train_file)
for i in range(examples_num):
    print('No', i, 'path', examples[i], 'label is', labels[i])