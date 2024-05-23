Base64 - encoding any binary data into text data consisting of the characters 0-64 matched with A-z
Protocols meant to transmit text and not byte streams, can lead to misinterpretation of data being transferred?? - interpretations of data from the protocol, certain characters are special and might mean something else to these applications. e.g Browser parsing HTML you just sent and actually rendering it. Data sent might be interpreted differently.
Transferability - converting every binary data to the predictable 64 known characters in its system.
