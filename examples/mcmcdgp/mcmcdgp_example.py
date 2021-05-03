from gapp import mcmcdgp
import numpy as np
from numpy import loadtxt, random, savetxt, zeros


if __name__=="__main__":
    (X, Y, Sigma) = loadtxt("../inputdata.txt", unpack='True')
    (DX, DY, DSigma) = loadtxt("../dinputdata.txt", unpack='True')

    xmin = 0.0
    xmax = 10.0
    nstar = 50

    nwalker = 20
    theta0 = random.normal(2.0, 0.2, (nwalker, 2))

    g = mcmcdgp.MCMCDGaussianProcess(X, Y, Sigma, theta0, Niter=50,
                                     dX=DX, dY=DY, dSigma=DSigma,
                                     cXstar=(xmin, xmax, nstar),
                                     threads=4, reclist=[0, 1])



    (Xstar, rec, drec) = g.mcmcdgp()


    savetxt("rec.txt", rec)
    savetxt("drec.txt", drec)
    savetxt("Xstar.txt", Xstar)

    pred = zeros((nstar,3))
    pred[:, 0] = Xstar[:, 0]
    pred[:, 1] = np.mean(rec, axis=1)
    pred[:, 2] = np.std(rec, axis=1)

    savetxt("f.txt", pred)


    dpred = zeros((nstar,3))
    dpred[:, 0] = Xstar[:, 0]
    dpred[:, 1] = np.mean(drec, axis=1)
    dpred[:, 2] = np.std(drec, axis=1)

    savetxt("df.txt", dpred)


    # test if matplotlib is installed
    try:
        import matplotlib.pyplot
    except:
        print("matplotlib not installed. no plots will be produced.")
        exit
    # create plot
    import plot
    plot.plot(X, Y, Sigma, DX, DY, DSigma, pred, dpred)

