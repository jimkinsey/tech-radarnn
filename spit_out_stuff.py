from textgenrnn import textgenrnn
t = textgenrnn('textgenrnn_weights.hdf5')
t.generate(30, temperature=0.75)