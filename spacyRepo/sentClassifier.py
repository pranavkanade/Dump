# bidirectional LSTM on sequences of word vectors. with keras

from preprocessor import Dataset, pad_vec_sequences
from sklearn import preprocessing

from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Dense, Dropout, Embeding, LSTM, INput, merge, GRU
from keras.utils import np_utils, generic_utils


# Prepare the dataset

ds = Dataset()

X_all = pad_vec_sequences(ds.X_all_vec_seq)
Y_all = ds.Y_all

xtrain, xtest, ytrain, ytest = cross_validation.train_test_split(X_all,
                                                                 Y_all,
                                                                 test_size=0.2)

ytrain, ytest = [np_utils.to_categorical(x) for x in (ytrain, ytest)]


# model architecture as follows

sequence = Input(shape=(maxlen,300), dtype='float32')
forwards = LSTM(hidden_dim, dropout_W=0.1, dropout_U=0.1)(sequence)
backwards = LSTM(hidden_dim, dropout_W=0.1,
                 dropout_U=0.1, go_backwards=True)(sequence)
merged = merge([forwards, backwards], mode='concat', concat_axis=-1)
after_dp = Dropout(0.1)(merged)
output = Dense(nb_classes, activation='softmax')(after_dp)
model = Model(input=sequence, output=output)

model.compile('adam', 'categorical_crossentropy')

print(model.summary())

model.fit(xtrain, ytrain, batch_size=batch_size,nb_epoch=num_epoch,
          validation_data=[xtest, ytest])

accuracy = model.evaluate(xtest, ytest, verbose=0)
print("\n\n++++++++++++++++++++")
print("Accuracy : %.2f%%" % (accuracy[1]*100))


