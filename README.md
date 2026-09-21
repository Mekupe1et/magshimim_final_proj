# magshimim_final_proj

## Project Overview
The goal of this project is to develop a machine learning model capable of predicting the decade in which a given text was written. By analyzing linguistic patterns, vocabulary, and other textual features, the model aims to classify texts into their respective historical periods.

## Directory Structure
```text
magshimim_final/
├── base_dbs/
│   ├── Loc-PD-Books/
│   │   ├── train_00001.parquet
│   │   ├── train_00002.parquet
│   │   ├── train_00003.parquet
│   │   ├── train_00004.parquet
│   │   ├── train_00005.parquet
│   │   ├── train_00006.parquet
│   │   ├── train_00007.parquet
│   │   ├── train_00008.parquet
│   │   └── train_00009.parquet
│   ├── common_corpus_1930_2020_balanced.parquet
│   ├── reddit.parquet
│   ├── shard_00040.parquet
│   ├── subset_100_1.parquet
│   ├── subset_100_2.parquet
│   ├── textage_large.csv
│   ├── twitter.csv
│   └── youTube.csv
├── data_creators/
│   ├── assembler.ipynb
│   ├── common corpus.ipynb
│   ├── LoC-PD-Books.ipynb
│   ├── pre_1900_corpus_40.ipynb
│   ├── processor.py
│   ├── Reddit_data_Extract.ipynb
│   ├── textage_large.ipynb
│   ├── twitter.ipynb
│   └── youtube.ipynb
├── models/
├── processed_dbs/
│   ├── combined_dataset.parquet
│   ├── common_corpus.parquet
│   ├── LoC-PD-Books.parquet
│   ├── pre_1900_corpus_40.parquet
│   ├── reddit.parquet
│   ├── textage_large.parquet
│   ├── twitter.parquet
│   └── youtube.parquet
├── .gitattributes
├── .gitignore
├── main.ipynb
├── README.md
├── requirements.txt
└── update_readme.py
```

## Features
- **Dataset Preparation**: Includes various datasets from different sources (e.g., Library of Congress, Twitter, YouTube).
- **Text Analysis**: Preprocessing and feature extraction from text data.
- **Model Training**: Machine learning models trained to classify texts by decade.
- **Evaluation**: Metrics to assess model performance.

## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yoav33333/magshimim_final_proj.git](https://github.com/yoav33333/magshimim_final_proj.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd magshimim_final_proj
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare the datasets by running the preprocessing notebooks.
2. Train the model using `main.ipynb`.
3. Evaluate the model and make predictions on new text data.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Project Contributors
- **arbelmv123**
- **Mekupelet**

## License
This project is licensed under the MIT License.
