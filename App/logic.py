"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import csv
import os

from DataStructures import Set as set

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

"""
La logica es el sitio donde se manipulan los datos y donde se le responde a la view
"""


def new_logic():
    """
    Crea una instancia de la logica
    """

    catalog = {"books": None,
            "tags": None,
            "book_tags": None}
    
    # Se crean los conjuntos vacios
    catalog["books"] = set.new_set()
    catalog["tags"] = set.new_set()
    catalog["book_tags"] = set.new_set()
    return catalog


# Funciones para la carga de datos

def load_books(catalog, filename):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea el conjunto de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    books = catalog["books"]
    books_file = os.path.join(data_dir, filename)
    catalog["books"] = set.load_set(books, books_file) 
    return book_size(catalog)


def load_tags(catalog, filename):
    # TODO: Mods de Est-1 y Est-2, Est-3 en el Lab 2
    tf = os.path.join(data_dir, filename)
    input_file = csv.DictReader(open(tf, encoding="utf-8"))
    catalog["model"] = create_book_tag_list(catalog["model"])
    for booktag in input_file:
        add_book_tag(catalog, booktag)
    return book_tag_size(catalog)

def load_books_tags(catalog, filename):
    """
    Carga los tags de los libros del archivo
    """
    catalog = control["model"]
    booksfile = os.path.join(cf.data_dir, filename)
    catalog = model.addBookTags(catalog, booksfile)
    return model.bookTagSize(catalog)



def first_book(catalog):
    """
    Devuelve el primer libro del catalogo
    """
    # TODO: Mods Est-3 en el Lab 2
    pass


def last_book(catalog):
    """
    Devuelve el ultimo libro del catalogo
    """
    # TODO: Mods Est-3 en el Lab 2
    pass

# Funciones para la manipulacion de los datos 
sMods de Est-1 y Est-2, Est-3 en el Lab 2
    bt = set.load_set(set.new_set(), booktagsfile)
    catalog["book_tags"] = bt
    return catalog

def create_book_tag_list(catalog):
    """
    Esta funcion crea una lista vacia para booktags.
    """
    catalog["book_tags"] = set.new_set()
    return catalog


def add_book_tag(catalog, booktag):
    """
    Esta funcion agrega un elemento a lista de booktags.
    """
    set.add_element(catalog["book_tags"], booktag)
    return catalog



# Funciones de consulta

def book_size(catalog):
# TODO Mods de Est-3 en el Lab 2
    return set.size(catalog["books"]
                )
def tag_size(catalog):
# TODO Mods de Est-3 en el Lab 2
    return set.size(catalog["tags"])

def book_tag_size(catalog):
# TODO Mods de Est-3 en el Lab 2
    return set.size(catalog["book_tags"])
