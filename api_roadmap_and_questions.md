# API Road Map and Questions as I build this Countdown App

#### Current API Implementation
- API_PATH = localhost:5000

- POST #{API_PATH}/countdown
- with the following payload:

```
{
    "title": "Number of Days Left till Ada Capstone",
    "countdown_till_date": "2021-07-30T13:34:00.000"
}
```

#### Produces the following response:
- "Countdown Event:  Number of Days Left till Ada Capstone succesfully created."
- "Countdown Event: {countdown.title} succesfully created."

<hr>

## Things I'm considering as I build this API:

1. what sort of format is it best to collect DateTime data in my API ? 
would it be helpful to return a response to the user of API with any of the following attributes:
    - weeks till date
    - days till date
    - minutes till date
    - seconds till date ?
That way the view layer can simply focus on displaying these attributes. If they are present.

2. Should I instead break up the saving of DateTime into chuncks? Such that I could ask a user for YYYY, DD, MM. Not sure if doing it this way will be more problematic or less so. Since it would mean I could use attributes: year, month, day and I could give meaningful tight constraints upon this incoming data.
    - year (can only be 4 digits)
    - month (can only be 1 - 12)
    - day (can only be 1 - 31)

3. Need to think of some sort of action to happen when countdown has reached its end. 