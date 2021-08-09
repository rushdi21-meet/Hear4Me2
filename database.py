from sqlalchemy.testing import db
from flask import Flask, jsonify, request, render_template, redirect, url_for
from sqlalchemy.sql import exists

from model import *
from textblob import TextBlob

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///Volunteers_DB.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def query_all():
    """
    Print all the volunteers
    in the database.
    """
    volunteers = session.query(Volunteer).all()
    return volunteers


def add_volunteer(full_name, username, password):
    """
    Add a volunteer to the database, given
    their name, year, and whether they have
    finished the lab.
    """
    new_volunteer = Volunteer(full_name=full_name, username=username, password=password)
    session.add(new_volunteer)
    session.commit()
    return print("new volunteer added!")


def query_by_name(username):
    try:
        volunteer = session.query(Volunteer).filter_by(username=username).first()
        return volunteer.id
    except:
        return ("no such volunteer")


def query_by_password(password):
    try:
        volunteer = session.query(Volunteer).filter_by(password=password).first()
        return volunteer.id
    except:
        return ("no such password")


def login(username, password):
    if query_by_name(username) == query_by_password(password):
        return true
    else:
        return false











