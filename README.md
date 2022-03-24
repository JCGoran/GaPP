# GaPP
This Gaussian Processes GaPP code auxiliary repository, replacing the original link (http://www.acgc.uct.ac.za/~seikel/GAPP/index.html) which seems to be broken.

GaPP was written by Seikel, Clarkson, Smith 2012 (https://arxiv.org/abs/1204.2832, JCAP06(2012)036).
The algorithm Gaussian processes can reconstruct a function from a sample of data without assuming a parameterization of the function.
The GaPP code can be used on any dataset to reconstruct a function.
It handles individual error bars on the data and can be used to determine the derivatives of the reconstructed function.
The data sample can consist of observations of the function and of its first derivative.

## Installation

Install using pip:

```
python3 -m pip install git+https://github.com/JCGoran/GaPP@feature/python3#GaPP
```

Furthermore, if you want to use the MCMC features of the code, you need to additionally install [emcee](https://github.com/dfm/emcee) and [acor](https://github.com/dfm/acor).

**NOTE**: some parts of the code may not function (Pylint still reports undefined variables), but the examples seem to work fine.

## Contact

Questions about GaPP can be addressed to carlosap87@gmail.com. 
