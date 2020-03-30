from covid19lib.data import preprocess_data, extract_archives
import os
import sys
import glob

if __name__ == '__main__':
    PATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, PATH)

    datafolder = "data" + os.path.sep
    outputdir = "preprocessed_data" + os.path.sep
    tmpdir = "tmp" + os.path.sep
    
    for file in os.listdir(datafolder):
        if file.endswith(".zip") & file.startswith("INSEE_deces_"):
            extract_archives(os.path.join(datafolder, file), outputdir=tmpdir)
            preprocess_data(str.split(file, sep=".")[0], inputdir=tmpdir, outputdir=outputdir)

        if file.endswith(".zip") & file.startswith("other_structure_TBD_"):
            extract_archives(os.path.join(datafolder, file), outputdir=tmpdir)
            #preprocess_data_2020(str.split(file, sep=".")[0], inputdir=tmpdir, outputdir=outputdir)


    [os.remove(file) for file in glob.glob(os.path.join(tmpdir, "*.csv"))]

