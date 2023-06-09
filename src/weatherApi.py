import requests


def getWeatherInfoResponse(apiURL, authorizationKey):
    url = apiURL
    headers = {
        'Authorization': authorizationKey
    }
    return requests.get(url, headers=headers)


def getResponseInJsonFormat(responseParam):
    return responseParam.json()


def print_response(responseParam):
    print("Response data :" + str(responseParam))


def get_response_code(responseParam):
    return responseParam.status_code


def verify_status_code(country):
    print("Response code :" + str(get_response_code(country)))
    assert get_response_code(country) == 200, "Status code is not matched"


def get_country_code(responseParam):
    data = responseParam
    country_code = data['sys']['country']
    return country_code


def verify_country_code(responseParam, code):
    if get_country_code(responseParam) == "GB":
        print("Country :" + get_country_code(responseParam))
        assert get_country_code(responseParam) == code, "Country code is not matched"


def log_temperature_Information(responseParam, country, code):
    data = responseParam
    temp_kelvin = data['main']['temp']
    if country == "Tel-Aviv":
        verify_country_code(responseParam, code)
        temp_celsius = temp_kelvin - 273.15
        print("Temperature in Tel-Aviv (Celsius):", temp_celsius)
    else:
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        print("Temperature in " + country + " (Fahrenheit):", temp_fahrenheit)
    print()
