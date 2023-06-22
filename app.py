"""
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
"""

from flask import Flask, render_template, request
from json import load
import math


class BookletInfo:
    def __init__(self, path):
        data = load(open(path, "r"))
        self.front = data["front"]
        self.content = data["content"]
        self.view_type = ""
        self.current_content = 0
        self.max_contents_per_page = 0

        self.set_mobile()

    def set_desktop(self):
        if self.view_type != "desktop":
            self.view_type = "desktop"
            self.current_content = 0
            self.max_contents_per_page = 10

    def set_mobile(self):
        if self.view_type != "mobile":
            self.view_type = "mobile"
            self.current_content = 0
            self.max_contents_per_page = 8

    def get_page(self):
        if self.current_content == 0:
            self.current_content += 1
            template = f"front_{self.view_type}.html"
            return render_template(template, data=self.front)

        return_contents = []
        total_contents = 0
        while self.current_content <= len(self.content):
            for piece in self.content[self.current_content - 1]["pieces"]:
                total_contents += max(len(piece["title"]), len(piece["composer"]))
                if total_contents > self.max_contents_per_page:
                    break
            if total_contents <= self.max_contents_per_page:
                return_contents.append(self.content[self.current_content - 1])
                self.current_content += 1
            else:
                break

        if self.current_content > len(self.content):
            self.current_content = 0

        template = f"content_{self.view_type}.html"
        return render_template(template, data=return_contents)


app = Flask(__name__, static_url_path="/static")
booklet = BookletInfo("./static/data.json")


@app.route("/")
def get_page():
    return booklet.get_page()


@app.route("/view")
def set_type():
    view_type = request.args.get("type")
    if view_type == "desktop":
        booklet.set_desktop()
    else:
        booklet.set_mobile()
    return booklet.get_page()


if __name__ == "__main__":
    app.run()
