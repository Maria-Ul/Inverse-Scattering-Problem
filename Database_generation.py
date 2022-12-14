import PyMieScatt as ps
import numpy as np
import pandas as pd

env_refractive_index = 1
n_0 = 1
wavelength = 660  # nm wavelength

theta, _, _, scatter_unpolarized = ps.ScatteringFunction(
    m=1.1,  # particle refractive index
    wavelength=660,
    diameter=5.4,  # in nanometrs
    nMedium=1.0,  # refractive index of enviroment
    minAngle=10,
    maxAngle=65,
    angularResolution=55 / 128,
    space='theta',
    angleMeasure='degrees',
    normalization=None
)

database = pd.DataFrame(columns=['radius', 'refractive_index'] + list(theta))
diameter_grid = np.arange(1730, 15760, 0.1)
refractive_idx_grid = np.arange(1.34, 1.64, 0.01)

diameter_grid.shape, refractive_idx_grid.shape, diameter_grid.shape[0] * refractive_idx_grid.shape[0]

idx = 0
for r in diameter_grid:
    for ref_idx in refractive_idx_grid:
        _, _, _, scatter_unpolarized = ps.ScatteringFunction(
            m=ref_idx,  # particle refractive index
            wavelength=660,
            diameter=2 * r,  # in nanometrs
            nMedium=1.0,  # refractive index of enviroment
            minAngle=10,
            maxAngle=65,
            angularResolution=55 / 128,
            space='theta',
            angleMeasure='degrees',
            normalization=None
        )

        database.loc[idx] = [r, ref_idx] + list(scatter_unpolarized)
        idx += 1
database['radius'].hist()
database.to_csv(
    '/content/drive/MyDrive/ML/обратная задача светорассеяния/databaces/database2000_r500_505_0.1_n1.1_1.5_0.01.csv')

