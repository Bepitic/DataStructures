# -*- coding: utf-8 -*-

##Geometrical Algorithm Project
# Team
# Silva Castellanos Oscar Arturo
# Amoros Cubells Francisco de Asís
# Likaj Shega
# Code based in 


import numpy as np
import math as m
from math import sqrt, pow
import networkx as nx
import matplotlib.pyplot as plt
import time


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.points = [x, y]
        self.x = x
        self.y = y
        self.hedges = []  # list of half edges whose tail is this vertex

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __repr__(self):
        return "({0})".format(self.name)


class Hedge:
    # v1 -> v2
    def __init__(self, v1, v2):
        self.prev = None
        self.twin = None
        self.next = None
        self.tail = v1
        self.face = None
        self.is_vHedge = False
        self.is_Infinite = False

    def __eq__(self, other):
        return self.tail == other.tail and \
               self.next.tail == other.next.tail

    def __repr__(self):
        if self.next is not None:
            return "({0})->({1})".format(self.tail.name, self.next.tail.name)

            # return "({0},{1})->({2},{3})".format(self.tail.x, self.tail.y,
            #                                    self.next.tail.x,
            #                                    self.next.tail.y)
        else:
            # return "({0},{1})->()".format(self.tail.x, self.tail.y)
            return "({0})->()".format(self.tail.name)


class Face:
    def __init__(self, he, name):
        self.halfEdge = he
        self.name = name
        self.v_vertex = None


