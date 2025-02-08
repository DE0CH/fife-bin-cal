# Fife Council Bin Calendar Look-up

A tool that looks up the Fife Council's bin collection dates.

## Motivation

Inspired by https://github.com/wupr/fife-bin-cal. It directly using the API for the Fife Bin Calendar.

The author found the Fife Council's bin calendar [search tool](https://www.fife.gov.uk/services/forms/bin-calendar) annoying to use.
Usually, one needs to visit the webpage in a browser, enter the postcode, click search, select the address from a list, and wait for the table of collection dates to load.
The URL of the webpage is never updated, so bookmarking does not help.

## Usage

### Installing dependencies

1. Install python
1. Install dependencies.
    ```sh
    python3 -m pip install -r requirements.txt
    ```

### Running

Clone this repository and run
```sh
python3 main.py <postcode> <number>
```

The script `main.py` takes two positional arguments.
The second argument `<number>` is the part of the address before the first comma, as displayed when using the look-up webpage.
Usually it is the house number.

For example, running
```sh
python3 main.py 'KY16 9AJ' 'College Gate'
```
resulted in the following output on 2025-02-08:
```text
{
  "data": {
    "results_returned": "true",
    "tab_collections": [
      {
        "colour": "Blue",
        "date": "Tuesday, February 18, 2025",
        "type": "Landfill / Blue Bin"
      },
      {
        "colour": "Blue",
        "date": "Tuesday, March 4, 2025",
        "type": "Landfill / Blue Bin"
      },
      {
        "colour": "Blue",
        "date": "Tuesday, March 18, 2025",
        "type": "Landfill / Blue Bin"
      },
      {
        "colour": "Blue",
        "date": "Tuesday, April 1, 2025",
        "type": "Landfill / Blue Bin"
      }
    ]
  },
  "action": "powersuite_bin_calendar_collections",
  "actionedby": "bin_calendar",
  "loadform": true,
  "links": [
    {
      "rel": "self",
      "href": "https://www.fife.gov.uk/api/custom?access=citizen&action=powersuite_bin_calendar_collections&actionedby=bin_calendar&loadform=true&locale=en"
    }
  ]
}
```
