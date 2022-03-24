"""
    GaPP: Gaussian Processes in Python
    Copyright (C) 2012, 2013  Marina Seikel
    University of Cape Town
    University of Western Cape
    marina [at] jorrit.de

    This file is part of GaPP.

    GaPP is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GaPP is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""



from gapp.covfunctions.squex import SquaredExponential
from gapp.covfunctions.dsquex import DoubleSquaredExponential
from gapp.covfunctions.mat32 import Matern32
from gapp.covfunctions.mat52 import Matern52
from gapp.covfunctions.mat72 import Matern72
from gapp.covfunctions.mat92 import Matern92
from gapp.covfunctions.cauchy import Cauchy
from gapp.covfunctions.ratquad import RationalQuadratic
from gapp.covfunctions.doublecov import DoubleCovariance
from gapp.covfunctions.mdsquex import MultiDSquaredExponential
from gapp.covfunctions.mddsquex import MultiDDoubleSquaredExponential
from gapp.covfunctions.mdcauchy import MultiDCauchy
from gapp.covfunctions.mdmat32 import MultiDMatern32
from gapp.covfunctions.mdmat52 import MultiDMatern52
from gapp.covfunctions.mdmat72 import MultiDMatern72
from gapp.covfunctions.mdmat92 import MultiDMatern92