class Delaunay_DCEL:

    #def check(self,n = ""):
    #    print(n)
    #    for he in self.h_edges:
    #        if(he.tail == he.twin.tail):
    #            raise Exception("Sorry")
    def show(self):
        DCEL = self
        print("============================= ")
        print("Half  Edges")
        for e in DCEL.h_edges:
            print("Edge {0}, Tail {1}, Next {2}, Prev {3})".format(e, e.tail, e.next, e.prev))
            #print("Twin {0}, Tail {1}, Next {2}, Prev {3})".format(e.twin, e.twin.tail, e.twin.next, e.twin.prev))
        print(" ")
        print("Faces")
        for e in DCEL.faces:
            print("Name: {} ".format(e.name))
            print("Half edges: {}, {}, {}".format(e.halfEdge, e.halfEdge.next, e.halfEdge.next.next))
            # print(e.halfEdge)
            # print(e.halfEdge.next)
            # print(e.halfEdge.next.next)
            # print(e.halfEdge.next.next.next)
            print(" ")
        print("Vertices")
        for key, value in DCEL.vertices.items():
            print(key, '->', value.hedges)
            # print(key, '-> twin ->', value.hedges.twin)
        print(" ============================== ")

    def show_voronoi(self):
        DCEL = self
        print("============================= ")
        print("Edges ")
        for e in DCEL.v_hedges:
            print("Edge {0}, Tail {1}, Next {2}, Prev {3})".format(e, e.tail, e.next, e.prev))
            #print("Twin {0}, Tail {1}, Next {2}, Prev {3})".format(e.twin, e.twin.tail, e.twin.next, e.twin.prev))
        print(" ")
        print("Vertices")
        for value in DCEL.v_vertices:
            print(value)
            # print(key, '-> twin ->', value.hedges.twin)
        print("============================== ")

    def __init__(self, v1, v2, v3):
        self.vertices = {}
        self.h_edges = []
        self.faces = []
        self.v_vertices = []
        self.v_hedges = []
        # Add the vertices to the list.
        self.vertices[v1.name] = v1
        self.vertices[v2.name] = v2
        self.vertices[v3.name] = v3

        # Create the Hedges (of the triangle) and add to their respective list.
        self.h_edges.append(Hedge(v1, v2))
        self.vertices[v1.name].hedges.append(self.h_edges[-1])
        self.h_edges.append(Hedge(v2, v3))
        self.vertices[v2.name].hedges.append(self.h_edges[-1])
        self.h_edges.append(Hedge(v3, v1))
        self.vertices[v3.name].hedges.append(self.h_edges[-1])
        # Link the edges with eachother
        self.h_edges[0].prev = self.h_edges[2]
        self.h_edges[1].prev = self.h_edges[0]
        self.h_edges[2].prev = self.h_edges[1]
        # the other way
        self.h_edges[0].next = self.h_edges[1]
        self.h_edges[1].next = self.h_edges[2]
        self.h_edges[2].next = self.h_edges[0]
        # add the face
        self.faces.append(Face(self.h_edges[0], str(len(self.faces))))
        self.h_edges[0].face = self.faces[-1]
        self.h_edges[0].next.face = self.faces[-1]
        self.h_edges[0].next.next.face = self.faces[-1]
        # Now the twins

        self.h_edges.append(Hedge(v2, v1))

        self.vertices[v2.name].hedges.append(self.h_edges[-1])
        self.h_edges[0].twin = self.h_edges[-1]
        self.h_edges[-1].twin = self.h_edges[0]

        self.h_edges.append(Hedge(v3, v2))
        self.vertices[v3.name].hedges.append(self.h_edges[-1])
        self.h_edges[1].twin = self.h_edges[-1]
        self.h_edges[-1].twin = self.h_edges[1]
        self.h_edges.append(Hedge(v1, v3))
        self.vertices[v1.name].hedges.append(self.h_edges[-1])
        self.h_edges[2].twin = self.h_edges[-1]
        self.h_edges[-1].twin = self.h_edges[2]

        # fit the twins and the next/prev
        self.h_edges[0].twin.next = self.h_edges[0].prev.twin
        self.h_edges[0].next.twin.next = self.h_edges[0].next.prev.twin
        self.h_edges[0].next.next.twin.next = self.h_edges[0].next.next.prev.twin

        self.h_edges[0].twin.prev = self.h_edges[0].next.twin
        self.h_edges[0].prev.twin.prev = self.h_edges[0].prev.next.twin
        self.h_edges[0].prev.prev.twin.prev = self.h_edges[0].prev.prev.next.twin

    def add_point(self, v1, v_prev, v_next):

        self.vertices[v1.name] = v1

        num_new = self.vertices[v1.name]
        num_pev = self.vertices[v_prev.name]
        num_after = self.vertices[v_next.name]

        ## need to obtain all the parts before we start changing

        # search the link that is in between this 2 vertices
        #print(v1.name,v_prev.name,v_next.name)

        #for e in self.h_edges:
        #    print("Edge {0}, Tail {1}, Next {2}, Prev {3})".format(e, e.tail, e.next, e.prev))

        for edge in num_after.hedges:
            if edge.twin.tail == num_pev:
                found_e = edge
        h_e_previous = found_e.prev
        h_e_after = found_e.next

        ## conecting everything

        # add the 2 links
        # and append to the vertex

        self.h_edges.append(Hedge(num_pev, num_new))

        self.vertices[num_pev.name].hedges.append(self.h_edges[-1])
        found_e.next = self.h_edges[-1]
        self.h_edges[-1].prev = found_e

        self.h_edges.append(Hedge(num_new, num_after))
        self.vertices[num_new.name].hedges.append(self.h_edges[-1])

        self.h_edges[-2].next = self.h_edges[-1]
        self.h_edges[-1].prev = self.h_edges[-2]

        self.h_edges[-1].next = found_e

        # add the face
        self.faces.append(Face(found_e, len(self.faces)))
        found_e.face = self.faces[-1]
        found_e.next.face = self.faces[-1]
        found_e.next.next.face = self.faces[-1]

        # their twins

        self.h_edges.append(Hedge(num_after, num_new))
        self.vertices[num_after.name].hedges.append(self.h_edges[-1])
        h_e_previous.next = self.h_edges[-1]
        self.h_edges[-1].prev = h_e_previous  # kindly checked

        self.h_edges.append(Hedge(num_new, num_pev))
        self.vertices[num_new.name].hedges.append(self.h_edges[-1])

        self.h_edges[-2].next = self.h_edges[-1]
        self.h_edges[-1].prev = self.h_edges[-2]

        self.h_edges[-1].next = h_e_after
        h_e_after.prev = self.h_edges[-1]

        ## make the twin conections
        found_e.next.twin = h_e_after.prev
        h_e_after.prev.twin = found_e.next
        found_e.next.next.twin = h_e_after.prev.prev
        h_e_after.prev.prev.twin = found_e.next.next

        self.test_edge(v1, v_prev, v_next)

    def center_circle(self, v1, v2, v3):
        A = (v1.x, v1.y)
        B = (v2.x, v2.y)
        C = (v3.x, v3.y)

        (x1, y1), (x2, y2), (x3, y3) = A, B, C
        A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
        B = (x1 ** 2 + y1 ** 2) * (y3 - y2) + (x2 ** 2 + y2 ** 2) * (y1 - y3) + (x3 ** 2 + y3 ** 2) * (y2 - y1)
        C = (x1 ** 2 + y1 ** 2) * (x2 - x3) + (x2 ** 2 + y2 ** 2) * (x3 - x1) + (x3 ** 2 + y3 ** 2) * (x1 - x2)

        return (-B / A / 2, -C / A / 2)

    def inCircle(self, a, b, c, d):
        matrix = [
            [a.points[0], a.points[1], a.points[0] ** 2 + a.points[1] ** 2, 1],
            [b.points[0], b.points[1], b.points[0] ** 2 + b.points[1] ** 2, 1],
            [c.points[0], c.points[1], c.points[0] ** 2 + c.points[1] ** 2, 1],
            [d.points[0], d.points[1], d.points[0] ** 2 + d.points[1] ** 2, 1]
        ]
        n_array = np.array(matrix)
        det = np.linalg.det(n_array)

        if det < 0:
            return -1  # outside the circle
        elif det > 0:
            return 1  # inside the circle
        else:
            return 0  # in the circle

    def swap_edge(self, v_1, v_2, v_3, v_4):
        #print()
        # points in counterclockwise hull of 2 triangles
        # usually is from v1 to v3
        # and we need to change it to v2 - v4
        # recheck this part***
        #print("swapping dawg", v_1.name, v_2.name,v_3.name , v_4.name)
        #self.check("1")
        vertex_1 = self.vertices[v_1.name]
        vertex_2 = self.vertices[v_2.name]
        vertex_3 = self.vertices[v_3.name]
        vertex_4 = self.vertices[v_4.name]
        #self.check("2")
        for edge in vertex_1.hedges:
            if edge.twin.tail == vertex_3:
                found_e = edge
        #print("found_e => ",found_e)
        #self.check("3")
        face_1 = found_e.face
        #self.check("4")
        face_2 = found_e.twin.face
        # TODO: remove the face from the faces list
        # Add the outer face to the edges
        if (face_1):
            self.faces.remove(face_1)
        if (face_2):
            self.faces.remove(face_2)
        #self.check("5")
        # self.show()

        # TODO: remove the edges
        # Fixing next and previous of v1
        #print("found_e.prev.next = found_e.twin.next",found_e.twin.next)
        found_e.prev.next = found_e.twin.next
        #self.check("6")
        #print("found_e.twin.next.prev = found_e.prev", found_e.prev)
        found_e.twin.next.prev = found_e.prev
        #self.check("7")
        # Fixing next and previous of v3
        for edge in vertex_1.hedges:
            if edge.twin.tail == vertex_2:
                e_12 = edge

        for edge in vertex_2.hedges:
            if edge.twin.tail == vertex_3:
                e_23 = edge

        for edge in vertex_3.hedges:
            if edge.twin.tail == vertex_4:
                e_34 = edge
        #self.check("8")

        for edge in vertex_4.hedges:
            if edge.twin.tail == vertex_1:
                e_41 = edge
        #self.check("9")


        e_23.next = e_34
        e_34.prev = e_23

        e_12.prev = e_41
        e_41.next = e_12
        #e_41 = e_34.next
        #e_12 = e_41.next
        #self.check("10")
        #e_12.face = None
        #e_23.face = None
        #e_34.face = None
        #e_41.face = None
        # TODO: remove the edge from the vertex list
        found_e.tail.hedges.remove(found_e)
        found_e.twin.tail.hedges.remove(found_e.twin)
        #self.check("11")
        # TODO: remove the edge from the list of edges
        self.h_edges.remove(found_e)
        self.h_edges.remove(found_e.twin)
        #self.check("12")
        # check
        #self.show()
        # TODO: add the edge
        e = Hedge(vertex_4, vertex_2)
        self.h_edges.append(e)
        # TODO: add the edge to the list of edges of the vertices
        self.vertices[vertex_4.name].hedges.append(e)
        #self.show()

        #self.check("13")

        #e = self.h_edges[-1]
        #self.check("14")
        #self.show()
        print(vertex_2.name, vertex_2.x)

        print(vertex_4.name, vertex_4.x)
        # Add the other edge
        e1 = Hedge(vertex_2, vertex_4)
        self.h_edges.append(e1)
        # TODO: add the edge to the list of edges of the vertices


        self.vertices[vertex_2.name].hedges.append(e1)
        #e1 = self.h_edges[-1]
        e1.twin = e
        e.twin = e1

        #self.show()

        # self.check("15")

        e.prev = e_34
        e_34.next = e
        e.next = e_23
        e_23.prev = e

        #self.show()
        #self.check("16")

        e1.prev = e_12
        e_12.next = e1
        e1.next = e_41
        e_41.prev = e1
        #self.check("17")

        # add the face
        self.faces.append(Face(e1, len(self.faces)))
        e1.face = self.faces[-1]
        e1.next.face = self.faces[-1]
        e1.next.next.face = self.faces[-1]

        self.faces.append(Face(e, len(self.faces)))
        e.face = self.faces[-1]
        e.next.face = self.faces[-1]
        e.next.next.face = self.faces[-1]

    def test_edge(self, v_new, v_prev, v_after):

        vertex_new = self.vertices[v_new.name]
        vertex_prev = self.vertices[v_prev.name]
        vertex_post = self.vertices[v_after.name]

        for edge in vertex_post.hedges:
            if edge.twin.tail == vertex_prev:
                found_e = edge

       #If we are traversing the outer face we got out
        if found_e.twin.face == None:
            return

        vertex_4 = found_e.twin.next.next.tail
        #print("Incircletest",v_prev.name,v_after.name,vertex_4.name,v_new.name)

        if (self.inCircle(v_prev, v_after, vertex_4, v_new) > 0):
            self.swap_edge(v_prev, v_new, v_after, vertex_4)
            self.test_edge(v_new, vertex_4, v_after)
            self.test_edge(v_new, v_prev, vertex_4)

    def output_voronoi(self):
        # get the boundaries
        # min_x = self.hedges.x
        # for i in self.hedges

        for f in self.faces:
            v1 = f.halfEdge.tail
            v2 = f.halfEdge.next.tail
            v3 = f.halfEdge.next.next.tail
            # Test
            print(f.halfEdge)
            f.halfEdge.face = f
            print(f.halfEdge.next)
            f.halfEdge.next.face = f
            print(f.halfEdge.next.next)
            f.halfEdge.next.next.face = f
            #
            x, y = self.center_circle(v1, v2, v3)
            f.v_vertex = Vertex(len(self.v_vertices), x, y)
            self.v_vertices.append(f.v_vertex)
            pass



        # TODO : Delete me
        for f in self.faces:
            pass
            #self.create_voronoi_edges(f.halfEdge)
            #self.create_voronoi_edges(f.halfEdge.next)
            #self.create_voronoi_edges(f.halfEdge.next.next)

        for h in self.h_edges:
            pass
            #print(h)
            self.create_voronoi_edges(h)

    def create_voronoi_edges(self, h):
        if (not h.is_vHedge and h.face and h.twin.face):
            v_orig = h.face.v_vertex
            v_end = h.twin.face.v_vertex
            edge1 = Hedge(v_orig, v_end)
            edge2 = Hedge(v_end, v_orig)
            edge1.twin = edge2
            edge2.twin = edge1
            self.v_hedges.append(edge1)
            self.v_hedges.append(edge2)
            h.face.v_vertex.is_vHedge = True
            h.twin.face.v_vertex.is_vHedge = True

        if (not h.is_vHedge and not h.twin.face and h.face):
            v_orig = h.face.v_vertex
            v1 = h.tail
            v2 = h.twin.tail

            dist = 0

            if (abs(v_orig.x - v1.x) > abs(v_orig.x - v2.x)):
                dist = v1.x - v_orig.x
            else:
                dist = v2.x - v_orig.x

            dist = dist * 2

            new_slope = -1 * ((v1.x - v2.x) / (v1.y - v2.y))

            x = v_orig.x + dist

            y = new_slope * (x - v_orig.x) + v_orig.y

            intinite = Vertex(len(self.v_vertices), x, y)
            self.v_vertices.append(intinite)

            ed1 = Hedge(v_orig, intinite)
            ed2 = Hedge(intinite, v_orig)
            ed1.is_Infinite = True
            ed2.is_Infinite = True

            ed1.twin = ed2
            ed2.twin = ed1
            self.v_hedges.append(ed1)
            self.v_hedges.append(ed2)


