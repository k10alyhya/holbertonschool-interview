# Star Wars API

This project uses the [Star Wars API](https://swapi-api.hbtn.io/) and the `request` module in Node.js to fetch and display data about Star Wars movies.

## Requirements

- Ubuntu 14.04 LTS
- Node.js 10.14.x
- `request` module
- Code is `semistandard` compliant
- All files start with `#!/usr/bin/node` and are executable

## Installation

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install semistandard --global
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Files

| File | Description |
|------|-------------|
| `0-starwars_characters.js` | Prints all characters of a Star Wars movie, one name per line, in the same order as the `characters` list of the `/films/` endpoint |

## Usage

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
...
```

The first argument is the Movie ID (example: `3` = "Return of the Jedi").

## How it works

1. Reads the Movie ID from the command line arguments.
2. Requests `/films/<id>/` and gets the list of character URLs.
3. Requests each character URL **one after another** (recursively inside the callback) to keep the original order, and prints its `name`.

## Author

Khaled Al-Yahya
