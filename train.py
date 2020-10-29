from textgenrnn import textgenrnn
t = textgenrnn()
t.train_from_file('tools.txt', num_epochs=5)