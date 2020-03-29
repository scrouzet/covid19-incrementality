import pytest
from covid19lib.data import extract_archives, add_features, load_preprocess_df, preprocess_data
import os
import pandas as pd
import pandas.testing as pdt
from zipfile import ZipFile
import glob


@pytest.fixture()
def dummyfolders(tmp_path):
    d = {"data": "../data/", "preprocessed_data": "../preprocessed_data/", "tmp": "../tmp/"}
    return d


@pytest.fixture()
def dummy_csv(dummyfolders):

    dummy_df = pd.DataFrame({"annee_comptabilisation": [1999, 2001, 2019, 1997, 2013],
                             "sexe": [1, 2, 1, 2, 1],
                             "age": [10, 20, 30, 40, 50],
                             "departement_deces": [1, 2, 3, 4, 5],
                             "nb_deces": 1,
                             "date_deces": ["01/05/1999", "31/12/2000", "12/06/2019", "28/04/1997", "09/11/2013"]})
    fn = os.path.join(dummyfolders["data"], "dummy.csv")
    dummy_df.to_csv(fn, sep=";")
    return fn

# TODO: the following fixture doesn't work as intended as it included the folder /data/ into archive.
# @pytest.fixture()
# def dummy_zip(dummyfolders, dummy_csv):
#     fn = os.path.join(dummyfolders["data"], "dummy.zip")
#     with ZipFile(fn, 'w') as myzip:
#         myzip.write(dummy_csv)
#     return fn



def test_extract_archives(dummyfolders, dummy_csv):
    """Check if extract correctly .zip to .csv"""
    extract_archives(dummyfolders["data"] + "dummy.zip", outputdir=dummyfolders["tmp"])
    files = [dummyfolders["tmp"] + "dummy.csv"]
    assert all([os.path.exists(file) for file in files])
    df = pd.read_csv(files[0], sep=";")
    expected_df = pd.read_csv(dummy_csv, sep=";")
    pdt.assert_frame_equal(df, expected_df)
    [os.remove(file) for file in files]


def test_preprocess_data(dummyfolders, dummy_csv):
    """Check if extract correctly .zip to .csv and preprocess data"""
    extract_archives(dummyfolders["data"] + "dummy.zip", outputdir=dummyfolders["tmp"])
    preprocess_data("dummy", inputdir=dummyfolders["tmp"], outputdir=dummyfolders["preprocessed_data"])
    files = [dummyfolders["preprocessed_data"] + "dummy.pkl"]
    assert all([os.path.exists(file) for file in files])
    df = pd.read_pickle(files[0])
    expected_df = pd.read_csv(dummy_csv, sep=";")
    pdt.assert_frame_equal(df, expected_df)
    [os.remove(file) for file in files]

