import csv
import json
from pyramid.config import Configurator
from pyramid.response import Response
import codecs

def hello(request):
    return Response('Hello World!')

def benford(request):
    # get the uploaded CSV file
    csv_file = request.POST['csv_file'].file
    print(csv_file)
    # parse the CSV file and extract the first digit of each number
    first_digits = []
    csv_reader = csv.reader(codecs.iterdecode(csv_file, 'utf-8'))
    for row in csv_reader:
        first_digit = int(str(row[0])[0])
        first_digits.append(first_digit)
    

    # calculate the expected frequencies based on Benford's Law
    expected_freq = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

    # calculate the actual frequencies
    actual_freq = []
    for i in range(1, 10):
        count = first_digits.count(i)
        freq = count / len(first_digits)
        actual_freq.append(freq)

    # check if the actual frequencies conform to Benford's Law
    is_conform = True
    for i in range(0, 9):
        if abs(expected_freq[i] - actual_freq[i]) > 0.02:
            is_conform = False
            break

    # prepare the response JSON
    response_data = {'is_conform': is_conform, 'actual_freq': actual_freq}
    with open('benford_result.json', 'w') as outfile:
        json.dump(response_data, outfile)

    return Response(json.dumps(response_data))

# create the Pyramid web application
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello, route_name='hello')
        config.add_route('benford', '/benford')
        config.add_view(benford, route_name='benford', renderer='json')
        app = config.make_wsgi_app()
        from wsgiref.simple_server import make_server
        server = make_server('0.0.0.0', 6543, app)
        server.serve_forever()
