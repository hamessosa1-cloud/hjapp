import numpy as np
import tensorflow as tf
import joblib # Para cargar el scaler si lo guardaste

class IrisModelManager:
    def __init__(self, model_path='modelo_iris.h5'):
        # Cargamos el modelo entrenado
        self.model = tf.keras.models.load_model(model_path)
        # Mapeo de salida según el orden del LabelEncoder
        self.classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        
    def predict(self, features):
        """
        features: lista [sepal_length, sepal_width, petal_length, petal_width]
        """
        # Convertir a array de numpy y dar forma (1, 4)
        input_data = np.array([features])
        
        # IMPORTANTE: Aquí deberías aplicar el mismo StandardScaler 
        # que usaste en el entrenamiento. 
        # input_scaled = self.scaler.transform(input_data)
        
        prediction = self.model.predict(input_data)
        class_idx = np.argmax(prediction)
        
        return {
            "species": self.classes[class_idx],
            "confidence": float(np.max(prediction))
        }