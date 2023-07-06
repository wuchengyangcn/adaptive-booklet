<!--
Copyright (C) 2023 musicnbrain.org

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
-->

# Adaptive Booklet

> Serving HTML pages with Flask and Jinja2 templates

## Setup

### Dependencies

- Python
- Flask
- Jinja2

### Project Structure

```
├── app.py
├── static
│   ├── data.json
│   ├── desktop.css
│   ├── mobile.css
│   └── turn.js
└── templates
    ├── content_desktop.html
    ├── content_mobile.html
    ├── desktop.html
    ├── front_desktop.html
    ├── front_mobile.html
    └── mobile.html
```

### Run

```
$ python -m flask run
```
