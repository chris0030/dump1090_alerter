# Dump1090 Alerter

## About The Project

This project is designed to trigger alerts on aircraft from Dump1090.
Currently it's set to alert if an aircraft is squawking 7001 for low-level flying,
or under 2000ft altitude. An aircraft can only trigger these alerts if it's inside
a defined bounding box.

Alerts are sent to Pushover and can be push notifications on IOS, Android, or desktop.

### Built With

* [Python](https://python.org)

<!-- GETTING STARTED -->
## Getting Started

Following are instructions to get a development environment up and running

### Installation

1. Copy config.template to config.py `cp config.template config.py`

1. Fill in the missing items, you'll need a [Pushover](https://pushover.net/) account

1. Install the requirements `pip install -r requirements.txt`

1. Run the app with `python3 app.py`

## Roadmap

See the [open issues](https://github.com/chris0030/dump1090_alerter/issues) for a list
of proposed features (and known issues).

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Chris - chris0030@pm.me

Project Link: [https://github.com/chris0030/dump1090_alerter](https://github.com/chris0030/dump1090_alerter)
