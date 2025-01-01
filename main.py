from pythonosc.dispatcher import Dispatcher
from typing import List, Any
from pythonosc.osc_server import BlockingOSCUDPServer
import mido
import functools

def select_midi(midi_devices: List[Any], preferred=None) -> Any:
    selection = None
    while selection == None:
        for i,device in enumerate(midi_devices):
            print(f"{i} -- {device}")
            if preferred == device:
                 return device
        selection = input()
        if selection.isdecimal() and int(selection) < len(midi_devices):
             return midi_devices[int(selection)]
    print(f"selection: {selection}, len: {len(midi_devices)}, isint: {isinstance(selection, int)}")

def set_note(mido_output, address: str,  *args: List[Any]) ->  None:

    print(f"handler with mido: {mido_output}")
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

#setting up mido
mido_ports = mido.get_output_names()
midi_device = select_midi(mido_ports)
print(f"midi device: {midi_device}")
mido_out = mido.open_output(midi_device)
testmes = mido.Message('note_on', note = 34, velocity = 127)
mido_out.send(testmes)


#setting up osc dispatcher
dispatcher = Dispatcher()
set_note_to_midi = functools.partial(set_note, mido_out)
dispatcher.map("/0/dmx/*", set_note_to_midi)


#run OSC listinging server
server = BlockingOSCUDPServer(("192.168.68.61", 9000), dispatcher)
server.serve_forever()
