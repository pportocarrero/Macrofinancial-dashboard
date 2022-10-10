[![affine.pro](https://img.shields.io/static/v1?label=live%20demo&logo=github,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAhpJREFUWEdjZEACtnl3MxgY/0YzMjAaMzAwcCLLUYH9/T/D/7MM/5mXHp6kPANmHiOI4Zx9Xfg3C+tKBob/zlSwiAgjGPey/vkdvneq5luwA+zy7+yhn+Vwv+89NFHFhREU7IyM/6YT4WyqK/n/nymT0Tb/1mFGBkYbqptOhIH/Gf4fYbTLv/2NBgmOCOvBSr6DHPCfWNW0UEe2A2x1uRlakiXBbtpx6jND+7KXZLmPbAdURokzeJjxwi31rrzH8OX7P5IdQbYDtnUoMXBzMMEt7Fj2imH7qU/0cQBy8MNsPHL5K0P13Of0cQB68MNsJScaSI4CHk4mhq3tSnCf3n36k0FZmh3Mn7L+DcPqgx9ICgWSHeBpxsdQESUGtgRk+eqDH+H8O09/MiR3P6atA1qTJRlsdLnhPgYlPOQQCW96wPDi3R+iHUFSCKAHP8wydEeREg0kOQA9+JOgwR1qL8CQEygC9jWp0UCSA+aVysIT3JqDHxgmr38DtlRCiIVhZZ0CPNhB6QDkEGIA0Q4gZAkuxxFyBNEOQA7ml+/+MIQ1PUAxG1kelAhB6YMYQLQDCPmQUAjhcgxRDiDWcEKOxOYIohyQGyjCEGIvANaPLfhhBiNHA6hmBBXNhABRDgCV/aBQAAFQpYMrn4PUgNTCACiXEMoNRDmAkC8okR8UDhjYRumAN8sHvGMCSkAD2jUDOWDAO6ewbDQQ3XMAy/oxKownQR0AAAAASUVORK5CYII=&color=orange&message=→)](https://macrofinancial-dashboard.streamlitapp.com/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/pportocarrero/Macrofinancial-dashboard)](https://github.com/pportocarrero/Macrofinancial-dashboard/releases)
[![See recent changes](https://img.shields.io/badge/changelog-See%20recent%20changes-blue)](https://github.com/pportocarrero/Macrofinancial-dashboard/compare/v0.0.7-alpha...v0.0.1-beta)

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
