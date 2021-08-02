import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import scale
from sklearn.metrics import plot_confusion_matrix
from sklearn.utils import resample
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt  

dataset = np.loadtxt('simple_combined_data.csv', delimiter=',')
dataset_no_inj = dataset[dataset[:, 6] == 0]
dataset_inj = dataset[dataset[:, 6] == 1]
dataset_inj = resample(dataset_inj, replace=False, n_samples=120, random_state=2)
dataset_no_inj = resample(dataset_no_inj, replace=False, n_samples=dataset_inj.shape[0], random_state=2)
model_data = np.concatenate((dataset_no_inj, dataset_inj), axis = 0)
X_train = np.concatenate((model_data[:, 0:1], np.array(pd.get_dummies(model_data[:, 1])), model_data[:, 2:6]), axis=1)
y_train = model_data[:, 6]
X_test = np.concatenate((dataset[:, 0:1], np.array(pd.get_dummies(dataset[:, 1])), dataset[:, 2:6]), axis=1)
y_test = dataset[:, 6]
model = SVC(kernel='rbf', C=0.1, gamma=1)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
## getting 88.83 accuracy consistenly
print('Accuracy: %.2f' % (accuracy*100))
plot_confusion_matrix(model, X_test, y_test, values_format='d', display_labels=["Not Reinjured", "Reinjured"])
plt.show()
