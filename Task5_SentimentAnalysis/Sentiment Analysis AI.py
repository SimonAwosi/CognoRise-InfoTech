import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the IMDb dataset
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

# Print dataset shapes
print(f"x_train shape: {x_train.shape}, y_train shape: {y_train.shape}")
print(f"x_test shape: {x_test.shape}, y_test shape: {y_test.shape}")

# Padding the sequences to ensure they are the same length (maxlen=200)
maxlen = 200
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# Check the shapes after padding
print(f"Shape of x_train after padding: {x_train.shape}")
print(f"Shape of x_test after padding: {x_test.shape}")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Build the model
model = Sequential()

# Embedding layer: Converts word indices to dense vectors
model.add(Embedding(input_dim=10000, output_dim=32, input_length=maxlen))

# LSTM layer with dropout to prevent overfitting
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))

# Dense layer with sigmoid activation for binary classification (positive/negative sentiment)
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Print model summary
model.summary()
# Train the model
history = model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))
# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\nTest accuracy: {test_acc}")
# Save the model to a file
model.save('sentiment_analysis_model.h5')
from tensorflow.keras.models import load_model

# Load the model from the .h5 file
model = load_model('sentiment_analysis_model.h5')

# Display the model architecture
model.summary()
