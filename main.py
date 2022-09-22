def parse(query: str) -> dict:
    query = query.split('?')
    if len(query) > 1:
        return dict(i.split('=') for i in query[1].split('&') if '=' in i)
    return {}


# print(parse('https://example.com/path/to/page?name=ferret&color=purple'))
# print(parse('https://example.com/path/to/page?name=ferret&color=purple&'))
# print(parse('http://example.com/'))
# print(parse('http://example.com/?'))
# print(parse('http://example.com/?name=Dima'))
if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    if len(query):
        return dict(i.split('=', 1) for i in query.split(';') if '=' in i)
    return {}


# print("------------------------------")
# print(parse_cookie('name=Dima;'))
# print(parse_cookie(''))
# print(parse_cookie('name=Dima;age=28;'))
# print(parse_cookie('name=Dima=User;age=28;'))
if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
