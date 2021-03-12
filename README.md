# SNJ - Spectral neighbor joining 
Code for the paper "Spectral neighbor joining for reconstruction of latent tree models" (https://arxiv.org/abs/2002.12547)


## Installing
You should install the package using pip. cd inside the `snj` folder and run 
```
pip install .
```
Now if you want to import the spectraltree package, for example for an experiment, you can simply run
```
import spectraltree
```

## Testing
To run the test suite, cd to `snj` and run
```
python -m unittest discover
```
To run a specific module:
```
python -m unittest tests.test_snj
```

## Documentation
Run
```
python setup.py build_sphinx
```
(You can also go into the `docs` folder and run `make html`). Then open `docs/_build/html/index.html` in a browser.
