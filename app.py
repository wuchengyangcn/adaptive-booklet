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


class BookletInfo:
    def __init__(self, path):
        data = load(open(path, "r"))
        self.front = data["front"]
        self.content = data["content"]

    def get_view(self, view="mobile"):
        if view == "mobile":
            max_contents_per_page = 11
        else:
            max_contents_per_page = 11

        content = []
        total_content = 0
        current_content = []
        for index in range(len(self.content)):
            lines = 0
            for piece in self.content[index]["pieces"]:
                lines += max(len(piece["title"]), len(piece["composer"]))
            lines += 1
            if total_content + lines > max_contents_per_page:
                content.append(current_content)
                total_content = 0
                current_content = []
            current_content.append(self.content[index])
            total_content += lines
        if len(current_content) > 0:
            content.append(current_content)

        template = f"{view}.html"
        return render_template(template, front=self.front, content=content)


app = Flask(__name__, static_url_path="")
booklet = BookletInfo("./static/data.json")


@app.route("/")
def default():
    return booklet.get_view()


@app.route("/view")
def view():
    return booklet.get_view(view=request.args.get("type"))


if __name__ == "__main__":
    app.run()
