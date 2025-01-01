from pythonosc.dispatcher import Dispatcher
from typing import List, Any

dispatcher = Dispatcher()



def set_note(address: str,  *args: List[Any]) ->  None:

    print(f"arguments supplied (#{len(args)}): {type(args[0])}")
    print(f"address: {address}")
    print(f"value: {args[0]}")

    urls = address.split('/')
    print(urls)

    if len(urls) == 4 and urls[1] == "0" and urls[2] == "dmx":
        channel = urls[3]
    else:
        print(f"address not parsed: {address}")
        return

    print(f"channel: {channel}")

    charval = int(255.0 * args[0])
    print(f"val to midi: {charval}")
    # We expect two float arguments
    if not len(args) == 2 or type(args[0]) is not float or type(args[1]) is not float:
        return

    # Check that address starts with filter
    if not address[:-1] == "/filter":  # Cut off the last character
        print(f"filter address? {address[:-1]}")
        return

    value1 = args[0]
    value2 = args[1]
    filterno = address[-1]
    print(f"Setting filter {filterno} values: {value1}, {value2}")

print("Running Osc2Midi")

dispatcher.map("/0/dmx/*", set_note)

from pythonosc.osc_server import BlockingOSCUDPServer

server = BlockingOSCUDPServer(("192.168.68.61", 9000), dispatcher)
server.serve_forever()
