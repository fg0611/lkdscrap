# 🚀 LinkedIn Web Scraping Project

This project extracts job opportunities from LinkedIn using Python and Selenium. It simulates human browsing by performing scrolling and random timeouts, leveraging various Selenium options to achieve its goal.

💡 **Tip:** I recommend using Anaconda for easier setup. This project is developed on Windows 11 with Python 3.9.21.

A Jupyter notebook is included for data wrangling to filter and sort positions. This project is still under construction, and more features will be added.

## 🛠️ Setup Instructions

```bash
# Create a Python 3.9.21 virtual environment named linkedin_scrapper
conda create --name linkedin_scrapper python=3.9.21

# List all conda environments
conda env list

# Activate the virtual environment
conda activate linkedin_scrapper

# Install required libraries
pip install -r requirements.txt
```

Navigate to the project root directory and run the following command with the environment active:

```bash
python main.py
```


MIT License

Copyright (c) 2025 Francisco Garrido

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.