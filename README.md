# ESP32 w/ LED Matrix

- ESP32 board (joy-it)
- Simple 64x64 LED matrix

This code requires a modified micropython with the
added [ledmatrix library](https://github.com/Winkelkatze/ledmatrix).
The compilation is not straightforward as it uses a modified
I2S implementation that is a bit out of date.

## Running

1. flash the firmware bin using esptool.py
2. copy [src/config.json.tmpl](src/config.json.tmpl) to src/config.json and set your SSID and password
3. write the contents of [src/](src) into the root of the device
4. reset device to start

## References

- ledmatrix - [ledmatrix](https://github.com/Winkelkatze/ledmatrix) code compiled into firmware bin
- mpy-miniterm - [dev tool](https://github.com/jeffmakes/mpy-miniterm) for syncing code to the device
- hsv2rgb - [some stackoverflow answer](https://stackoverflow.com/a/26856771)
- CEST time conversion - [from a discussion]('https://github.com/orgs/micropython/discussions/11173) on the micropython
  forum

## [License](LICENSE.txt)

```
Copyright 2023 Matthias L. Jugel

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
