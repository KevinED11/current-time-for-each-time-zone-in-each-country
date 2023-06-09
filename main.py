import datetime


import pytz


def get_all_available_countries() -> dict[str, str]:
    return dict(pytz.country_names)


def delete_countries_with_no_timezone(countries: dict[str, str],
                                      countries_code: list[str] = ["BV", "HM"]) -> list[str]:
    return [countries.pop(country_code) for country_code in countries_code if country_code in countries]


def get_all_countries_as_tupple(countries: dict[str, str]) -> list[tuple[str, str]]:
    return list(countries.items())


def get_time_zones(countries: dict[str, str]) -> list[list[str]]:
    return [pytz.country_timezones(country_code) for country_code in countries.keys()]


def get_time_zones_for_each_country(countries: dict[str, str] | list[tuple[str, str]]) -> dict[str, list[str]]:
    if isinstance(countries, list):
        countries = dict(countries)
    return {country_code: {"timezones": pytz.country_timezones(country_code)} for country_code in countries.keys()}


def get_the_current_time_for_each_time_zone_in_each_country(time_zones: dict[str, list[str]],
                                                            countries: list[str] | None = None) -> dict[str, dict[str, str]]:
    time_zones_countries:  dict[str, dict[str, str]] = {}
    for country_code in time_zones.keys():
        time_zones_countries[country_code] = {time_zone: datetime.datetime.now(pytz.timezone(
            time_zone)).strftime("%H:%M:%S") for time_zone in time_zones[country_code]["timezones"]}

    if isinstance(countries, list) and countries:
        filtered: dict[str, dict[str, str]] = {country_code: time_zones_countries[country_code]
                                               for country_code in countries if country_code in time_zones_countries}

        if not filtered:
            raise ValueError(
                "No se encontraron países con esos códigos proporcionados")

        return filtered

    return time_zones_countries


# all_countries = dict(pytz.country_names)
# print(all_countries)


# all_countries.pop("BV")
# all_countries.pop("HM")


# all = {}
# for zona, name_pais in all_countries.items():
#     timezones = pytz.country_timezones(zona)
#     all[name_pais] = {"Zonas horarias": timezones, "hora por zona horaria": {
#         zona: datetime.datetime.now(pytz.timezone(zona)).strftime("%H:%M:%S") for zona in timezones}}
# print("\nCADA PAIS CON SUS RESPECTIVAS ZONAS HORARIAS")
# print(all)


# print("\n")
# print(list(all_countries.values()))

# print("\nZONAS HORARIAS DEL PAIS ELEGIDO")
# print(all["United States"])


def main() -> None:
    available_countries: dict[str, str] = get_all_available_countries()
    delete_countries_with_no_timezone(
        available_countries, countries_code=["BV", "HM"])
    countries = get_all_countries_as_tupple(available_countries)
    timezones = get_time_zones_for_each_country(countries)
    print(get_the_current_time_for_each_time_zone_in_each_country(
        time_zones=timezones, countries=["MX", "AR"]))


if __name__ == "__main__":
    main()
