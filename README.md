# MentalHealthProject

Text preprocessing pipeline for suicide detection data from Reddit.

## Current Status

Preprocessing is implemented and working.

Completed:
- Loaded dataset from `Input/SuicideData.csv`
- Keep first one-third of rows for faster experimentation
- Remove optional `Index` column
- Clean text (regex cleanup, contraction expansion, lowercasing)
- Split merged words with `wordninja`
- Remove stopwords and lemmatize
- Save processed output to `Output/ProcessedData.csv`

Not completed yet:
- Model training
- Evaluation/metrics reporting
- Final inference pipeline

## Project Structure

- `src/Preprocessing.py`: Main preprocessing script
- `Input/SuicideData.csv`: Input dataset (not currently saved in codebase due to issues with Github file limits)
- `Output/ProcessedData.csv`: Generated preprocessed dataset
- `suicide-detection-using-reddit-data.ipynb`: Notebook (not the active completed workflow)

## Requirements

Install at least:
- pandas
- nltk
- contractions
- wordninja

Example install:

```bash
pip install pandas nltk contractions wordninja
```

## Run Preprocessing

From project root:

```bash
python src/Preprocessing.py
```

The script downloads NLTK stopwords if needed and writes the cleaned CSV to `Output/ProcessedData.csv`.

## Notes

- The dataset is not tracked in Git and must be downloaded from https://www.kaggle.com/code/nouranmuhammad/suicide-detection-using-reddit-data
- Current work is focused on data cleaning only; model files are not yet part of the active pipeline.
