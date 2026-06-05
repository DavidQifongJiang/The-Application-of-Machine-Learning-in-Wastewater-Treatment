# Data Notes

The `data/` directory contains the research datasets and derived feature tables used by the notebooks.

## Files

- `Wastewater treatment plant.csv`: plant-level wastewater treatment observations.
- `Original dataset.xlsx` and `QAQ.xlsx`: original spreadsheet sources preserved for reproducibility.
- `data_features_Class.csv` and `data_features_phylums.csv`: engineered microbiome feature tables.
- `CHANGE RATE(Class).csv` and `CHANGE RATE(PHYLUM).csv`: change-rate modeling tables.
- `SBDJWCLASS.csv` and `combination.csv`: combined class/phylum feature datasets used by experiments.

## Reproducibility

The notebooks keep the original experimental trail. The Python package is intended to make the reusable parts portable: preprocessing, model selection, tuning, and evaluation. If this repo is used for publication-grade reproduction, pin package versions and record the exact notebook run order.
