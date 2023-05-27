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
        for i in range(0,8):
            cubie_x = self.cube[i]
        # for cubie_x in self.cube:
            mesh_trace_list, points_trace_list = self.get_cubie_trace(cubie_x)
            for trace_x in points_trace_list:
                fig.add_trace(trace_x)
            for trace_y in mesh_trace_list:
                fig.add_trace(trace_y)
        scene = dict(camera=dict(eye=dict(x=1.15, y=1.15, z=0.8)),  # the default values are 1.25, 1.25, 1.25
                     xaxis=dict(),
                     yaxis=dict(),
                     zaxis=dict(),
                     aspectmode='data',  # this string can be 'data', 'cube', 'auto', 'manual'
                     # a custom aspectratio is defined as follows:
                     aspectratio=dict(x=1, y=1, z=1))
        fig.update_layout(scene=scene)
        fig.show()

    @staticmethod
    def get_cubie_trace(cubie):
        size1 = 10
        mode1 = 'lines+markers'
        tag = cubie.tag
        traces = []
        points_traces = []
        if cubie.current_face1_points is not None:
            color1 = cubie.current_face1_points["color"]
            points = cubie.current_face1_points["points"]
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
            points = cubie.current_face2_points["points"]
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
            points = cubie.current_face3_points["points"]
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


# def display_color_test():
#     fig_test = go.Figure()
#     l = 10
#     deg = 10
#     T1_mat = np.asarray([[1, 0, 0, 0],
#                         [0, np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0],
#                         [0, -np.sin(np.radians(deg)), np.cos(np.radians(deg)), 0],
#                         [0, 0, 0, 1]])
#     T2_mat = np.asarray([[np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0, 0],
#                         [np.sin(np.radians(deg)), np.cos(np.radians(deg)), 0, 0],
#                         [0, 0, 1, 0],
#                         [0, 0, 0, 1]])
#     T_mat = np.matmul(T1_mat, T2_mat)
#     point1 = np.asarray([0, 3, 3, 1])
#     point2 = np.asarray([0, 2, 3, 1])
#     point3 = np.asarray([0, 3, 2, 1])
#     point4 = np.asarray([0, 2, 2, 1])
#     trans_point1 = np.matmul(T_mat, np.transpose(point1))
#     trans_point2 = np.matmul(T_mat, np.transpose(point2))
#     trans_point3 = np.matmul(T_mat, np.transpose(point3))
#     trans_point4 = np.matmul(T_mat, np.transpose(point4))
#     trans_points = np.asarray([np.transpose(trans_point1), np.transpose(trans_point2),
#                                np.transpose(trans_point3), np.transpose(trans_point4)])
#     x = trans_points[:, 0]
#     y = trans_points[:, 1]
#     z = trans_points[:, 2]
#     fig_test.add_trace(go.Mesh3d(x=x, y=y, z=z, color="green", name='yz_plane'))
#     fig_test.add_trace(go.Scatter3d(x=x, y=y, z=z, mode="markers", marker=dict(size=10, color="green"), name='test'))
#     # fig_test.add_trace(go.Mesh3d(y=np.asarray([0, 0, 0, 0]), x=np.asarray([3, 2, 3, 2]), z=np.asarray([3, 3, 2, 2]),
#     #                         color="orange", name='zx_plane'))
#     fig_test.show()
#
#
# display_color_test()