# After a while the colab deletes the files in /content folder, Reupload if needed.


def inCircle(a, b, c, d):
    matrix = [
        [a[0], a[1], a[0] ** 2 + a[1] ** 2, 1],
        [b[0], b[1], b[0] ** 2 + b[1] ** 2, 1],
        [c[0], c[1], c[0] ** 2 + c[1] ** 2, 1],
        [d[0], d[1], d[0] ** 2 + d[1] ** 2, 1]
    ]
    n_array = np.array(matrix)
    det = np.linalg.det(n_array)

    if det < 0:
        return -1  # outside the circle
    elif det > 0:
        return 1  # inside the circle
    else:
        return 0  # in the circle


def read_convex_hull_points():
    with open("ExampleInput.txt", "r") as file_of_convex_hull:
        FileContent = file_of_convex_hull.read().split("\n")

    convex_hull_points = {}
    convex_hull_points_rep = []

    for key, value in enumerate(FileContent):
        point = value.split(" ")
        convex_hull_points.update({chr(65 + key): [float(point[0]), float(point[1])]})
        convex_hull_points_rep.append(chr(65 + key))
        file_of_convex_hull.close()
    return convex_hull_points, convex_hull_points_rep


def remove_vertex_from_convex_hull(convex_hull_points_rep):
    permutation = np.random.permutation(convex_hull_points_rep)
    list_permutation = permutation.tolist()
    delete_history_of_points = []
    while len(list_permutation) > 3:
        # Get the point
        point = list_permutation.pop(0)

        # point = convex_hull_points.get(index_point)
        point_index = convex_hull_points_rep.index(point)
        if convex_hull_points_rep.index(point) == 0:
            left_neighbor_point = convex_hull_points_rep[len(convex_hull_points_rep) - 1]
            right_neighbor_point = convex_hull_points_rep[point_index + 1]
        elif convex_hull_points_rep.index(point) == len(convex_hull_points_rep) - 1:
            left_neighbor_point = convex_hull_points_rep[len(convex_hull_points_rep) - 2]
            right_neighbor_point = convex_hull_points_rep[0]
        else:
            left_neighbor_point = convex_hull_points_rep[point_index - 1]
            right_neighbor_point = convex_hull_points_rep[point_index + 1]

        # # delete the point from convex_hull
        # # after we calucate the neighors and delete we point we pop also from the convex full.
        # print(convex_hull_points[index_point])
        delete_history_of_points.append([point, [left_neighbor_point, right_neighbor_point]])
        # delete_history_of_points.append([left_neighbor_point, point, right_neighbor_point])
        convex_hull_points_rep.remove(point)

    return convex_hull_points_rep, delete_history_of_points


