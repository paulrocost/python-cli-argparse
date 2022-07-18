## Country Holiday Cli

Python CLI which fetchs the following 5 holidays from a country, based on its country code.

#### Premises

- Return the next 5 country holidays from now on.
- country code is a required argument. Eg:. DE for Germany country code.
- It's allowed to fetch the respective data once a day.

#### Goal

- Retrieve the next 5 holidays of your choose country, once a day

#### Usage

Input:

```
#  The command below will retrieve the following 5 holidays from Germany.
python src/cli.py --cc de
```

Output:

```
{
    "country_holiday_list": [
        {
            "counties": [
                "DE-SL"
            ],
            "date": "2022-08-15",
            "name": "Assumption Day",
            "types": [
                "Public"
            ]
        },
        {
            "counties": [
                "DE-TH"
            ],
            "date": "2022-09-20",
            "name": "World Children's Day",
            "types": [
                "Public"
            ]
        },
        {
            "counties": null,
            "date": "2022-10-03",
            "name": "German Unity Day",
            "types": [
                "Public"
            ]
        },
        {
            "counties": [
                "DE-BB",
                "DE-MV",
                "DE-SN",
                "DE-ST",
                "DE-TH",
                "DE-HB",
                "DE-HH",
                "DE-NI",
                "DE-SH"
            ],
            "date": "2022-10-31",
            "name": "Reformation Day",
            "types": [
                "Public"
            ]
        },
        {
            "counties": [
                "DE-BW",
                "DE-BY",
                "DE-NW",
                "DE-RP",
                "DE-SL"
            ],
            "date": "2022-11-01",
            "name": "All Saints' Day",
            "types": [
                "Public"
            ]
        }
    ],
    "created_at": "2022-07-18 14:57:56.879437"
}

```
