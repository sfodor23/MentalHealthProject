# MentalHealthProject

Rudimentary notebook project for suicide detection text classification using Reddit data.

## Project Structure

- `suicide-detection-using-reddit-data.ipynb`: Main analysis and modeling notebook.
- `input/suicide-watch/`: Local data folder (ignored by Git).

## Dataset

This project expects the CSV file at:

`input/suicide-watch/Suicide_Detection.csv`

Note: The dataset is intentionally not tracked in Git because it is too large for standard GitHub limits.

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies (minimum):
   - pandas
   - numpy
   - scikit-learn
   - nltk
   - matplotlib
   - tabulate
3. Launch Jupyter and open the notebook:

```bash
jupyter notebook suicide-detection-using-reddit-data.ipynb
```

## Notes

- Downloaded NLTK resources in the notebook may include:
  - `vader_lexicon`
  - `stopwords`
- Keep large data files in `input/` and out of Git history.
