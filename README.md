# Keebsound

Keebsound is a package that I built to generate realistic keyboard tap sounds. You can provide a string and it will "type" those characters out, providing ASMR goodness. 
It also supports hooking into the keyboard and replacing your keytap sound with whichever key switch profile you desire. 

## Getting Started

TODO

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

TODO

## Usage

```bash
Options:
  --hook           This hooks into your keyboard and plays a sound when you
                   type

  --switches TEXT  Provide the sound profile, by default it's set to gateron-
                   red

  --delay FLOAT    Sound delay multiplier for playing keyboard sound from a
                   string

  --string TEXT    Pass some arbitrary string to play a keyboard typing sound
                   typing said string

  --help           Show this message and exit.
```

### Playing the sound of a string

`python main.py --string "Foo bar is not enough. What are you up to?" --delay 3`

### Hooking to the keyboard

`python main.py --hook`

You can now start typing and it will generate sounds for you. 

### Using explicit key switch sounds

`python main.py --string "Foo bar is not enough. What are you up to?" --switches gateron-red`

## Contributing

TODO

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

