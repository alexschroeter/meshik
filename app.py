from arkitekt_next import register
import time
import pymeshlab
import pandas as pd

@register
def generate_mesh_obj_from_csv(points: Table, mesh_filter_script: file = None) -> File:
    """Generate a Mesh Obj from a list of Coordinates in CSV
    
    Parameters
    ----------

    Returns
    -------
    """
    # Create a csv from Table
    df_from_table = table.to_pandas()
    df_from_table.to_csv('points.csv', header=False, index=False)

    # create the mesh
    ms = py.pymeshlab.MeshSet();
    ms.load_new_mesh("points.csv")
    if !mesh_filter_script:
        # transfer filter script 
        ms.load_filter_script(mesh_filter_script)
        ms.apply_filter_script()
    ms.save_current_mesh("mesh.obj")

    # upload the obj file
    # ToDo: Return mesh.obj file maybe as MeshFile (https://pymeshlab.readthedocs.io/en/latest/io_format_list.html)

