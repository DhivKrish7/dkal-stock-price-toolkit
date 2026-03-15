# DKAL – Stock Price Toolkit

DKAL is a lightweight stock price calculator designed to help investors quickly estimate **break-even prices, trading costs, and profitability** when buying and selling stocks. The tool is especially useful for investors, traders and stock brokers who want a **fast desktop calculator** without opening spreadsheets or complex trading platforms to calculate manually.

## Features
* Break-even price calculator for stock purchases
* Automatic calculation of trading commissions
* Simple and fast desktop interface
* Portable `.exe` version (no installation required)
* Built using Python

## Screenshot
```
(space for screenshot - need to upload)
```

## How It Works
The calculator estimates the **minimum selling price required to avoid a loss** after accounting for trading commissions.

Typical calculation flow: Enter **buy price** and DKAL calculates the **break-even selling price**

## Installation

### Option 1 — Download Executable
Download the latest `.exe` from the **Releases** section.
Run:
```
dkal.exe
```
No Python installation required.

### Option 2 — Run from Source
Clone the repository:
```
git clone https://github.com/DhivKrish7/dkal-stock-price-toolkit.git
cd dkal
```
Create virtual environment:
```
python -m venv venv
```
Activate environment:
Windows:
```
venv\Scripts\activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the application:
```
python dkal.py
```

## Project Structure
```
dkal/
│
├── dkal.py            # Main application
├── dkal.spec          # PyInstaller build configuration
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

## Build Executable
To generate the portable `.exe`:
```
pyinstaller dkal.spec
```
Output file will appear in:
```
dist/dkal.exe
```

## Use Case

DKAL helps traders, investors and stock brokers quickly answer questions like:
* What price must I sell at to break even?
* How much commission am I paying?
* How much profit will I make after fees?

## Future Improvements

Planned upgrades:
* Profit calculator
* Loss calculator
* Position sizing tool

## Author
Developed by **Dhivyarajan K' Yozhandren**, Financial Engineering Undergraduate, University of Colombo. Interested in building **financial tools, fintech systems, and algorithmic trading infrastructure**.

## License
This project is open source and available under the **MIT License**.
