from pathlib import Path
from zipfile import ZipFile
import pandas as pd

THIS_DIR = Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR.joinpath("data")
RAW_ZIPFILE = DATA_DIR.joinpath("competitive-data-science-predict-future-sales.zip")

with ZipFile(RAW_ZIPFILE) as zf:

    with zf.open("test.csv.gz") as f:
        TEST_DF = pd.read_csv(f, compression="gzip")

    with zf.open("sample_submission.csv.gz") as f:
        SAMPLE_SUBMISSION_DF = pd.read_csv(f, compression="gzip")

    with zf.open("sales_train.csv.gz") as f:
        SALES_TRAIN_DF = pd.read_csv(f, compression="gzip")

    with zf.open("shops.csv") as f:
        SHOPS_DF = pd.read_csv(f)

    with zf.open("item_categories.csv") as f:
        ITEM_CATEGORIES_DF = pd.read_csv(f)

    with zf.open("items.csv") as f:
        ITEMS_DF = pd.read_csv(f)
