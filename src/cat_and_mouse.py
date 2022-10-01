def cat_and_mouse(x: int, y: int, z: int) -> str:
    if not ((1 <= x <= 100) and (1 <= y <= 100) and (1 <= z <= 100)):
        return ""

    distance_x_to_z = abs(x-z)
    distance_y_to_z = abs(y-z)

    if distance_x_to_z > distance_y_to_z:
        return 'Cat B'
    elif distance_x_to_z < distance_y_to_z:
        return 'Cat A'
    return 'Mouse C'
