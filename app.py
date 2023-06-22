import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('themost.db')
    conn.row_factory = sqlite3.Row
    return conn


# def get_post(post_id):
#     conn = get_db_connection()
#     post = conn.execute('SELECT * FROM themost WHERE id = ?',(post_id,)).fetchone()
#     conn.close()  
#     return post

@app.route('/homepage')
def index():
    conn = get_db_connection()
    con = get_db_connection()
    aaa = conn.execute('SELECT * FROM houses_types').fetchall()
    bbb = con.execute('SELECT * FROM buildings_types').fetchall()
    conn.close()
    con.close()
    # return 'result'
    return render_template('index.html', houses = aaa,buildings = bbb)


# @app.route('/')
# def index2():
#     # conn = get_db_connection()
#     con = get_db_connection()
#     # aaa = conn.execute('SELECT * FROM houses_types').fetchall()
#     bbb = con.execute('SELECT * FROM buildings_types').fetchall()
#     con.close()
#     # conт.close()
#     # return 'result'
#     return render_template('index.html', buildings = bbb)

# @app.route('/house/<int:house_id>')

@app.route('/houses/<int:id>')
def houses(id):
    conn = get_db_connection()

    if id == 1:
        id = '1'
        table_name = 'houses'

    elif id == 2:
        id = '2'
        table_name = 'tree_houses'
    
    elif id == 3:
        id = '3'
        table_name = 'houses_on_wheels'

    elif id == 4:
        id = '4'
        table_name = 'houses_on_water'

    sql = 'SELECT * FROM ' + table_name    
    result = conn.execute(sql).fetchall()
    sql_2 = 'SELECT * FROM houses_types WHERE id =' + id
    aaa = conn.execute(sql_2).fetchall()
    conn.close()
    return render_template('houses_test.html', houses = result, img_folder = table_name,  houses_types = aaa)



@app.route('/buildings/<int:id>')
def buildings(id):
    conn = get_db_connection()

    if id == 2:
        id = '2'
        table_name = 'churches_buildings'

    elif id == 3:
        id = '3'
        table_name = 'schools_buildings'

    elif id == 4:
        id = '4'
        table_name = 'university_buildings'

    elif id == 5:
        id = '5'
        table_name = 'castles_buildings'

    elif id == 6:
        id = '6'
        table_name = 'lions_buildings'
    

    sql = 'SELECT * FROM ' + table_name    
    result = conn.execute(sql).fetchall()
    sql_2 = 'SELECT * FROM buildings_types WHERE id =' + id
    aaa = conn.execute(sql_2).fetchall()
    conn.close()
    return render_template('buildings.html', buildings = result, img_folder = table_name, buildings_types = aaa)



# @app.route('/house/<int:id>')
# def houses(id):
#     id = 1
#     conn = get_db_connection()
#     aaa = conn.execute('SELECT * FROM houses').fetchall()
#     conn.close()
#     return render_template('houses.html', houses = aaa)


# @app.route('/house/2')
# def tree_houses():
#     conn = get_db_connection()
#     aaa = conn.execute('SELECT * FROM tree_houses').fetchall()
#     conn.close()
#     return render_template('tree_houses.html', tree_houses = aaa)

# @app.route('/house/4')
# def houses_on_water():
#     conn = get_db_connection()
#     aaa = conn.execute('SELECT * FROM houses_on_water').fetchall()
#     conn.close()
#     return render_template('houses_on_water.html', houses_on_water = aaa)


@app.route('/single-gallery')
def single_gallery():
    return render_template('single-gallery.html')


@app.route('/category')
def category():
    return render_template('category.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/single-standard')
def single_standart():
    return render_template('single-standard.html')


@app.route('/base')
def base():
    return render_template('base.html')