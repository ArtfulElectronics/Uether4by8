A Wooden Mechanical Keyboard
============================

This project is about building split mechanical keyboards out of **wood**, including the circuit board and the keycaps.

![The Finished Keyboard](images/final.png)

 1. Unlike a true split keyboard with two microcontrollers communicating wirelessly, we use only one microcontroller and connect the two parts using the common 8P8C connector (also known as RJ-45, the Ethernet jack, hence the name). This choice eliminates potential delay of wireless communication between the main half and the secondary half of the keyboard, on top of saving costs.

 2. The keyboard has 32 keys in total (16 keys on each half), wired in a 4-by-8 matrix (hence the name). Physically, they are laid out similar to the [Corne keyboard](https://github.com/foostan/crkbd), except with one fewer column and less thumb keys.

 3. Another goal is to redesign the typing experience. With only 32 keys (one third of a typical full layout keyboard), we must make use of several advanced *firmware features* not commonly found in a typical commercial keyboard such as multi-layers, home row mods, etc. With ten keys less than the Corne, we need to alter the key mapping for optimal daily usage.

 4. Both wired (running QMK, RP2040 MCU) and wireless (running ZMK, nRF52840 MCU) designs are available.

The Keymap
----------

The default layer features the most common keys, namely the letters (a-z), space/backspace (also functions as layers switching keys), enter and escape.

![The Default Layer](images/default_layer.png)

Some notes:

 1. We use Auto Shift feature (a shifted key e.g. capital letter is output when the key is pressed and hold a little bit before being released, a quick tap and release output the regular key) to avoid having to hold Shift keys.

 2. Unlike standard [home row mods](https://precondition.github.io/home-row-mods) practice, we could skip one of the Alt/GUI key since we do not need to use them that often. Also, try to avoid putting them on letter keys ... since Auto Shift won't work for those keys then. (In fact, the only use for Alt is to switch applications with Alt + Tab so we could well put this in place of Tab.)

The first and second layers are complimentary. Their keys could form a single layer but split into two to avoid hitting the two keys with the same hand (the layer switching key and another key on the same half).

The keys here are the numbers, symbols and some other useful keys such as Print Screen, F5.

![The First Layer](images/first_layer.png)
![The Second Layer](images/second_layer.png)

Note that Auto Shift remains working on all layers. So we could type the `!` symbol by holding the `[LT2]` key (to activate the layer 2), then press and hold the `1` key just a bit longer. No home row mods is necessary on these layers (unless you need to Ctrl / Alt them).
