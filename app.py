#################################################
# Hi Project Team!!
# This is our Flask App.
#################################################


from flask import Flask, jsonify, render_template, request, flash, redirect, json
from config import remote_db_endpoint, remote_db_port, remote_dbname, remote_dbuser, remote_dbpwd
import os

import pandas as pd
import numpy as np

# from sqlalchemy import create_engine
# import pymysql
# pymysql.install_as_MySQLdb()


app = Flask(__name__)

#################################################
# FINAL PROJECT - Put code we are keeping HERE
#################################################
<<<<<<< HEAD
=======
# AWS Database Connection

engine = create_engine(
    f"mysql://{remote_dbuser}:{remote_dbpwd}@{remote_db_endpoint}:{remote_db_port}/{remote_dbname}")

# Create a remote database engine connection
conn = engine.connect()
>>>>>>> be09a07f874975e8adea85fdf4c430a2ee3cb4c7

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

<<<<<<< HEAD
@app.route("/addresses")
def addresss():
=======
@app.route("/names")
def names():
>>>>>>> be09a07f874975e8adea85fdf4c430a2ee3cb4c7
    """Return foreclosure list."""

    db = pd.read_csv("foreclosure_data_4-12v2.csv")
    addresses = pd.DataFrame(db).to_dict('records')
    print(addresses)
    return jsonify(addresses)

@app.route("/table")
def table():
    return render_template("table2.html")

if __name__ == "__main__":
    app.run(debug=True)

#################################################
# Database Setup (commented out because of AWS error)
#################################################

# # AWS Database Connection
# engine = create_engine(
#     f"mysql://{remote_dbuser}:{remote_dbpwd}@{remote_db_endpoint}:{remote_db_port}/{remote_dbname}")

# # Create a remote database engine connection
# conn = engine.connect()

# @app.route("/names")
# def names():
#     """Return foreclosure list."""

#     data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)

#     names = data_df.to_dict('records')

#     print(names)
#     return jsonify(names)


<<<<<<< HEAD
# @app.route("/foreclosure_data")
# def foreclosure_data():
#     """Return foreclosure list."""

#     # # Use Pandas to perform the sql query
#     # stmt = db.session.query(Samples).statement
#     # df = pd.read_sql_query(stmt, db.session.bind)
=======
@app.route("/table.html")
def table():
    """Return foreclosure list."""
    data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)
    names = data_df.to_dict('records')
>>>>>>> be09a07f874975e8adea85fdf4c430a2ee3cb4c7

#     # Return a list of the column names (sample names)

#     data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)

<<<<<<< HEAD
#     # OPTION 1 -- return json
#     data_json = data_df.to_json()
#     return data_json

#     # OPTION 2 -- return json records; list of dicts
#     #data_json = data_df.to_json(orient='records')
#     # return data_json
=======
@app.route("/graph.html")
def graph():
    """Return foreclosure list."""
    
    # # Use Pandas to perform the sql query
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)
    # Return a list of the column names (sample names)
    
    #graph = pd.DataFrame(db).to_dict('records')
    data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)
    graph_data = data_df[["principal_amount","zestimate"]]
    #print(graph)
    #return graph.to_json(orient="records")
    graph = pd.DataFrame(graph_data).to_dict('records')
    data = {'graph': graph}
    return render_template("graph.html", data=data)
>>>>>>> be09a07f874975e8adea85fdf4c430a2ee3cb4c7

#     # OPTION 3 -- jsonify dictionary
#     #data_dict = data_df.to_dict()
#     # return jsonify(data_dict)
#     # WARNING: This approach contains the keys. If you want to get only the values, use
#     # Object.values() in your JS file

<<<<<<< HEAD

# @app.route("/table.html")
# def table():
#     """Return foreclosure list."""
#     data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)
#     names = data_df.to_dict('records')

#     table_df = data_df[["property_address","zestimate","bedrooms","bathrooms","deposit","principal_amount","estimated_equity","date_of_auction","auction_location"]]
#     # table_df = table_df.rename(columns={"property_address":"Property Address"}, inplace=True)

#     columnNames = table_df.columns.values
#     return render_template('table.html', records=names, colnames=columnNames)
=======
@app.route("/graphdata")
def graphdata():
    """Return foreclosure list."""
    
    # # Use Pandas to perform the sql query
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)
    # Return a list of the column names (sample names)
    
    #graph = pd.DataFrame(db).to_dict('records')
    data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)
    graph_data = data_df[["principal_amount","zestimate"]]
>>>>>>> be09a07f874975e8adea85fdf4c430a2ee3cb4c7


# @app.route("/graph.html")
# def graph():
#     """Return foreclosure list."""

#     # # Use Pandas to perform the sql query
#     # stmt = db.session.query(Samples).statement
#     # df = pd.read_sql_query(stmt, db.session.bind)
#     # Return a list of the column names (sample names)

#     #graph = pd.DataFrame(db).to_dict('records')
#     data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)
#     graph_data = data_df[["principal_amount","zestimate"]]
#     #print(graph)
#     #return graph.to_json(orient="records")
#     graph = pd.DataFrame(graph_data).to_dict('records')
#     data = {'graph': graph}
#     return render_template("graph.html", data=data)


# @app.route("/graphdata")
# def graphdata():
#     """Return foreclosure list."""

#     # # Use Pandas to perform the sql query
#     # stmt = db.session.query(Samples).statement
#     # df = pd.read_sql_query(stmt, db.session.bind)
#     # Return a list of the column names (sample names)

#     #graph = pd.DataFrame(db).to_dict('records')
#     data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)
#     graph_data = data_df[["principal_amount","zestimate"]]

#     graph = pd.DataFrame(graph_data).to_dict('records')

#     print(graph)
#     # return graph.to_json(orient="records")
#     return jsonify(graph)

@app.route("/map")
def map():
    """Return foreclosure map view."""
    # # Use Pandas to perform the sql query
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)
    # Return a list of the column names (sample names)

    data_df = pd.read_sql("SELECT * FROM foreclosure_data_final", conn)

    # OPTION 1 -- return json
    data_json = data_df.to_json()
    return data_json


