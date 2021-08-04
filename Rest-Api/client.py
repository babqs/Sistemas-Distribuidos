import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)


# get all
def list ():
    response = requests.get('http://127.0.0.1:5000/freights/')
    return response.json()


# insert
def insert ():
    cep = input('Insert cep:')
    price = input('Insert price:')

    response = requests.post('http://127.0.0.1:5000/freights/', data={'cep': cep, 'price': price})
    return response.json()


# get single
def get_single ():
    index = input('Insert ID:')
    response = requests.get(f'http://127.0.0.1:5000/freights/{index}')
    return response.json()


# edit
def edit ():
    index = input('Insert ID:')
    price = input('Insert price:')
    response = requests.put(f'http://127.0.0.1:5000/freights/{index}', data={'price': price})
    return response.json()


# delete
def delete ():
    index = input('Insert ID:')
    response = requests.delete(f'http://127.0.0.1:5000/freights/{index}')
    return response


if __name__ == "__main__":
  # just uncomment to use a function

    # pp.pprint(list())
    # pp.pprint(insert())
    # pp.pprint(get_single())
    # pp.pprint(edit())
    # pp.pprint(delete())