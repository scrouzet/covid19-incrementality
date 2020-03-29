import pytest
from covid19lib.data import extract_archives, add_features, load_preprocess_df, preprocess_data
import os
import pandas as pd
import pandas.testing as pdt


@pytest.fixture()
def dummyfolders():
    return {"name": "dummy", "datafolder": "../data/", "outputfolder": "../preprocessed_data/", "temp": "../temp/"}


def test_extract_archives(dummyfolders):
    """Check if extract correctly .zip to .csv"""
    extract_archives(dummyfolders["datafolder"]+dummyfolders["name"] + ".zip", outpudir=dummyfolders["temp"])
    files = [dummyfolders["temp"]+dummyfolders["name"]+".csv"]
    assert all([os.path.exists(file) for file in files])
    df = pd.read_csv(files[0], sep=";").drop(labels="date_deces", axis=1)
    expected_df = pd.DataFrame({"annee_comptabilisation": 2013,
                                "sexe": [1, 2, 1, 2, 1],
                                "age": [1, 2, 3, 4, 5],
                                "departement_deces": [1, 2, 3, 4, 5],
                                "nb_deces": 1})
    pdt.assert_frame_equal(df, expected_df)
    [os.remove(file) for file in files]


def test_preprocess_data(dummyfolders):
    """Check if extract correctly .zip to .csv and preprocess data"""
    extract_archives(dummyfolders["datafolder"]+dummyfolders["name"] + ".zip", outpudir=dummyfolders["temp"])
    preprocess_data(dummyfolders["name"], inputdir=dummyfolders["temp"], outputdir=dummyfolders["outputfolder"])
    files = [dummyfolders["outputfolder"]+dummyfolders["name"]+".pkl"]
    assert all([os.path.exists(file) for file in files])
    df = pd.read_pickle(files[0])
    expected_df = None  # add corresponding DF
    pdt.assert_frame_equal(df, expected_df)
    [os.remove(file) for file in files]

