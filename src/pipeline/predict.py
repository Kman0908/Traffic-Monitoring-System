import os
from src.utils.helper import count
from src.components.detector import Detect

def run(folder_path):
    detector = Detect()

    for file in os.listdir(folder_path):
        if file.endswith((".jpg", ".png", ".mp4")):
            path = os.path.join(folder_path, file)

            result = detector.predict(path)
            count_vehicles = count(result)

            print(f'{file}, Vehicle count: {count_vehicles}')
            result[0].save(filename = f'data/processed/{file}')