# Randomizer_simple
A simple approach to write fake randomizer function. Fake means that it does not depend on any other random values, except those it has generated itself.

The approach bases on two sinusoid functions with different periods and amplitude=32767. The high period of first function results to the statement: small change in X axis can result very big change in Y axis. Thus we try to make random behaviour for these small changes. In addition we don't want our function to give the same results each call, so that's why we will save variable i - number of calls of ```randomizer.random()``` and variable x - parameter which is passed to the sinusoid function.

To save it in 1 file, I have added the ```randomizer.save()``` method which rewrites the source code for every call of ```randomizer.random()```.

Randomizer is realized in Randomizer class, it's instance is made as follows:
```python
randomizer = Randomizer()
randomizer.random() # return random number from -32767 to 32767
```

# Test
The test.py generates dataset.csv with 1000 random numbers geterated by randomizer. They are visualized in 1000_distibution.png.
On the image we can see that number located not quite randomly. There more dots in top (Y axis frmo 30000 to 32767) and bottom (Y axis from -30000 to 32767).
But all in all it is a fare payment for such simple approach.
