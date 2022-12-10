from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn import preprocessing
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras import callbacks

#Read data from CSV file
myDataLabels = pd.read_csv("mega_output.csv", sep=',')

#Convert to numpy array
myData = np.array( myDataLabels )

#Remove timestamp data
myData = np.delete(myData, 0, 1)

means = np.zeros((1,53))
stds = np.zeros((1,53))

means = np.mean(myData, axis=0)
stds = np.std(myData, axis=0)

np.save("means.npy", means)
np.save("stds.npy", stds)

#Normalize the data
scaler = preprocessing.StandardScaler().fit(myData)
myData = scaler.transform(myData)

#Take every 50th datapoint
finalData = np.zeros((1176,53))
x = 0
for i in range(58799):
  if (i + 1) % 50 == 0:
    finalData[x,0:2] = myData[i+1,0:2]
    finalData[x,3:53] = myData[i,3:53]
    x = x + 1

noise = np.random.normal(1, 0.3, (1176,53))

noisyData = finalData * noise

multiModelData = np.zeros((1176,53,10))

multiModelData[:,:,0] = finalData[:,:] #All data

multiModelData[:,0:11,1] = finalData[:,[0,1,2,37,39,43,38,40,44,47,48]] #attacker rates, packet drop rates, flow table sizes, bandwidth utilization

multiModelData[:,0:6,2] = finalData[:,[0,1,2,37,39,43]] #attacker rates and packet drop rates

multiModelData[:,0:6,3] = finalData[:,[0,1,2,38,40,44]] #attacker rates and flow table sizes

multiModelData[:,0:5,4] = finalData[:,[0,1,2,47,48]] #attacker rates and bandwidth utilization

multiModelData[:,:,5] = noisyData[:,:] #All data

multiModelData[:,0:11,6] = noisyData[:,[0,1,2,37,39,43,38,40,44,47,48]] #attacker rates, packet drop rates, flow table sizes, bandwidth utilization

multiModelData[:,0:6,7] = noisyData[:,[0,1,2,37,39,43]] #attacker rates and packet drop rates

multiModelData[:,0:6,8] = noisyData[:,[0,1,2,38,40,44]] #attacker rates and flow table sizes

multiModelData[:,0:5,9] = noisyData[:,[0,1,2,47,48]] #attacker rates and bandwidth utilization

multiModelSize = np.array([53,11,6,6,5,53,11,6,6,5])

multiModelLoss = np.zeros(10)

fig, axs = plt.subplots(2)

for modelIndex in range(10):
  #Set 80% of data for training, 20% for testing
  trainData = multiModelData[0:941,:,modelIndex]
  testData = multiModelData[941:1175,:,modelIndex]

  #Split into data and labels
  trainX = trainData[:,0:multiModelSize[modelIndex]]
  trainY = np.zeros((941,10))

  #Export labels for training data
  for i in range(10):
    trainY[:,i] = finalData[0:941,27+2*i]
    
  #Repeat above for test data
  testX = testData[:,0:multiModelSize[modelIndex]]
  testY = np.zeros((234,10))

  for i in range(10):
    testY[:,i] = finalData[941:1175,27+2*i]

  def baseline_model():
    #create model
    model = keras.Sequential([
      layers.Dense(20, input_dim=multiModelSize[modelIndex], activation='relu'),
      layers.Dropout(0.15),
      layers.Dense(20, activation = 'relu'),
      layers.Dropout(0.15),
      layers.Dense(20, activation = 'relu'),
      layers.Dropout(0.15),
      layers.Dense(10)
    ])
    #Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

  #fit model and graph training loss per epoch
  MLP = KerasRegressor(build_fn=baseline_model, epochs=50, batch_size=5, validation_split=0.2)

  estop = callbacks.EarlyStopping(monitor ="val_loss", 
                                          mode ="min", patience = 5, 
                                          restore_best_weights = True)

  history = MLP.fit(trainX, trainY, callbacks =[estop])

  preds = MLP.predict(testX)
  test_error = np.abs(testY - preds)
  mean = np.mean(test_error)
  std = np.std(test_error)

  print("mean: ", mean)
  print("std: ", std)

  multiModelLoss[modelIndex] = mean

  if modelIndex == 0:
    axs[0].plot(history.history['loss'], label='loss1')
    axs[0].plot(history.history['val_loss'], label='val_loss1')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'orange')
    MLP.model.save("model1.h5")
  elif modelIndex == 1:
    axs[0].plot(history.history['loss'], label='loss2')
    axs[0].plot(history.history['val_loss'], label='val_loss2')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'red')
    MLP.model.save("model2.h5")
  elif modelIndex == 2:
    axs[0].plot(history.history['loss'], label='loss3')
    axs[0].plot(history.history['val_loss'], label='val_loss3')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'saddlebrown')
    MLP.model.save("model3.h5")
  elif modelIndex == 3:
    axs[0].plot(history.history['loss'], label='loss4')
    axs[0].plot(history.history['val_loss'], label='val_loss4')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'darkgray')
    MLP.model.save("model4.h5")
  elif modelIndex == 4:
    axs[0].plot(history.history['loss'], label='loss5')
    axs[0].plot(history.history['val_loss'], label='val_loss5')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'cyan')
    MLP.model.save("model5.h5")
  elif modelIndex == 5:
    axs[0].plot(history.history['loss'], label='loss6')
    axs[0].plot(history.history['val_loss'], label='val_loss6')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'b')
    MLP.model.save("model6.h5")
  elif modelIndex == 6:
    axs[0].plot(history.history['loss'], label='loss7')
    axs[0].plot(history.history['val_loss'], label='val_loss7')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'g')
    MLP.model.save("model7.h5")
  elif modelIndex == 7:
    axs[0].plot(history.history['loss'], label='loss8')
    axs[0].plot(history.history['val_loss'], label='val_loss8')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'black')
    MLP.model.save("model8.h5")
  elif modelIndex == 8:
    axs[0].plot(history.history['loss'], label='loss9')
    axs[0].plot(history.history['val_loss'], label='val_loss9')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'deeppink')
    MLP.model.save("model9.h5")
  elif modelIndex == 9:
    axs[0].plot(history.history['loss'], label='loss10')
    axs[0].plot(history.history['val_loss'], label='val_loss10')
    axs[0].scatter([estop.stopped_epoch],[mean], c = 'lime')
    MLP.model.save("model10.h5")


axs[1].scatter([1,2,3,4,5], multiModelLoss[0:5], c='blue')
axs[1].scatter([1,2,3,4,5], multiModelLoss[5:10], c='red')