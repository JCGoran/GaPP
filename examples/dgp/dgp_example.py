"""
This is an example how to use the dgp module of GaPP.
You can run it with 'python dgp_example.py'.
"""


from gapp import dgp
from numpy import loadtxt, savetxt



if __name__=="__main__":
    # load the data from inputdata.txt
    (X, Y, Sigma) = loadtxt("../inputdata.txt", unpack='True')
    
    # nstar points of the function will be reconstructed 
    # between xmin and xmax
    xmin = 0.0
    xmax = 10.0
    nstar = 200

    # initial values of the hyperparameters
    initheta = [2.0, 2.0]

    # initialization of the Gaussian Process
    g = dgp.DGaussianProcess(X, Y, Sigma, cXstar=(xmin, xmax, nstar))

    # training of the hyperparameters and reconstruction of the function
    (rec, theta) = g.gp(theta=initheta)

    # reconstruction of the first, second and third derivatives.
    # theta is fixed to the previously determined value.
    (drec, theta) = g.dgp(thetatrain='False')
    (d2rec, theta) = g.d2gp()
    (d3rec, theta) = g.d3gp()

    # save the output
    savetxt("f.txt", rec)
    savetxt("df.txt", drec)
    savetxt("d2f.txt", d2rec)
    savetxt("d3f.txt", d3rec)


    # test if matplotlib is installed
    try:
        import matplotlib.pyplot
    except:
        print("matplotlib not installed. no plots will be produced.")
        exit
    # create plot
    import plot
    plot.plot(X, Y, Sigma, rec, drec, d2rec, d3rec)

