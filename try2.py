def calculate_volume_or_missing_card(cards):
    xy_planes = {}
    xz_planes = {}
    yz_planes = {}
    min_x = min_y = min_z = float('inf')
    max_x = max_y = max_z = float('-inf')
    for card in cards:
        x, y, z, plane = card
        if plane == 'xy':
            xy_planes[(x, y, z)] = True
            min_z = min(min_z, z)
            max_z = max(max_z, z)
        elif plane == 'xz':
            xz_planes[(x, y, z)] = True
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        elif plane == 'yz':
            yz_planes[(x, y, z)] = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
    volume = (max_x - min_x) * (max_y - min_y) * (max_z - min_z)
    missing_faces = set()
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if (x, y, min_z) not in xy_planes:
                missing_faces.add((x, y, min_z, 'xy'))
            if (x, y, max_z) not in xy_planes:
                missing_faces.add((x, y, max_z, 'xy'))
    for x in range(min_x, max_x):
        for z in range(min_z, max_z):
            if (x, min_y, z) not in xz_planes:
                missing_faces.add((x, min_y, z, 'xz'))
            if (x, max_y, z) not in xz_planes:
                missing_faces.add((x, max_y, z, 'xz'))
    for y in range(min_y, max_y):
        for z in range(min_z, max_z):
            if (min_x, y, z) not in yz_planes:
                missing_faces.add((min_x, y, z, 'yz'))
            if (max_x, y, z) not in yz_planes:
                missing_faces.add((max_x, y, z, 'yz'))
    if not missing_faces:
        return volume
    elif len(missing_faces) == 1:
        missing_face = missing_faces.pop()
        return f"{missing_face[0]} {missing_face[1]} {missing_face[2]} {missing_face[3]}"
    else:
        return "Error: More than one missing card"

n = int(input().strip())
cards = []
for _ in range(n):
    x, y, z, plane = input().strip().split()
    x, y, z = int(x), int(y), int(z)
    cards.append((x, y, z, plane))
result = calculate_volume_or_missing_card(cards)
print(result)