## Creating Delaunay Graph

# Reading the input file and creating a dictionary of the points and their position.
convex_hull_points, convex_hull_points_rep = read_convex_hull_points()
all_x = []
all_y = []

# We  obtain a rectangle with max positions of x and y this is just for getting the box were will
# output the graphs
for _, value in convex_hull_points.items():
    all_x.append(value[0])
    all_y.append(value[1])

x_min = min(all_x) - 0.1
x_max = max(all_x) + 0.1
y_min = min(all_y) - 0.1
y_max = max(all_y) + 0.1

# We remove one vertex at a time of the convex hull , every time we remove a vertex we store
# its neighbours at the time of removal until we only have 3 points or one triangle

start_time = time.process_time()
convex_hull_points_rep, delete_history_of_points = remove_vertex_from_convex_hull(convex_hull_points_rep)
delete_history_of_points = [['B', ['A', 'C']], ['G', ['F', 'A']], ['C', ['A', 'D']], ['F', ['E', 'A']]]
convex_hull_points_rep = ['A', 'D', 'E']
print("Convex hull points: {}".format(convex_hull_points))
print("Delete history of points: {}".format(delete_history_of_points))
print("Starting triangle: {}".format(convex_hull_points_rep))



a = convex_hull_points_rep[0]
b = convex_hull_points_rep[1]
c = convex_hull_points_rep[2]
a_point = convex_hull_points.get(a)
b_point = convex_hull_points.get(b)
c_point = convex_hull_points.get(c)

