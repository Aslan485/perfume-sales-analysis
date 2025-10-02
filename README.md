# 🛍️ E-commerce Perfume Sales Analysis

Comprehensive data analysis of mens perfume sales from eBay marketplace. This project demonstrates advanced data analysis techniques, business intelligence reporting, and actionable insights for e-commerce optimization.

## 📊 Features
- **Business Metrics**: Total revenue, sales volume, and pricing analysis
- **Brand Performance**: Ranking and efficiency scoring of top brands
- **Price Segmentation**: Budget, Mid-Range, Premium, and Luxury segment analysis
- **Inventory Efficiency**: Stock turnover rates and optimization insights
- **Sales Velocity**: Products with highest sales per dollar
- **Market Share Analysis**: Product category performance and dominance

## 🛠️ Technologies Used
- **Python 3.8+** - Core programming language
- **Pandas 2.3.2** - Data manipulation and analysis
- **NumPy 1.26.4** - Numerical computations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository
```bash
git clone https://github.com/Aslan485/perfume-sales-analysis.git

Install dependencies

bash
pip install -r requirements.txt

Run the analysis

bash
python perfume_analysis.py

📈 Analysis Components
Key Performance Indicators
Total Sales Volume: 761,669 units

Total Revenue: $25.8M+

Average Price: $46.48

Brand Diversity: 246 unique brands

Business Insights
Price Segments: Mid-Range ($21-50) dominates with 70% of sales

Product Categories: Eau de Toilette represents 73.4% market share

Inventory Efficiency: 98%+ efficiency across top products

Sales Correlation: Negative correlation (-0.085) between price and volume

Top Performing Brands
Calvin Klein: 97,572 units sold

Versace: 96,519 units sold

Davidoff: 54,944 units sold

Azzaro: 38,305 units sold

Armaf: 24,282 units sold

🎯 Business Use Cases
This analysis can be used for:

Pricing Strategy Optimization

Inventory Management Decisions

Brand Performance Evaluation

Market Trend Identification

Sales Forecasting

Product Portfolio Analysis

👨‍💻 Author
Aslan Akhundov - Data Analyst

GitHub: Aslan485

Email: axundovaslan44@gmail.com

Skills: Python, Pandas, SQL, Data Analysis, Business Intelligence

📁 Project Structure
text
perfume-sales-analysis/
├── perfume_analysis.py     # Main analysis code
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
🔧 Customization
Adding New Analysis
Modify the analysis functions in perfume_analysis.py:

python
def analyze_new_metric(df):
    # Add your custom analysis here
    return new_insights
Modifying Price Segments
Update the price segmentation logic:

python
def get_price_segment(price):
    if price <= 25: return 'Budget'
    elif price <= 75: return 'Mid-Range'
    # Customize thresholds as needed
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Pandas community for robust data analysis tools

NumPy team for numerical computation capabilities

eBay marketplace for the sales data

⭐ If you find this project helpful, please give it a star!
🔗 Useful Links
Pandas Documentation

NumPy Documentation

Python Data Analysis Tutorials

📞 Support
If you have any questions or need help with setup, please open an issue on GitHub or contact the author directly.

Happy Analyzing! 📊🚀
