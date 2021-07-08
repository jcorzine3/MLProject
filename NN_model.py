# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot

# load the dataset
dataset = loadtxt('simple_combined_data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:, 0:6]
y = dataset[:, 6]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=6, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
history = model.fit(X, y, epochs=40, batch_size=10)
# evaluate the keras model  
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

pyplot.title('Loss Over Epochs')
pyplot.plot(history.history['loss'], label='train')
