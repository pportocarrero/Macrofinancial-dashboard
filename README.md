[![GitHub release (latest by date)](https://img.shields.io/github/v/release/pportocarrero/Macrofinancial-dashboard)](https://github.com/pportocarrero/Macrofinancial-dashboard/releases)
[![See recent changes](https://img.shields.io/badge/changelog-See%20recent%20changes-blue)](https://github.com/pportocarrero/Macrofinancial-dashboard/compare/v0.0.2-alpha...v0.0.3-alpha)

# Macrofinancial Dashboard

This is a dashboard showing information of the main macroeconomic and financial indicators. Additionally, it displays financial news and macrofinancial information for United States and Peru (I work in Peru and need to follow it).

# What's next

The dashboard is far from over, in the following weeks, I will be making several improvements and add new features:

- More indicators related to United States (macroeconomic, financial, and public finance indicators).
- More indicators for Peru (macroeconomic, financial, and public finance indicators).
- Relevant financial news.

# Instructions
This dashboard has been developed using the multipage streamlit platform. Currently, you only need to run the 01_Start.py file. Eventually, this repository will include all the code to automatically update all information. First, you need to install the streamlit library.


```bash
pip install streamlit
```

The scripts that retrieve the information are coded to work on Windows or Mac computers.

For now, open a prompt from your Anaconda Navigator, PowerShell prompt, or terminal and navigate to the folder containing this repo, then run the following:

```bash
streamlit run Dashboard.py
```

# Sources
Data is taken from official sources such as the Federal Reserve Bank of St. Louis, the Federal Reserve Bank of New York, the Ministry of Economy and Finance of Peru, the Central Reserve Bank of Peru, Yahoo! Finance and Alpha Vantage. I don't own any of this information, I am just consolidating it as a way to better analyze macrofinancial information.

# Authors
Main development has been done by me. Many thanks to @capm for his help and feedback. If you have questions or comments, please contact me (see my contact info on my github profile).
