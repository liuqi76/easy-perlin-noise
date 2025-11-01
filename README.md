# easy-perlin-noise
to generate a perlin-noise pic or matrix
to run:
```bash
python pn.py mode size lattice
```
- mode=m:generate matrix file(value ranges in (-1,1))
- mode=p:generate Grayscale picture
- size will determine the size of file, the size will be $2^sof$ * $2^sof$
- lattice will determine how many grad vectors will be in each axis
