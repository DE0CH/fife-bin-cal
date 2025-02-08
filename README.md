# Fife Council Bin Calendar Look-up

A tool that looks up the Fife Council's bin collection dates.

## Motivation

The author found the Fife Council's bin calendar [search tool](https://www.fife.gov.uk/services/forms/bin-calendar) annoying to use.
Usually, one needs to visit the webpage in a browser, enter the postcode, click search, select the address from a list, and wait for the table of collection dates to load.
The URL of the webpage is never updated, so bookmarking does not help.

The code in this repository automates the process using [Playwright](https://playwright.dev).

## Usage

### Installing dependencies

1. Install [Node.js](https://nodejs.org/).
1. Install dependencies.
    Using npm, one can run:
    ```sh
    npm install
    ```
    You may need to install some system dependencies.
    See also [official instructions](https://playwright.dev/docs/intro), which uses npm.

### Running

Clone this repository and run
```sh
npx ts-node main.ts <postcode> <number>
```

The script `main.ts` takes two positional arguments.
Both arguments are case-insensitive.
The second argument `<number>` is the part of the address before the first comma, as displayed when using the look-up webpage.
Usually it is the house number.

For example, running
```sh
npx ts-node main.ts 'KY16 9AJ' 'College Gate'
```
resulted in the following output on 2025-02-08:
```text
Submitted postcode 'KY16 9AJ'.
Selected address 'College Gate, North Street, St Andrews, Fife, KY16 9AJ'.
18/02/2025      Landfill / Blue Bin
04/03/2025      Landfill / Blue Bin
18/03/2025      Landfill / Blue Bin
01/04/2025      Landfill / Blue Bin
```

With a good Internet connection, this should take less than 10 seconds to run.

The first two lines are printed to stderr. The rest is printed to stdout, with a tab separating the date and the bin type in each line.

## License

The source code of this tool is distributed under the terms of Apache License, Version 2.0.
See [LICENSE](LICENSE) for details.
