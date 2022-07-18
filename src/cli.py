import argparse
import logging
from model import RequestException, ValidationException, AttemptException, process_data


def main():
    parser = argparse.ArgumentParser(
        prog="Country Holidays", description="Check country holidays"
    )
    parser.add_argument(
        "-cc",
        "--country_code",
        type=str,
        help="'de' for Germany next 5 holidays",
        required=True,
    )
    args = parser.parse_args()

    if len(args.country_code) != 2:
        logging.error(
            "Country code must have two characteres. Eg: 'us' for United States next 5 country holidays"
        )
        exit(1)

    process_data(args.country_code)


if __name__ == "__main__":
    try:
        main()
    except ValidationException as e:
        logging.error(e)
    except RequestException as e:
        logging.error(e)
    except AttemptException as e:
        logging.error(e)
    except Exception as e:
        logging.exception(e)
