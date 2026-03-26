import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("energy_model.h5")

# Example prediction
sample = np.array([[12, 34, 11]])  # hour, temperature, appliances

prediction = model.predict(sample)

print("Predicted Energy Consumption:", prediction[0][0])