# Storing our first triangle in the DCEL
DCEL = Delaunay_DCEL(Vertex(a, a_point[0], a_point[1]), Vertex(b, b_point[0], b_point[1]),
                     Vertex(c, c_point[0], c_point[1]))


# We add every vertex we removed in the reverse order, and do the in circle test to validate
# Delauney triangulation conditions

for key, value in enumerate(delete_history_of_points):

    # Obtaining the last vertex removed
    next_vertex_history = delete_history_of_points[len(delete_history_of_points) - 1 - key]
    vertex_coordinate = convex_hull_points.get(next_vertex_history[0])

    # Retrieving coordinates of the neighbours
    first_neighbour_coordinate = convex_hull_points.get(next_vertex_history[1][0])
    second_neighbour_coordinate = convex_hull_points.get(next_vertex_history[1][1])

    # Adding the removed vertex to the DCEL. The edge will be tested if it does not comply with the in circle test
    # the edge will be flipped
    #print(next_vertex_history[0])
    DCEL.add_point(Vertex(next_vertex_history[0], vertex_coordinate[0], vertex_coordinate[1]),
                   Vertex(next_vertex_history[1][0], first_neighbour_coordinate[0], first_neighbour_coordinate[1]),
                   Vertex(next_vertex_history[1][1], second_neighbour_coordinate[0], second_neighbour_coordinate[1]))


