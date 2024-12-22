"""
Generates performance reports for your stock portfolio.
"""
import argparse
import csv
from collections import OrderedDict
import requests


def main():
    """
    Entrypoint into program.
    """
  


def read_portfolio(filename):
    """
    Returns data from a CSV file
    """
    with open(filename, newline='') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        return data


def get_args(args=None):
    """
    Parse and return command line argument values
    """
    


def get_market_data(stocks_list):
    """
    Get the latest market data for the given stock symbols
    """
    


def calculate_metrics(input_file, market_data):
    """
    Calculates the various metrics of each of the stocks
    """
    


def save_portfolio(output_data, filename):
    """
    Saves data to a CSV file
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, ['symbol', 'units', 'cost'])
        writer.writeheader()  # Write the header
        writer.writerows(output_data)  # Write all the rows at once


if __name__ == '__main__':
    main()
