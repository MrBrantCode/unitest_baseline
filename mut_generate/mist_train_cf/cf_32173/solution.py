"""
QUESTION:
Write a function `concatenate_arrays` that takes 16 1D arrays as input, where each pair of 8 arrays contains the same type of data. The function should concatenate each pair of arrays and return the concatenated arrays as a dictionary with keys 'aux_id', 'lat', 'mid_lat', 'lon', 'mid_lon', 'elev', 'point_type', and 'seg_name'. The input arrays are: `aux_id_var`, `lat_var`, `mid_pt_lat_var`, `lon_var`, `mid_pt_lon_var`, `elev_var`, `point_type_var`, `seg_name_var`, `np_rwis_aux_id`, `np_rwis_lat`, `np_rwis_mid_pt_lat`, `np_rwis_lon`, `np_rwis_mid_pt_lon`, `np_rwis_elev`, `np_rwis_point_type`, and `np_rwis_seg_name`.
"""

import numpy as np

def concatenate_arrays(aux_id_var, lat_var, mid_pt_lat_var, lon_var, mid_pt_lon_var, elev_var, point_type_var, seg_name_var, np_rwis_aux_id, np_rwis_lat, np_rwis_mid_pt_lat, np_rwis_lon, np_rwis_mid_pt_lon, np_rwis_elev, np_rwis_point_type, np_rwis_seg_name):
    concatenated_arrays = {
        'aux_id': np.concatenate([aux_id_var, np_rwis_aux_id]),
        'lat': np.concatenate([lat_var, np_rwis_lat]),
        'mid_lat': np.concatenate([mid_pt_lat_var, np_rwis_mid_pt_lat]),
        'lon': np.concatenate([lon_var, np_rwis_lon]),
        'mid_lon': np.concatenate([mid_pt_lon_var, np_rwis_mid_pt_lon]),
        'elev': np.concatenate([elev_var, np_rwis_elev]),
        'point_type': np.concatenate([point_type_var, np_rwis_point_type]),
        'seg_name': np.concatenate([seg_name_var, np_rwis_seg_name])
    }
    return concatenated_arrays