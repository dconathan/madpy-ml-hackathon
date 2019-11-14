 # MadPy Machine Learning Hackathon 11/14/2019
 
 This is a repo for one team doing a machine learning hackathon as part of the [MadPy (Madison Python) meetup](https://www.meetup.com/MadPython/events/265880536/).
  
 Data and project description can be obtained [here](https://www.kaggle.com/c/competitive-data-science-predict-future-sales/data).
 
 ## Environment setup
 
 We use Python 3.7.  The easiest way to get an environment set up is to use [pipenv](https://pipenv-fork.readthedocs.io/en/latest/):
 
 ```
pipenv sync
pipenv shell
```

A `requirements.txt` file is provided in case you are using vanilla `pip`:
```
pip install -r requirements.txt
```

 
 ## Data
 
 Download the `competitive-data-science-predict-future-sales.zip` file and put it in the `data/` folder.  The `load.py` module will load all the CSV files from the zip into Pandas DataFrames.
 
 ```
from load import TEST_DF, SAMPLE_SUBMISSION_DF, SALES_TRAIN_DF, SHOPS_DF, ITEM_CATEGORIES_DF, ITEMS_DF
```

Descriptions of the contents can be found on the Kaggle website.


