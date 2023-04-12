import pandas as pd
import numpy as np

mtcars = pd.read_csv('C:\\Users\\student\\Downloads\\mtcars.csv')

print(mtcars)

sort_auti = mtcars.sort_values(by=['mpg'])
prvih_pet = sort_auti.tail(5)

print(prvih_pet)

prvi_tri = print(mtcars.query('cyl == [8]').car)

prva_tri = (sort_auti.head(3)).car

print(prva_tri)

prvi_tri = mtcars.query('cyl == [6]')

sr_vr = prvi_tri.mean().mpg

print(sr_vr)

print(mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.200)])

automatic = mtcars[mtcars.am == 1]
manual = mtcars[mtcars.am == 0]

print(automatic['am'].count())
print(manual['am'].count())

print(mtcars[(mtcars.am == 1) & (mtcars.hp > 100)].car)

mtcars["mass_kg"] = mtcars["wt"] * 1000 * 0.45392
print(mtcars[["car", "mass_kg"]])
