import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt


def create_sphere(k):
    # wrapper für devide-triangle
    triangles = []
    # inititalisierung mit dem ursprungs Dreieck, Rekursionstiefe und einer Liste für die berechneten Dreiecke
    devide_triangle(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), k * 2,
                    triangles)  # es entstehen lücken im dreieckt falls die Rekursionstiefe nicht grade ist
    triangles = np.array(triangles)

    masks = [[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1], [1, -1, -1], [-1, -1, 1], [-1, 1, -1],
             [-1, -1, -1]]  # Masken zur
    sphere = []
    for mask in masks:
        for t in triangles:
            tnew = []
            for point in t:
                tnew.append(point * mask)
            sphere.append(tnew)
    return np.array(sphere)


def sort_after_length(triangle):
    # sortiert nach längsten Kanten und gibt die punkte in entsprechender Reihenfolge
    # gibt (a,b,c) zurück mit a-b als längste Kante

    distance = []
    distance.append(np.linalg.norm(triangle[0] - triangle[1]))
    distance.append(np.linalg.norm(triangle[1] - triangle[2]))
    distance.append(np.linalg.norm(triangle[0] - triangle[2]))

    index = distance.index(max(distance))

    if index == 0:
        return triangle[0], triangle[1], triangle[2]

    if index == 1:
        return triangle[2], triangle[1], triangle[0]

    if index == 2:
        return triangle[0], triangle[2], triangle[1]


def devide_triangle(triangle, depth, tlist):
    a, b, c = sort_after_length(triangle)

    # neuer Punkt zwischen a und b
    newPoint = (a - b) / 2 + b

    # Vektor normalisieren
    newPoint = newPoint / np.linalg.norm(newPoint)

    # aus den 4 Puntkten 2 neue Dreiecke erstellen
    triangleA = np.array([c, b, newPoint])
    triangleB = np.array([c, a, newPoint])

    depth -= 1
    if depth == 0:
        # Dreiecke in eine Liste schreiben
        tlist.append(triangleA)
        tlist.append(triangleB)
        return
    else:
        # Rekursiv anwenden
        devide_triangle(triangleA, depth, tlist)
        devide_triangle(triangleB, depth, tlist)


def plot_triangles(array):
    # Einfache grafische darstellung
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.add_collection3d(Poly3DCollection(array, facecolors="black", linewidths=0.1, edgecolors="green"))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    ax.view_init(20, 30)
    plt.show()


def write_obj(array):
    # erstellt OBJ datei aus array von Dreiecken
    verteces = ""
    faces = ""

    vcount = 1
    for triangle in array:
        faces += "\nf "
        for points in triangle:
            verteces += "v {:.6f} {:.6f} {:.6f}\n".format(points[0], points[1], points[2])
            faces += " " + str(vcount)
            vcount += 1

    f = open("out.obj", "w+")
    f.write(verteces)
    f.write("#---------------------------------------")
    f.write(faces)
    f.close()


if __name__ == '__main__':
    array = create_sphere(3)
    write_obj(array)
