# Etienne.St-Onge@usherbrooke.ca

from trimeshpy.math import *


def vertices_gaussian_curvature(triangles, vertices, area_weighted=False):
    theta_matrix = edge_theta_angle(triangles, vertices)
    gaussian_curvature = np.squeeze(np.array(2.0 * np.pi - theta_matrix.sum(1)))
    if area_weighted:
        vts_mix_area = vertices_mix_area(triangles, vertices)
        gaussian_curvature = gaussian_curvature / vts_mix_area
    return np.squeeze(np.array(gaussian_curvature))


def vertices_cotan_curvature(triangles, vertices, area_weighted=True):
    vts_dir = vertices_cotan_direction(triangles, vertices, normalize=False, area_weighted=area_weighted)
    vts_normal = vertices_normal(triangles, vertices, normalize=False, area_weighted=area_weighted)
    curvature_sign = -np.sign(dot(vts_dir, vts_normal))
    curvature = length(vts_dir)
    
    return curvature*curvature_sign


def vertices_cotan_direction(triangles, vertices, normalize=True, area_weighted=True):
    curvature_normal_mtx = mean_curvature_normal_matrix(triangles, vertices, area_weighted=area_weighted)
    cotan_normal = curvature_normal_mtx.dot(vertices)

    if normalize:
        return normalize_vectors(cotan_normal)
    return cotan_normal