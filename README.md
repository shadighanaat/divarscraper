# Persian Car Price Scraper

This project is a tool that scrapes car price information for Peugeot 206 vehicles in Isfahan province, Iran, from the website divar.ir. The tool uses Python technologies, with `requests` for making HTTP requests, `BeautifulSoup` for parsing HTML, and `bidi.algorithm` and `arabic_reshaper` for processing and displaying Persian text.

## Prerequisites

Before running the project, make sure the following libraries are installed:

- requests
- beautifulsoup4
- arabic_reshaper
- python-bidi

You can install these libraries using the following command:

```bash
pip install requests beautifulsoup4 arabic_reshaper python-bidi

How to Use

    Clone the project.

    Run the file 3.py.

    Once executed, the Peugeot 206 car prices in Isfahan province will be displayed.

The convert function is used to convert Persian text into a format that can be displayed correctly in environments that do not support right-to-left languages.
Example Output:

Buying and selling prices for Peugeot 206 cars in Isfahan province, model years 1395 to 1402.
...

Project Description

This project is designed for people who want to automatically scrape real-time car prices for specific models from the Divar website. The extracted information can be used for further analysis or displayed as a report.
Contribution

If you want to contribute to the project or add new features, please submit a pull request or create issues and share your suggestions.
License

This project is licensed under the MIT License.

