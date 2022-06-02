#!/usr/bin/env python3

# Written by Ivona Obonova
# 22.2.2022

from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
