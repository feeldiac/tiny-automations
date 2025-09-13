# Tiny automations

This projects aims to improve some small (and initially personal) daily processes.

## Discord greetings

The main objective of this automation is to avoid me to enter to my job's discord and say good morning or whatever.

For now, this automation get all open windows, use a keyword (hardcoded) to get the correct Discord window, then takes a dynamic message copy it to the clipboard, paste it into the selected (active) window and send the message using `enter`.

The following are some aspects that I want to improve in the future:

1. Not use hardcoded keyword for getting the Discord window.
2. Customize the message to change the greeting depending not just in the day of the week, but also in the current time.
3. Programmatically open Discord (now it <em>have to be</em> open).
4. Not just send sentences, but also send gifs.