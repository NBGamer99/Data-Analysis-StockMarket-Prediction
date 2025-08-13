<div align="center">

<h3 align="center">STOCK MARKET LSTM PREDICTION
</h3>

  <p align="center">
    When your neural network thinks it knows the market better than Wall Street
    <br />
    <br />
    <a href="#contribute">Contribute</a>
    ·
    <a href="https://github.com/NBGamer99/stock-market-lstm-prediction/issues">Report Bug</a>
  </p>

![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) &emsp;
![tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white) &emsp;
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) &emsp;
![plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white) &emsp;
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) &emsp;
![sklearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

This is an intelligent stock market analysis application that leverages LSTM neural networks for price prediction and trend analysis. The project features an interactive Streamlit interface with real-time visualizations, candlestick charts, and AI-powered predictions for major tech stocks.

## Getting Started

### Prerequisites
* Python 3.8 or higher
* At least 4GB RAM (for model training)
* Internet connection (for fetching stock data)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/NBGamer99/stock-market-lstm-prediction.git
   ```

2. It is recommended to use a virtual environment
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```

4. Download pre-trained models (optional)
   ```sh
   # Models will be automatically trained on first run if not present
   # Pre-trained models can be found in the /models directory
   ```

## Usage

### Running the Application

To run the Streamlit app, execute the following command in the project directory:
```sh
streamlit run app.py
```
The app will be available at `http://localhost:8501`

### Supported Stocks
The application currently supports analysis for:
- AAPL (Apple Inc.)
- ADBE (Adobe Inc.)
- AMZN (Amazon.com Inc.)
- GOOGL (Alphabet Inc.)
- IBM (International Business Machines)
- INTC (Intel Corporation)
- META (Meta Platforms Inc.)
- MSFT (Microsoft Corporation)
- NVDA (NVIDIA Corporation)
- ORCL (Oracle Corporation)

### Features Demo

The application features:

![Live Demo](./demo.gif)

- **Interactive Stock Selection**: Choose from 10 major tech stocks
- **OHLC Candlestick Charts**: Beautiful interactive charts with volume data
- **LSTM Price Prediction**: AI-powered next-day price predictions
- **Historical Analysis**: Comprehensive trend analysis and statistics
- **Volume Distribution**: Color-coded volume analysis charts
- **Model Performance Metrics**: Real-time accuracy and loss tracking

## Architecture

- **Frontend**: Streamlit with interactive Plotly charts
- **Backend**: Python with TensorFlow/Keras for LSTM modeling
- **Data Processing**: pandas for data manipulation and feature engineering
- **Visualization**: Plotly for interactive financial charts
- **ML Pipeline**: Sequential LSTM with dropout regularization
- **Data Scaling**: MinMaxScaler for feature normalization

## Model Details

### LSTM Architecture
- **Layer 1**: 50 LSTM units with 0.2 dropout
- **Layer 2**: 60 LSTM units with 0.3 dropout  
- **Layer 3**: 80 LSTM units with 0.4 dropout
- **Layer 4**: 120 LSTM units with 0.5 dropout
- **Output**: Dense layer with single neuron
- **Optimizer**: Adam with MSE loss function

### Training Configuration
- **Window Size**: 100 days of historical data
- **Train/Test Split**: 70/30
- **Epochs**: 100 (with early stopping)
- **Batch Size**: 32

## Contribute

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. Feel free to open a pull request or an issue.

- Fork the repo
- Create a new branch (`git checkout -b feature/AmazingFeature`)
- Make your changes and add them (`git add .`)
- Commit and push your changes (`git commit -m 'Add some AmazingFeature' && git push origin feature/AmazingFeature`)
- Create a new pull request 🤩
- And that's it 😊
- Don't forget to star ⭐ the repo if you like it 😊

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

For any questions or suggestions, feel free to contact:
- Yasser Nabouzi - [@NBGamer99](https://www.github.com/NBGamer99)
- Hamza Mesrar - [@ez7mz](https://hmesrar.netlify.app/)

---
**Disclaimer:** This application is for educational and research purposes only. Stock predictions are not guaranteed and should not be used as the sole basis for investment decisions. Always do your own research and consult with financial advisors before making investment choices.
