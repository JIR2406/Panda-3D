def cube_collision(
    obj1x,
    obj1y,
    obj1z,
    obj1_width,
    obj1_height,
    obj1_depth,
    obj2x,
    obj2y,
    obj2z,
    obj2_width,
    obj2_height,
    obj2_depth,
):
    # Coordenadas de los lados del cubo 1
    x1_min, x1_max = obj1x - obj1_width / 2, obj1x + obj1_width / 2
    y1_min, y1_max = obj1y - obj1_height / 2, obj1y + obj1_height / 2
    z1_min, z1_max = obj1z - obj1_depth / 2, obj1z + obj1_depth / 2

    # Coordenadas de los lados del cubo 2
    x2_min, x2_max = obj2x - obj2_width / 2, obj2x + obj2_width / 2
    y2_min, y2_max = obj2y - obj2_height / 2, obj2y + obj2_height / 2
    z2_min, z2_max = obj2z - obj2_depth / 2, obj2z + obj2_depth / 2

    # Comprobación de colisión en cada dimensión
    if (x1_min <= x2_max and x1_max >= x2_min) and \
       (y1_min <= y2_max and y1_max >= y2_min) and \
       (z1_min <= z2_max and z1_max >= z2_min):
        return True
    return False
