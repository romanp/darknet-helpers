# darknet-helpers
Python helper functions for Darknet usage

# function "plot_learning_curve.py"
Plots 2-D learning curve (abscissa=epochs, ordinate=AVG training loss) given a file named './train.out'.
train.out is the stdout of Darknet training
```
./darknet detector train <data> <cfg> <arch> > train.out
```

# bash-script "cpproc.sh"
Detects standard file './predictions.png' and moves file to './result/predictions-<x>.png' with increasing
index <x> >=0. It allows processing of multiple images referred by a text file './imgfiles.txt'.
```
cat imgfiles.txt 
data/horses.jpg
data/dog.jpg
./cpproc.sh &
./darknet detect cfg/yolo.cfg yolo.weights < imgfiles.txt
ls result
predictions-0.png  predictions-1.png
pgrep -f cpproc.sh | xargs kill -15
```
 
