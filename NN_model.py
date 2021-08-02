from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot
import PCA

dataset = loadtxt('simple_combined_data.csv', delimiter=',')
# number of inputs to be reduced to after PCA
inputs = 4

X = PCA.pca(inputs)
y = dataset[:, 6]
# define model
model = Sequential()
model.add(Dense(12, input_dim=inputs, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile model
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])
# fit model on dataset
history = model.fit(X, y, epochs=40, batch_size=10)
# evaluate  model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# plot model
pyplot.title('Loss Over Epochs with ' + str(inputs)+'-Feature PCA')
pyplot.plot(history.history['loss'], label='train')
pyplot.show()
