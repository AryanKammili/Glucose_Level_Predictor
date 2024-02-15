import pandas as pd
import numpy as np
import os

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn import model_selection


class Predictor:
    def __init__(self):
        # Ignores warning that I don't have a GPU ;( #
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        import tensorflow as tf

        self.data = pd.read_csv("full_filled_stroke_data (1).csv",
                                header=None,
                                delimiter=",")

        self.data = self.data.iloc[1:, :]

        self.data.columns = ["Gender", "Age", "Hypertension",
                             "Heart_Disease", "Ever_Married",
                             "Work_Type", "Residence_Type",
                             "Average_Glucose", "BMI", "Smoking_Status",
                             "Stroke"]

        self.transformer = make_column_transformer(
            (StandardScaler(), ["Age", "BMI"]),
            (OneHotEncoder(handle_unknown="ignore"), ["Gender", "Hypertension", "Heart_Disease", "Ever_Married", "Work_Type", "Residence_Type", "Stroke"]))

        y = self.data["Average_Glucose"]
        x = self.data.drop(["Average_Glucose", "Smoking_Status"], axis=1)

        x = self.transformer.fit_transform(x)

        y = y.astype(float)

        x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.1)

        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=18, dtype=tf.float32),
            tf.keras.layers.Dense(units=60, activation="gelu"),
            tf.keras.layers.Dense(units=40, activation="gelu"),
            tf.keras.layers.Dense(units=20, activation="gelu"),
            tf.keras.layers.Dense(units=1)
        ])

        self.model.compile(
            loss=tf.losses.mae,
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
            metrics=["mae"]
        )

        self.model.fit(x_train, y_train, epochs=400, verbose=0)

    def predict(self, vals):
        x_list = np.array(vals).reshape(1, 9)

        reshaped = pd.DataFrame(x_list, columns=["Gender", "Age", "Hypertension",
                                       "Heart_Disease", "Ever_Married",
                                       "Work_Type", "Residence_Type",
                                       "BMI", "Stroke"])

        final = self.transformer.transform(reshaped)

        return self.model.predict(final)
