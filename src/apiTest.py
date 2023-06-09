import weatherApi
import testData

for i in range(len(testData.countries)):
    url = testData.url.replace("countryName", testData.countries[i].get("countryName"))

    weatherResponse = weatherApi.getWeatherInfoResponse(url, testData.apiKey)

    weatherResponseInJsonFormat = weatherApi.getResponseInJsonFormat(weatherResponse)

    weatherApi.print_response(weatherResponseInJsonFormat)

    weatherApi.get_response_code(weatherResponse)

    weatherApi.verify_status_code(weatherResponse)

    weatherApi.verify_country_code(weatherResponseInJsonFormat, testData.countries[i].get("countryCode"))

    weatherApi.get_country_code(weatherResponseInJsonFormat)

    weatherApi.log_temperature_Information(weatherResponseInJsonFormat, testData.countries[i].get("countryName"),
                                           testData.countries[i].get("countryCode"))
