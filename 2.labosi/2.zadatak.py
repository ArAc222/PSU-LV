import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("C:\\Users\\student\\PycharmProjects\\pythonProject\\main\\venv\\mtcars (2).csv", "rb"), usecols=(1, 2, 3, 4, 5, 6),
                  delimiter=",", skiprows=1)
plt.scatter(x = data[:, 0], y = data[:, 3], color = 'black',s=data[:,5]*10)

for i in range(2, 32):
        plt.text(data[i,0], data[i, 3], s=data[i, 5], fontsize=10)
plt.ylabel('hp')
plt.xlabel('mpg')

mpg_values = data[:,0]
print('Minimalna vrijednost mpg za automobile: ', np.min(mpg_values))
print('Maksimalna vrijednost mpg za automobile: ', np.max(mpg_values))
print('Srednja vrijednost mpg za automobile', np.mean(mpg_values))

mpg_value = data[data[:, 1]==6, 0]
print('Minimalna vrijednost mpg za automobile sa 6 cilindara: ', np.min(mpg_value))
print('Maksimalna vrijednost mpg za automobile sa 6 cilindara: ', np.max(mpg_value))
print('Srednja vrijednost mpg za automobile sa 6 cilindara', np.mean(mpg_value))

plt.show()
