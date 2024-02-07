import pandas as pd
import os

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn import model_selection


class Predictor:
    def __init__(self):
        # Ignores warning that I don't have a GPU ;( #
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        import tensorflow as tf

        data = pd.read_csv("full_filled_stroke_data (1).csv",
                           header=None,
                           delimiter=",")

        data = data.iloc[1:, :]

        data.columns = ["Gender", "Age", "Hypertension",
                        "Heart_Disease", "Ever_Married",
                        "Work_Type", "Residence_Type",
                        "Average_Glucose", "BMI", "Smoking_Status",
                        "Stroke"]

        transformer = make_column_transformer(
            (StandardScaler(), ["Age", "Hypertension", "Heart_Disease", "BMI", "Stroke"]),
            (OneHotEncoder(handle_unknown="ignore"), ["Gender", "Ever_Married", "Work_Type", "Residence_Type"])
        )

        y = data["Average_Glucose"]
        x = data.drop("Average_Glucose", axis=1)

        x = transformer.fit_transform(x)

        y = y.astype(float)

        x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.1)

        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=15, dtype=tf.float32),
            tf.keras.layers.Dense(units=60, activation="gelu"),
            tf.keras.layers.Dense(units=400, activation="gelu"),
            tf.keras.layers.Dense(units=20, activation="gelu"),
            tf.keras.layers.Dense(units=1)
        ])

        self.model.compile(
            loss=tf.losses.mae,
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
            metrics=["mae"]
        )

        self.model.fit(x_train, y_train, epochs=600, verbose=1)

    def predict(self, x_list):
        return self.model.predict(x_list)