print("{:.4e}".format(time.process_time() - start_time), "Delauney Triangulation Running time")

#Creating Voronoi Diagram

start_time = time.process_time()
DCEL.show()
#Once the Delauney Graph it's stored on the DCEL the class has function implemented to compute the Voronoi Diagram
DCEL.output_voronoi()
print("{:.5e}".format(time.process_time() - start_time), "Voronoi Diagram Running time")


print("=============================")
print("Delauney Triangulation")
DCEL.show()
print("=============================")

print("=============================")
print("Voronoi Diagram")
DCEL.show_voronoi()
print("=============================")



# for i in DCEL.v_hedges:
#     print(i.tail.name)
#     print(i.tail.x, i.tail.y)
#     print(i.twin.tail.x, i.twin.tail.y)
#
#     # print(dir(i))
#     # print(i.tail, i.twin.tail)
#
# print(DCEL.v_hedges)


# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []
        self.nodes = []
        self.pose = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def addNode(self, ver, pose1, pose2):
        temp = ver
        temp2 = [pose1, pose2]

        self.nodes.append(temp)
        self.pose.append(temp2)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.DiGraph()
        for i, a in enumerate(self.nodes):
            #print(i, a, (self.pose[i]))
            G.add_node(a, pos=self.pose[i])
        node_pos = nx.get_node_attributes(G, 'pos')

        G.add_edges_from(self.visual)
        nx.draw_networkx(G, node_pos)
        ax = plt.gca()
        ax.set(xlim=(x_min, x_max), ylim=(y_min, y_max))
        plt.show()


G = GraphVisualization()

for key, value in DCEL.vertices.items():

    G.addNode(key, value.x, value.y)
    for half_edge in value.hedges:
        G.addEdge(half_edge.tail.name, half_edge.twin.tail.name)

print("==========================")

G.visualize()

G_v = GraphVisualization()



print("==========================")

for i in DCEL.v_hedges:
    G_v.addEdge(i.tail.name, i.twin.tail.name)
    G_v.addNode(i.tail.name, i.tail.x, i.tail.y)

for i, a in DCEL.vertices.items():
    # print(i,a,(DCEL.pose[i]))
    G_v.addNode(i, a.x, a.y)

G_v.visualize()

G = nx.path_graph(6)
center_nodes = {0, 3}
cells = nx.voronoi_cells(G, center_nodes)
partition = set(map(frozenset, cells.values()))
sorted(map(sorted, partition))

# for i in DCEL.v_hedges: 
#     print(i.tail.name)
#     print(i.tail.x, i.tail.y)
#     print(i.twin.tail.x, i.twin.tail.y)

#     # print(dir(i))
#     # print(i.tail, i.twin.tail)

# print(DCEL.v_hedges)

print(DCEL.v_vertices)
