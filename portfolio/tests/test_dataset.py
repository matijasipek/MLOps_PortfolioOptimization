import pandas as pd
import os
from tests import _PATH_DATA
import pytest


def test_dataframe_type():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_train.csv"))
    assert isinstance(dataset, pd.DataFrame)

def test_non_empty():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_train.csv"))
    assert not dataset.empty

def test_columns():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_train.csv"))
    expected_columns = ['Date', 'AAL.L', 'ABF.L', 'AHT.L', 'ANTO.L', 'AV.L', 'AZN.L', 'BA.L',
       'BARC.L', 'BATS.L', 'BDEV.L', 'BKG.L', 'BLND.L', 'BNZL.L', 'BP.L',
       'BT-A.L', 'CNA.L', 'CRDA.L', 'DGE.L', 'FCIT.L', 'GSK.L', 'HLMA.L',
       'HSBA.L', 'HSX.L', 'III.L', 'IMB.L', 'INF.L', 'JD.L', 'JMAT.L', 'KGF.L',
       'LAND.L', 'LGEN.L', 'LLOY.L', 'NG.L', 'NWG.L', 'NXT.L', 'PRU.L',
       'PSN.L', 'PSON.L', 'REL.L', 'RIO.L', 'RKT.L', 'RR.L', 'RTO.L', 'SBRY.L',
       'SDR.L', 'SGE.L', 'SGRO.L', 'SMDS.L', 'SMIN.L', 'SMT.L', 'SN.L',
       'SPX.L', 'SSE.L', 'STAN.L', 'STJ.L', 'SVT.L', 'TSCO.L', 'TW.L',
       'ULVR.L', 'UU.L', 'VOD.L', 'WEIR.L', 'WPP.L', 'WTB.L'] 
    assert list(dataset.columns) == expected_columns

def test_no_nan_values():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_train.csv"))
    assert not dataset.isnull().values.any()

def test_dataframe_type_test():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_test.csv"))
    assert isinstance(dataset, pd.DataFrame)

def test_non_empty_test():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_test.csv"))
    assert not dataset.empty

def test_columns_test():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_test.csv"))
    expected_columns = ['Date', 'AAL.L', 'ABF.L', 'AHT.L', 'ANTO.L', 'AV.L', 'AZN.L', 'BA.L',
       'BARC.L', 'BATS.L', 'BDEV.L', 'BKG.L', 'BLND.L', 'BNZL.L', 'BP.L',
       'BT-A.L', 'CNA.L', 'CRDA.L', 'DGE.L', 'FCIT.L', 'GSK.L', 'HLMA.L',
       'HSBA.L', 'HSX.L', 'III.L', 'IMB.L', 'INF.L', 'JD.L', 'JMAT.L', 'KGF.L',
       'LAND.L', 'LGEN.L', 'LLOY.L', 'NG.L', 'NWG.L', 'NXT.L', 'PRU.L',
       'PSN.L', 'PSON.L', 'REL.L', 'RIO.L', 'RKT.L', 'RR.L', 'RTO.L', 'SBRY.L',
       'SDR.L', 'SGE.L', 'SGRO.L', 'SMDS.L', 'SMIN.L', 'SMT.L', 'SN.L',
       'SPX.L', 'SSE.L', 'STAN.L', 'STJ.L', 'SVT.L', 'TSCO.L', 'TW.L',
       'ULVR.L', 'UU.L', 'VOD.L', 'WEIR.L', 'WPP.L', 'WTB.L'] 
    assert list(dataset.columns) == expected_columns

def test_no_nan_values_test():
    dataset = pd.read_csv(os.path.join(_PATH_DATA+'/processed/', "X_test.csv"))
    assert not dataset.isnull().values.any()