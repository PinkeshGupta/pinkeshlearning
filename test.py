# def Add(Num1 , Num2):
#     return Num1 + Num2

# def sub(Num1 , Num2):
#     return Num1 - Num2

# def Mul(Num1 , Num2):
#     return Num1 * Num2

# def Div(Num1 , Num2):
#     return Num1 / Num2

# print("Select one operation to perform calculaion -\n" \
#       "1. Add -\n"\
#       "2. Subtract -\n"\
#       "3. Multiplication-\n"\
#       "4. Division \n")

# select = input("Select operator from 1 2 3 4 \n")
# if select > "4" or select<"1":
#     print("Please select correct input")
# else:
#     numb1 = int(input("Please enter First number \n"))
#     numb2 = int(input("Please enter Second  number \n"))


# if select =="1":
#     print(numb1,"+",numb2, "=",
#           Add(numb1,numb2))
# elif select =="2":
#     print(numb1, "-", numb2, "=",
#           sub(numb1, numb2))
# elif select =="3":
#     print(numb1, "*", numb2, "=",
#           Mul(numb1, numb2))

# elif select =="4":
#     print(numb1, "/", numb2, "=",
#           Div(numb1, numb2))
# else:
#     print("invalid Operator")












#!/usr/bin/env python3

"""A script for retrieving and parsing results from requests to
somewhere.com.

This script works as either a standalone script or as a library. To use
it as a standalone script, run it as `python3 scriptname.py`. To use it
as a library, use the `retrieve_terms` function."""

import urllib.request
import json
import sys

E_OPERATION_ERROR = 1
E_INVALID_PARAMS = 2

def parse_result(result):
    """Parse a JSONP result string and return a list of terms"""
    prefix = 'oo.visualization.Query.setResponse('
    suffix = ');'

    # Strip JSONP function wrapper
    if result.startswith(prefix) and result.endswith(suffix):
        result = result[len(prefix):-len(suffix)]

    # Deserialize JSON to Python objects
    result_object = json.loads(result)

    # Get the rows in the table, then get the second column's value
    # for each row
    return [row['c'][2]['v'] for row in result_object['table']['rows']]

def retrieve_terms(limit, seedterm):
    """Retrieves and parses data and returns a list of terms"""
    url_template = 'http://somewhere.com/relatedqueries?limit={limit}&query={seedterm}'
    url = url_template.format(limit=limit, seedterm=seedterm)

    try:
        with urllib.request.urlopen(url) as data:
            data = perform_request(limit, seedterm)
            result = data.read()
    except:
        print('Could not request data from server', file=sys.stderr)
        exit(E_OPERATION_ERROR)

    terms = parse_result(result)
    print(terms)

def main(limit, seedterm):
    """Retrieves and parses data and prints each term to standard output"""
    terms = retrieve_terms(limit, seedterm)
    for term in terms:
        print(term)

if __name__ == '__main__'
    try:
        limit = int(sys.argv[1])
        seedterm = sys.argv[2]
    except:
        error_message = '''{} limit seedterm

limit must be an integer'''.format(sys.argv[0])
        print(error_message, file=sys.stderr)
        exit(2)

    exit(main(limit, seedterm))














