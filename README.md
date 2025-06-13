Flipkart Product Scraper and Analyzer
Overview
This Jupyter Notebook automates the process of scraping product information from Flipkart, a popular e-commerce platform in India. It fetches data such as product name, price, rating, and other details, and allows for basic analysis and visualization.
Features
- Web scraping using requests and BeautifulSoup
- Dynamic pagination handling to fetch multiple product pages
- Extraction of:
  - Product name
  - Price
  - Rating
  - Product URL
- Data cleaning and organization with pandas
- Visualization of data (e.g., price distribution, rating trends)
- Export to CSV
Dependencies
To run this notebook, ensure the following Python libraries are installed:

pip install pandas numpy requests beautifulsoup4 matplotlib seaborn
How to Use
1. Open the Notebook: Launch flipkart.ipynb in Jupyter Notebook or JupyterLab.
2. Enter a Search Term: Specify a product keyword (e.g., 'laptops', 'mobiles').
3. Run the Notebook Cells: Execute all cells sequentially to scrape, clean, and analyze the data.
4. View Output: Analyze the output in tabular or visual format.
5. Export Results: Download the scraped dataset in .csv format.
Output
The output includes:
- A clean pandas DataFrame of Flipkart product listings
- Plots showing:
  - Price distribution
  - Average ratings
- CSV export for further analysis
Notes
- Flipkart may block automated requests. Use time delays or rotating proxies if needed.
- The site structure may change, requiring updates to the scraping logic.
- This script is intended for educational and research purposes only.
File Structure
flipkart.ipynb       # Main Jupyter Notebook
README.docx          # Project documentation (this file)
