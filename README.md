# darknet-helpers
Python helper functions for Darknet usage

# Function "plot_learning_curve.py"
Plots 2-D learning curve (abscissa=epochs, ordinate=AVG training loss) given a file named 'train.out'.
train.out is the stdout of Darknet training
```
./darknet detector train <data> <cfg> <arch> > train.out
```
