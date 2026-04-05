def count(results):
    vehicle_classes = ['car', 'truck', 'bus', 'motorcycle']

    count = 0

    for r in results:
        if r.boxes is None:
            continue

        for box in r.boxes:
            cls_id = int(box.cls.item())   # safer
            label = r.names[cls_id]

            if label in vehicle_classes:
                count += 1

    return count