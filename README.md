# DME

This project is to simulate the analysis of DME pulses. The pulses are measured relative to an unsynchronized clock. The program will take in 4 numbers representing the time(in us) of the received pulse. The first two pulses are the transmitted pulses. For example, consider the following pulse timings.

1862 1874 2024 2036

The spacing for the transmitted pulse is 1874-1860 = 12 us.
The spacing between the received pulses is 2036--2024 = 12us
This is a valid channel X transmission.
The time between when the first pulse was transmitted and received is 2024-1862 = 162us
This can be converted to distance by (162 – 50)/12.36 = 9.06 nmi.

TASK: Create a program that takes in the time of 4 pulses.
If correct pulses for channel X are detected the system will print
Channel is X, distance is dd.d nautical miles. Where dd.d is the correct distance such as 12.2.
If correct pulses for channel Y are detected the system will print
Channel is Y, distance is dd.d nautical miles. Where dd.d is the correct distance such as 12.2.
If the system receives a valid pulse spacing for the X channel when transmitting on the Y channel or vice versa, this means that we have received pulses from an aircraft other than our own. In this case the system will print
FRUIT detected.
if the measured time between the transmitted and received pulses exceeds 200 nmi than the system will print
Channel is X, no reply. or Channel is Y, no reply. depending on the channel.
If incorrect pulses spacings for channel X or Y are detected or if the received signals arrive in less than the built-in delay of the ground station print
Signal Garbled.

Example:

> > DME(572,584,772,784)
> > Channel is X, distance is 12.14 nm.
