# Create your event

## Step 1. Find the country folder

    /source/Japan

If there is no folder, then create one

    Copy the _event.yml template into the folder, rename it to \[eventname\].yml

## Step 2. Enter the details in the yml data file

One yml file is to be maintained per organiser / event series.  If you organise several events, but they have different event names, you can create one file for each.

In the yml file, follow the format of data sequences:

    country: jp
    city: osk

The country code is 2-letter ISO standard

The city code is 3-letter IATA airport code standard

Each data is a name followed by colon space and the data on the same line.

## Step 3. Enter the details for a year, e.g. 2020

The data for 2020 is tagged "y2020".  For 2021 is tagged "y2021".

    y2020:
      startdate:
      enddate:
      fbevent:

Put the start and end dates in YYYY-MM-DD format.

The fbevent should be a link to the event page.

