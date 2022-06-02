#!/usr/bin/env python3

# Written by Ivona Obonova
# 22.2.2022

from flask import Blueprint, render_template, request, flash
from .knn import Knn

controller = Blueprint('controller', __name__)

@controller.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        isbn = request.args.get('isbn')
        title = request.args.get('title')

        if isbn:
            recommended = Knn.knn(isbn)
            return render_template("home.html", found=False, found_books=[ ], recommend=True, recommended=recommended)
        elif title:
            found_books = Knn.find(title)
            if found_books.empty:
                flash('The book was not found.', category='error')
                return render_template("home.html", found=False, found_books=[ ], recommend=False, recommended=[ ])
            else:
                return render_template("home.html", found=True, found_books=found_books.iterrows(), recommend=False, recommended=[ ])
        else:
            return render_template("home.html", found=False, found_books=[ ], recommend=False, recommended=[ ])

    return render_template("home.html", found=False, found_books=[ ], recommend=False, recommended=[ ])
