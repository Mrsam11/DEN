# Coffee Shop Sales Analysis

## Objective
The objective of this project is to analyze the coffee shop sales dataset to evaluate product and service profitability. The analysis focuses on identifying profitable and loss-incurring products, forecasting profits, and proposing strategies to improve profit margins and reduce losses.

## Project Overview
This project covers the following tasks:
1. **Data Cleaning**:
   - Identified and handled missing values, duplicates, and outliers in the dataset.
   - Ensured data consistency and accuracy for further analysis.

2. **Profit/Loss Analysis**:
   - Calculated total sales, profit margins, and performed a detailed sales comparison.
   - Visualized product profitability and identified top-selling, least-selling, and low-margin products.
   
3. **Profit Increase Prediction**:
   - Applied ARIMA for forecasting future sales based on historical data.
   - Used predictive modeling (Linear Regression) to forecast total sales based on transaction quantities and unit prices.

4. **Loss Mitigation**:
   - Analyzed drivers of losses for specific products and developed strategies to mitigate these losses.
   - Proposed actionable strategies to boost profit margins and convert losses into profits.

## Dataset
The dataset includes the following columns:
- `transaction_date`: The date of the transaction.
- `product_detail`: Product or service name.
- `transaction_qty`: Quantity of products sold.
- `unit_price`: Price per unit.
- `total_sales`: Calculated by multiplying `transaction_qty` and `unit_price`.
- Additional features used for profit calculation and clustering.

## Key Insights
1. **Top-Selling Products**: Identified and visualized the top 10 selling products and their contribution to total sales.
2. **Least-Selling Products**: Highlighted the bottom 10 selling products and analyzed reasons for low sales.
3. **Profitability Analysis**: Used profit margins to evaluate the financial performance of each product.
4. **Sales Forecasting**: Forecasted future sales trends using ARIMA, helping in inventory management and sales strategy planning.

## Predictive Modeling
- Applied **Linear Regression** to predict total sales based on key features (e.g., transaction quantity, unit price).
- Used **K-Means clustering** for customer segmentation based on transaction data, helping to target marketing strategies.

## Inventory Turnover
Calculated inventory turnover to analyze how efficiently the inventory is managed for each product.

## Visualizations
- Bar plots for total sales, profit, and transaction quantities by product.
- Dual-axis plots to compare sales and profit trends.
- Scatter plots for customer segmentation using K-Means clustering.

## Tools and Libraries
- **Python**: Core programming language for data analysis and modeling.
- **Pandas & NumPy**: Data manipulation and numerical operations.
- **Matplotlib & Seaborn**: For creating insightful visualizations.
- **scikit-learn**: Machine learning algorithms (Linear Regression, K-Means).
- **ARIMA**: Time series forecasting model for sales predictions.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/coffee-shop-sales-analysis.git
   cd coffee-shop-sales-analysis
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis notebook or script to reproduce the results:
   ```bash
   python analysis_script.py
   ```

## Results
The analysis provides a comprehensive overview of sales and profitability, offering actionable insights for improving profit margins, reducing losses, and forecasting future trends.
