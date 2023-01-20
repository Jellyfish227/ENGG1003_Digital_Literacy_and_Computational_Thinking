import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

header = ['User-Agent', 'Mozilla 5.0']
ambulance_service_indicators = pd.read_csv(
    "https://www.hkfsd.gov.hk/" + "datagovhk/datasets/Ambulance_Service_Indicators_eng.csv")
