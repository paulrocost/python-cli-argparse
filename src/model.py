from dataclasses import dataclass, field
import datetime as dt
import json
import os
import api as api


COUNTRY_CACHE = "countries_cache.txt"
HOLIDAY_CACHE = "holiday_cache.txt"


#  Exceptions
class ValidationException(Exception):
    pass


class RequestException(Exception):
    pass


class AttemptException(Exception):
    pass


#  Models
@dataclass
class CountryHoliday:
    date: str
    name: str
    counties: "list[str]" = field(default_factory=list)
    types: "list[str]" = field(default_factory=list)


@dataclass
class CountryHolidayRegister:
    created_at: str
    country_holiday_list: "list[CountryHoliday]" = field(default_factory=list)


#  Business logic
def __create_available_countries_cache_file() -> None:
    data_list = api.get_available_countries()
    data_list.insert(0, {"created_at": str(dt.datetime.now())})
    with open(COUNTRY_CACHE, "w") as wf:
        json.dump(data_list, wf)


def __read_available_countries_cache_file() -> dict:
    if not os.path.exists(COUNTRY_CACHE):
        __create_available_countries_cache_file()
    with open(COUNTRY_CACHE, "r") as rf:
        return json.load(rf)


def __fetch_data_when_expires(data_list):
    created_at_str = data_list[0]
    created_at_dt = dt.datetime.strptime(
        created_at_str.get("created_at"), "%Y-%m-%d %H:%M:%S.%f"
    )
    if created_at_dt < (dt.datetime.now() + dt.timedelta(days=-1)):
        __create_available_countries_cache_file()


def __is_available_country(country_code) -> bool:
    data_list = __read_available_countries_cache_file()
    __fetch_data_when_expires(data_list)
    for item in data_list[1:]:
        if item.get("countryCode") == country_code.upper():
            return True
    return False


def __map_data_to_object(data_list):
    country_holiday_list = []
    for item in data_list:
        country_holiday_list.append(
            CountryHoliday(
                name=item.get("name"),
                date=item.get("date"),
                counties=item.get("counties"),
                types=item.get("types"),
            ).__dict__
        )
    register = CountryHolidayRegister(
        created_at=str(dt.datetime.now()), country_holiday_list=country_holiday_list
    )

    return register


def __create_country_holiday_cache_file(country_code) -> None:
    data_list = api.get_country_following_holidays(country_code)
    register = __map_data_to_object(data_list)
    with open(HOLIDAY_CACHE, "w") as wf:
        json.dump(register.__dict__, wf)


def __read_country_holiday_cache_file() -> str:
    if not os.path.exists(HOLIDAY_CACHE):
        return None
    with open(HOLIDAY_CACHE, "r") as rf:
        return rf.read()


def __check_attempts(data_list) -> None:
    if data_list:
        json_data = json.loads(data_list)
        created_time = json_data.get("created_at")
        date_time_obj = dt.datetime.strptime(created_time, "%Y-%m-%d %H:%M:%S.%f")
        if date_time_obj > (dt.datetime.now() + dt.timedelta(days=-1)):
            raise AttemptException(
                f"Last request less than one day, last request time: {created_time}."
            )


def __add_holiday_record(country_code) -> str:
    data_list = __read_country_holiday_cache_file()
    __check_attempts(data_list)
    __create_country_holiday_cache_file(country_code)
    return __read_country_holiday_cache_file()


def process_data(country_code) -> None:
    if not __is_available_country(country_code):
        raise RequestException(
            f"The country code, {country_code.upper()}, has no holidays available data."
        )
    record = __add_holiday_record(country_code)
    if record:
        json_data = json.loads(record)
        print(json.dumps(json_data, indent=4))
