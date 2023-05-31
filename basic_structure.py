import numpy as np
from cubies_26 import get_corner_cubies_8, get_edge_cubies_12, get_center_cubies_6
import plotly.graph_objects as go


class RubiksCube3x3():
    def __init__(self):
        self.cube = self.construct_ideal_cube()  ## list of 26 cubie class objects

    @staticmethod
    def construct_ideal_cube():
        corners = get_corner_cubies_8()
        edges = get_edge_cubies_12()
        centers = get_center_cubies_6()
        cube = corners + edges+ centers
        return cube

    def display_cube(self):
        fig = go.Figure()
        for cubie_x in self.cube:
            mesh_trace_list, points_trace_list = self.get_cubie_trace(cubie_x)
            # for trace_x in points_trace_list:
            #     fig.add_trace(trace_x)
            for trace_y in mesh_trace_list:
                fig.add_trace(trace_y)
        fig.update_yaxes(
            scaleanchor="x",
            scaleratio=1,
        )
        fig.show()

    @staticmethod
    def bias_plotly_transformation(points):
        transformed_points = []
        deg = 10
        T1_mat = np.asarray([[1, 0, 0, 0],
                             [0, np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0],
                             [0, -np.sin(np.radians(deg)), np.cos(np.radians(deg)), 0],
                             [0, 0, 0, 1]])
        T2_mat = np.asarray([[np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0, 0],
                             [-np.sin(np.radians(deg)), np.cos(np.radians(deg)), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
        T_mat = np.matmul(T1_mat, T2_mat)
        for point in points:
            point1 = np.asarray([[point[0]], [point[1]], [point[2]], [1]])
            trans_point1 = np.matmul(T_mat, point1)
            trans_point = np.transpose(trans_point1)
            transformed_points.append(trans_point[0])
        return np.asarray(transformed_points)

    def get_cubie_trace(self, cubie):
        size1 = 10
        mode1 = 'lines+markers'
        tag = cubie.tag
        traces = []
        points_traces = []
        if cubie.current_face1_points is not None:
            color1 = cubie.current_face1_points["color"]
            points1 = cubie.current_face1_points["points"]
            points = self.bias_plotly_transformation(points1)
            x = points[:, 0]
            y = points[:, 1]
            z = points[:, 2]
            trace1 = go.Mesh3d(x=x, y=y, z=z, color=color1, name=tag)
            traces.append(trace1)

            pts_trace1 = go.Scatter3d(x=x, y=y, z=z, mode=mode1,
                                   marker=dict(size=size1, color=color1), name=tag)
            points_traces.append(pts_trace1)
        if cubie.current_face2_points is not None:
            color1 = cubie.current_face2_points["color"]
            points1 = cubie.current_face2_points["points"]
            points = self.bias_plotly_transformation(points1)
            x = points[:, 0]
            y = points[:, 1]
            z = points[:, 2]
            trace2 = go.Mesh3d(x=x, y=y, z=z, color=color1, name=tag)
            traces.append(trace2)
            pts_trace2 = go.Scatter3d(x=x, y=y, z=z, mode=mode1,
                                      marker=dict(size=size1, color=color1), name=tag)
            points_traces.append(pts_trace2)
        if cubie.current_face3_points is not None:
            color1 = cubie.current_face3_points["color"]
            points1 = cubie.current_face3_points["points"]
            points = self.bias_plotly_transformation(points1)
            x = points[:, 0]
            y = points[:, 1]
            z = points[:, 2]
            trace3 = go.Mesh3d(x=x, y=y, z=z, color=color1, name=tag)
            traces.append(trace3)
            pts_trace3 = go.Scatter3d(x=x, y=y, z=z, mode=mode1,
                                      marker=dict(size=size1, color=color1), name=tag)
            points_traces.append(pts_trace3)
        return traces, points_traces


test_cube = RubiksCube3x3()
ideal_cube = test_cube.cube
test_cube.display_cube()
print('')


