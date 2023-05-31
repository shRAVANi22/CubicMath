import numpy as np
from dataclasses import dataclass


@dataclass
class Cubie():
    tag: str
    type: str
    home_cubicle: str
    current_cubicle: str
    current_face1_points: dict | None
    current_face2_points: dict | None
    current_face3_points: dict | None
    ideal_face1_points: dict | None
    ideal_face2_points: dict | None
    ideal_face3_points: dict | None


def get_corner_cubies_8(off):
    ## UBL Cubie
    ubl = Cubie("UBL", "corner", "ubl", "ubl", None, None, None, None, None, None)
    ubl.current_face1_points = {"points": np.array([[0, 3, 3], [1-off, 3, 3], [0, 2+off, 3], [1-off, 2+off, 3]]), "color": "white"}
    ubl.current_face2_points = {"points": np.array([[0, 3, 3], [1-off, 3, 3], [0, 3, 2+off], [1-off, 3, 2+off]]), "color": "orange"}
    ubl.current_face3_points = {"points": np.array([[0, 3, 3], [0, 2+off, 3], [0, 3, 2+off], [0, 2+off, 2+off]]), "color": "green"}
    ubl.ideal_face1_points = {"points": np.array([[0, 3, 3], [1-off, 3, 3], [0, 2+off, 3], [1-off, 2+off, 3]]), "color": "white"}
    ubl.ideal_face2_points = {"points": np.array([[0, 3, 3], [1-off, 3, 3], [0, 3, 2+off], [1-off, 3, 2+off]]), "color": "orange"}
    ubl.ideal_face3_points = {"points": np.array([[0, 3, 3], [0, 2+off, 3], [0, 3, 2+off], [0, 2+off, 2+off]]), "color": "green"}

    ## UFL Cubie
    ufl = Cubie("UFL", "corner", "ufl", "ufl",
                {"points": np.array([[0, 0, 3], [1-off, 0, 3], [0, 1-off, 3], [1-off, 1-off, 3]]), "color": "white"},
                {"points": np.array([[0, 0, 3], [1-off, 0, 3], [0, 0, 2+off], [1-off, 0, 2+off]]), "color": "red"},
                {"points": np.array([[0, 0, 3], [0, 1-off, 3], [0, 0, 2+off], [0, 1-off, 2+off]]), "color": "green"},
                {"points": np.array([[0, 0, 3], [1 - off, 0, 3], [0, 1 - off, 3], [1 - off, 1 - off, 3]]),
                 "color": "white"},
                {"points": np.array([[0, 0, 3], [1 - off, 0, 3], [0, 0, 2 + off], [1-off, 0, 2 + off]]), "color": "red"},
                {"points": np.array([[0, 0, 3], [0, 1 - off, 3], [0, 0, 2 + off], [0, 1 - off, 2 + off]]),
                 "color": "green"})

    ## UFR Cubie
    ufr = Cubie("UFR", "corner", "ufr", "ufr",
                {"points": np.array([[3, 0, 3], [2+off, 0, 3], [3, 1-off, 3], [2+off, 1-off, 3]]), "color": "white"},
                {"points": np.array([[3, 0, 3], [2+off, 0, 3], [3, 0, 2+off], [2+off, 0, 2+off]]), "color": "red"},
                {"points": np.array([[3, 0, 3], [3, 0, 2+off], [3, 1-off, 3], [3, 1-off, 2+off]]), "color": "blue"},
                {"points": np.array([[3, 0, 3], [2 + off, 0, 3], [3, 1 - off, 3], [2+off, 1 - off, 3]]), "color": "white"},
                {"points": np.array([[3, 0, 3], [2 + off, 0, 3], [3, 0, 2 + off], [2+off, 0, 2 + off]]), "color": "red"},
                {"points": np.array([[3, 0, 3], [3, 0, 2 + off], [3, 1 - off, 3], [3, 1 - off, 2 + off]]),
                 "color": "blue"})

    ## URB Cubie
    urb = Cubie("URB", "corner", "urb", "urb",
                {"points": np.array([[3, 3, 3], [3, 2+off, 3], [2+off, 3, 3], [2+off, 2+off, 3]]), "color": "white"},
                {"points": np.array([[3, 3, 3], [3, 2+off, 3], [3, 3, 2+off], [3, 2+off, 2+off]]), "color": "blue"},
                {"points": np.array([[3, 3, 3], [3, 3, 2+off], [2+off, 3, 3], [2+off, 3, 2+off]]), "color": "orange"},
                {"points": np.array([[3, 3, 3], [3, 2 + off, 3], [2 + off, 3, 3], [2 + off, 2 + off, 3]]),
                 "color": "white"},
                {"points": np.array([[3, 3, 3], [3, 2 + off, 3], [3, 3, 2 + off], [3, 2 + off, 2 + off]]),
                 "color": "blue"},
                {"points": np.array([[3, 3, 3], [3, 3, 2 + off], [2 + off, 3, 3], [2 + off, 3, 2 + off]]),
                 "color": "orange"})

    ## DBL Cubie
    dbl = Cubie("DBL", "corner", "dbl", "dbl",
                {"points": np.array([[0, 3, 0], [1-off, 3, 0], [0, 2+off, 0], [1-off, 2+off, 0]]), "color": "yellow"},
                {"points": np.array([[0, 3, 0], [1-off, 3, 0], [0, 3, 1-off], [1-off, 3, 1-off]]), "color": "orange"},
                {"points": np.array([[0, 3, 0], [0, 3, 1-off], [0, 2+off, 0], [0, 2+off, 1-off]]), "color": "green"},
                {"points": np.array([[0, 3, 0], [1 - off, 3, 0], [0, 2 + off, 0], [1 - off, 2 + off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[0, 3, 0], [1 - off, 3, 0], [0, 3, 1 - off], [1 - off, 3, 1 - off]]),
                 "color": "orange"},
                {"points": np.array([[0, 3, 0], [0, 3, 1 - off], [0, 2 + off, 0], [0, 2 + off, 1 - off]]),
                 "color": "green"})

    ## DFL Cubie
    dfl = Cubie("DFL", "corner", "dfl", "dfl",
                {"points": np.array([[0, 0, 0], [1-off, 0, 0], [0, 1-off, 0], [1-off, 1-off, 0]]), "color": "yellow"},
                {"points": np.array([[0, 0, 0], [1-off, 0, 0], [0, 0, 1-off], [1-off, 0, 1-off]]), "color": "red"},
                {"points": np.array([[0, 0, 0], [0, 1-off, 0], [0, 0, 1-off], [0, 1-off, 1-off]]), "color": "green"},
                {"points": np.array([[0, 0, 0], [1 - off, 0, 0], [0, 1 - off, 0], [1 - off, 1 - off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[0, 0, 0], [1 - off, 0, 0], [0, 0, 1 - off], [1 - off, 0, 1 - off]]),
                 "color": "red"},
                {"points": np.array([[0, 0, 0], [0, 1 - off, 0], [0, 0, 1 - off], [0, 1 - off, 1 - off]]),
                 "color": "green"})

    ## DFR Cubie
    dfr = Cubie("DFR", "corner", "dfr", "dfr",
                {"points": np.array([[3, 0, 0], [2+off, 0, 0], [3, 1-off, 0], [2+off, 1-off, 0]]), "color": "yellow"},
                {"points": np.array([[3, 0, 0], [2+off, 0, 0], [3, 0, 1-off], [2+off, 0, 1-off]]), "color": "red"},
                {"points": np.array([[3, 0, 0], [3, 0, 1-off], [3, 1-off, 0], [3, 1-off, 1-off]]), "color": "blue"},
                {"points": np.array([[3, 0, 0], [2 + off, 0, 0], [3, 1 - off, 0], [2 + off, 1 - off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[3, 0, 0], [2 + off, 0, 0], [3, 0, 1 - off], [2 + off, 0, 1 - off]]),
                 "color": "red"},
                {"points": np.array([[3, 0, 0], [3, 0, 1 - off], [3, 1 - off, 0], [3, 1 - off, 1 - off]]),
                 "color": "blue"})

    ## DRB Cubie
    drb = Cubie("DRB", "corner", "drb", "drb",
                {"points": np.array([[3, 3, 0], [3, 2+off, 0], [2+off, 3, 0], [2+off, 2+off, 0]]), "color": "yellow"},
                {"points": np.array([[3, 3, 0], [3, 2+off, 0], [3, 3, 1-off], [3, 2+off, 1-off]]), "color": "blue"},
                {"points": np.array([[3, 3, 0], [3, 3, 1-off], [2+off, 3, 0], [2+off, 3, 1-off]]), "color": "orange"},
                {"points": np.array([[3, 3, 0], [3, 2 + off, 0], [2 + off, 3, 0], [2 + off, 2 + off, 0]]),
                 "color": "yellow"},
                {"points": np.array([[3, 3, 0], [3, 2 + off, 0], [3, 3, 1 - off], [3, 2 + off, 1-off]]), "color": "blue"},
                {"points": np.array([[3, 3, 0], [3, 3, 1 - off], [2 + off, 3, 0], [2 + off, 3, 1-off]]), "color": "orange"})
    corner_cubies = [ubl, ufl, ufr, urb, dbl, dfl, dfr, drb]
    return corner_cubies


def get_edge_cubies_12(off):
    ## UL Cubie
    ul = Cubie("UL", "edge", "ul", "ul",
               {"points": np.array([[0, 1, 3], [0, 2, 3], [1-off, 1, 3], [1-off, 2, 3]]), "color": "white"},
               {"points": np.array([[0, 1, 3], [0, 2, 3], [0, 1, 2+off], [0, 2, 2+off]]), "color": "green"}, None,
               {"points": np.array([[0, 1, 3], [0, 2, 3], [1-off, 1, 3], [1-off, 2, 3]]), "color": "white"},
               {"points": np.array([[0, 1, 3], [0, 2, 3], [0, 1, 2+off], [0, 2, 2+off]]), "color": "green"}, None)
    ## UF Cubie
    uf = Cubie("UF", "edge", "uf", "uf",
               {"points": np.array([[1, 0, 3], [2, 0, 3], [1, 1-off, 3], [2, 1-off, 3]]), "color": "white"},
               {"points": np.array([[1, 0, 3], [2, 0, 3], [1, 0, 2+off], [2, 0, 2+off]]), "color": "red"}, None,
               {"points": np.array([[1, 0, 3], [2, 0, 3], [1, 1-off, 3], [2, 1-off, 3]]), "color": "white"},
               {"points": np.array([[1, 0, 3], [2, 0, 3], [1, 0, 2+off], [2, 0, 2+off]]), "color": "red"}, None)
    ## UR Cubie
    ur = Cubie("UR", "edge", "ur", "ur",
               {"points": np.array([[3, 1, 3], [3, 2, 3], [2+off, 1, 3], [2+off, 2, 3]]), "color": "white"},
               {"points": np.array([[3, 1, 3], [3, 2, 3], [3, 1, 2+off], [3, 2, 2+off]]), "color": "blue"}, None,
               {"points": np.array([[3, 1, 3], [3, 2, 3], [2+off, 1, 3], [2+off, 2, 3]]), "color": "white"},
               {"points": np.array([[3, 1, 3], [3, 2, 3], [3, 1, 2+off], [3, 2, 2+off]]), "color": "blue"}, None)
    ## UB Cubie
    ub = Cubie("UB", "edge", "ub", "ub",
               {"points": np.array([[1, 3, 3], [2, 3, 3], [1, 2+off, 3], [2, 2+off, 3]]), "color": "white"},
               {"points": np.array([[1, 3, 3], [2, 3, 3], [1, 3, 2+off], [2, 3, 2+off]]), "color": "orange"}, None,
               {"points": np.array([[1, 3, 3], [2, 3, 3], [1, 2+off, 3], [2, 2+off, 3]]), "color": "white"},
               {"points": np.array([[1, 3, 3], [2, 3, 3], [1, 3, 2+off], [2, 3, 2+off]]), "color": "orange"}, None)

    ## BL Cubie
    bl = Cubie("BL", "edge", "bl", "bl",
               {"points": np.array([[0, 3, 1], [0, 3, 2], [1-off, 3, 1], [1-off, 3, 2]]), "color": "orange"},
               {"points": np.array([[0, 3, 1], [0, 3, 2], [0, 2+off, 1], [0, 2+off, 2]]), "color": "green"}, None,
               {"points": np.array([[0, 3, 1], [0, 3, 2], [1-off, 3, 1], [1-off, 3, 2]]), "color": "orange"},
               {"points": np.array([[0, 3, 1], [0, 3, 2], [0, 2+off, 1], [0, 2+off, 2]]), "color": "green"}, None)
    ## LF Cubie
    lf = Cubie("LF", "edge", "lf", "lf",
               {"points": np.array([[0, 0, 1], [0, 0, 2], [0, 1-off, 1], [0, 1-off, 2]]), "color": "green"},
               {"points": np.array([[0, 0, 1], [0, 0, 2], [1-off, 0, 1], [1-off, 0, 2]]), "color": "red"}, None,
               {"points": np.array([[0, 0, 1], [0, 0, 2], [0, 1-off, 1], [0, 1-off, 2]]), "color": "green"},
               {"points": np.array([[0, 0, 1], [0, 0, 2], [1-off, 0, 1], [1-off, 0, 2]]), "color": "red"}, None)
    ## FR Cubie
    fr = Cubie("FR", "edge", "fr", "fr",
               {"points": np.array([[3, 0, 1], [3, 0, 2], [2+off, 0, 1], [2+off, 0, 2]]), "color": "red"},
               {"points": np.array([[3, 0, 1], [3, 0, 2], [3, 1-off, 1], [3, 1-off, 2]]), "color": "blue"}, None,
               {"points": np.array([[3, 0, 1], [3, 0, 2], [2+off, 0, 1], [2+off, 0, 2]]), "color": "red"},
               {"points": np.array([[3, 0, 1], [3, 0, 2], [3, 1-off, 1], [3, 1-off, 2]]), "color": "blue"}, None)
    ## RB Cubie
    rb = Cubie("RB", "edge", "rb", "rb",
               {"points": np.array([[3, 3, 1], [3, 3, 2], [3, 2+off, 1], [3, 2+off, 2]]), "color": "blue"},
               {"points": np.array([[3, 3, 1], [3, 3, 2], [2+off, 3, 1], [2+off, 3, 2]]), "color": "orange"}, None,
               {"points": np.array([[3, 3, 1], [3, 3, 2], [3, 2+off, 1], [3, 2+off, 2]]), "color": "blue"},
               {"points": np.array([[3, 3, 1], [3, 3, 2], [2+off, 3, 1], [2+off, 3, 2]]), "color": "orange"}, None)

    ## DL Cubie
    dl = Cubie("DL", "edge", "dl", "dl",
               {"points": np.array([[0, 1, 0], [0, 2, 0], [1-off, 1, 0], [1-off, 2, 0]]), "color": "yellow"},
               {"points": np.array([[0, 1, 0], [0, 2, 0], [0, 1, 1-off], [0, 2, 1-off]]), "color": "green"}, None,
               {"points": np.array([[0, 1, 0], [0, 2, 0], [1-off, 1, 0], [1-off, 2, 0]]), "color": "yellow"},
               {"points": np.array([[0, 1, 0], [0, 2, 0], [0, 1, 1-off], [0, 2, 1-off]]), "color": "green"}, None)
    ## DF Cubie
    df = Cubie("DF", "edge", "df", "df",
               {"points": np.array([[1, 0, 0], [2, 0, 0], [1, 1-off, 0], [2, 1-off, 0]]), "color": "yellow"},
               {"points": np.array([[1, 0, 0], [2, 0, 0], [1, 0, 1-off], [2, 0, 1-off]]), "color": "red"}, None,
               {"points": np.array([[1, 0, 0], [2, 0, 0], [1, 1-off, 0], [2, 1-off, 0]]), "color": "yellow"},
               {"points": np.array([[1, 0, 0], [2, 0, 0], [1, 0, 1-off], [2, 0, 1-off]]), "color": "red"}, None)
    ## DR Cubie
    dr = Cubie("DR", "edge", "dr", "dr",
               {"points": np.array([[3, 1, 0], [3, 2, 0], [2+off, 1, 0], [2+off, 2, 0]]), "color": "yellow"},
               {"points": np.array([[3, 1, 0], [3, 2, 0], [3, 1, 1-off], [3, 2, 1-off]]), "color": "blue"}, None,
               {"points": np.array([[3, 1, 0], [3, 2, 0], [2+off, 1, 0], [2+off, 2, 0]]), "color": "yellow"},
               {"points": np.array([[3, 1, 0], [3, 2, 0], [3, 1, 1-off], [3, 2, 1-off]]), "color": "blue"}, None)
    ## DB Cubie
    db = Cubie("DB", "edge", "db", "db",
               {"points": np.array([[1, 3, 0], [2, 3, 0], [1, 2+off, 0], [2, 2+off, 0]]), "color": "yellow"},
               {"points": np.array([[1, 3, 0], [2, 3, 0], [1, 3, 1-off], [2, 3, 1-off]]), "color": "orange"}, None,
               {"points": np.array([[1, 3, 0], [2, 3, 0], [1, 2+off, 0], [2, 2+off, 0]]), "color": "yellow"},
               {"points": np.array([[1, 3, 0], [2, 3, 0], [1, 3, 1-off], [2, 3, 1-off]]), "color": "orange"}, None)

    edge_cubies = [ul, uf, ur, ub, bl, lf, fr, rb, dl, df, dr, db]
    return edge_cubies


def get_center_cubies_6():
    ## Up face centre
    u = Cubie("U", "center", "u", "u",
              {"points": np.array([[1, 1, 3], [2, 1, 3], [1, 2, 3], [2, 2, 3]]), "color": "white"}, None, None,
              {"points": np.array([[1, 1, 3], [2, 1, 3], [1, 2, 3], [2, 2, 3]]), "color": "white"}, None, None)
    ## Down face centre
    d = Cubie("D", "center", "d", "d",
              {"points": np.array([[1, 1, 0], [2, 1, 0], [1, 2, 0], [2, 2, 0]]), "color": "yellow"}, None, None,
              {"points": np.array([[1, 1, 0], [2, 1, 0], [1, 2, 0], [2, 2, 0]]), "color": "yellow"}, None, None)
    ## Front face centre
    f = Cubie("F", "center", "f", "f",
              {"points": np.array([[1, 0, 1], [1, 0, 2], [2, 0, 1], [2, 0, 2]]), "color": "red"}, None, None,
              {"points": np.array([[1, 0, 1], [1, 0, 2], [2, 0, 1], [2, 0, 2]]), "color": "red"}, None, None)
    ## Back face centre
    b = Cubie("B", "center", "b", "b",
              {"points": np.array([[1, 3, 1], [1, 3, 2], [2, 3, 1], [2, 3, 2]]), "color": "orange"}, None, None,
              {"points": np.array([[1, 3, 1], [1, 3, 2], [2, 3, 1], [2, 3, 2]]), "color": "orange"}, None, None)
    ## Left face centre
    l = Cubie("L", "center", "l", "l",
              {"points": np.array([[0, 1, 1], [0, 2, 1], [0, 1, 2], [0, 2, 2]]), "color": "green"}, None, None,
              {"points": np.array([[0, 1, 1], [0, 2, 1], [0, 1, 2], [0, 2, 2]]), "color": "green"}, None, None)
    ## Right face centre
    r = Cubie("R", "center", "r", "r",
              {"points": np.array([[3, 1, 1], [3, 2, 1], [3, 1, 2], [3, 2, 2]]), "color": "blue"}, None, None,
              {"points": np.array([[3, 1, 1], [3, 2, 1], [3, 1, 2], [3, 2, 2]]), "color": "blue"}, None, None)
    center_cubies = [u, d, f, b, l, r]
    return center_cubies