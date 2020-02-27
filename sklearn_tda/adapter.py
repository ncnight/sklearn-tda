"""
@author: Nithin Chalapathi
"""
import kmapper as km
import numpy as np

from .clustering import  MapperComplex

def create_mapper_complex_from_kmapper(km_graph, km_obj, X, filters, filter_bnds, colors):
    """
    km_graph: Kepler mapper defaultdict detailing node and edge information
    km_obj: Kepler Mapper Object
    X: Numpy array (N x D) N points in D dims to mapper was on
    filters: Numpy array (N x num_filters) Filters
    filter_bnds: Numpy array (num_filters x 2) Bounds of the filters. No default.
    colors: (N x num_colors) Used to color nodes. If none, same as the filters.
    Note this only works for 1D mapper
    """
    km_cover = km_obj.cover
    resolutions = np.asarray([km_cover.n_cubes for i in range(filters.shape[1])])
    gains = np.asarray([km_cover.perc_overlap for i in range(filters.shape[1])])

    # TODO: Inp, clusterer, and mask are default values ('point cloud', dbscan, 0) Will this break something?
    # TODO: Seems like it shouldn't matter.
    mc = MapperComplex(filters=filters, filter_bnds=filter_bnds, colors=colors, resolutions=resolutions, gains=gains)