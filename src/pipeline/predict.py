from src.utils.helper import count
from src.components.detector import Detect

def run(image_path):
    detector = Detect()
    results = detector.predict(image_path)

    vehicle_count = count(results)
    print(f'Vehicle count: {vehicle_count}')

    results[0].save(filename = 'data/processed/output.jpg')