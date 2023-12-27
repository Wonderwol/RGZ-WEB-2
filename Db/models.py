from . import db


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)


class cinema_sessions(db.Model):
    session_id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    seat_1 = db.Column(db.Boolean, default=False)
    seat_2 = db.Column(db.Boolean, default=False)
    seat_3 = db.Column(db.Boolean, default=False)
    seat_4 = db.Column(db.Boolean, default=False)
    seat_5 = db.Column(db.Boolean, default=False)
    seat_6 = db.Column(db.Boolean, default=False)
    seat_7 = db.Column(db.Boolean, default=False)
    seat_8 = db.Column(db.Boolean, default=False)
    seat_9 = db.Column(db.Boolean, default=False)
    seat_10 = db.Column(db.Boolean, default=False)
    seat_11 = db.Column(db.Boolean, default=False)
    seat_12 = db.Column(db.Boolean, default=False)
    seat_13 = db.Column(db.Boolean, default=False)
    seat_14 = db.Column(db.Boolean, default=False)
    seat_15 = db.Column(db.Boolean, default=False)
    seat_16 = db.Column(db.Boolean, default=False)
    seat_17 = db.Column(db.Boolean, default=False)
    seat_18 = db.Column(db.Boolean, default=False)
    seat_19 = db.Column(db.Boolean, default=False)
    seat_20 = db.Column(db.Boolean, default=False)
    seat_21 = db.Column(db.Boolean, default=False)
    seat_22 = db.Column(db.Boolean, default=False)
    seat_23 = db.Column(db.Boolean, default=False)
    seat_24 = db.Column(db.Boolean, default=False)
    seat_25 = db.Column(db.Boolean, default=False)
    seat_26 = db.Column(db.Boolean, default=False)
    seat_27 = db.Column(db.Boolean, default=False)
    seat_28 = db.Column(db.Boolean, default=False)
    seat_29 = db.Column(db.Boolean, default=False)
    seat_30 = db.Column(db.Boolean, default=False)
    occupant_1 = db.Column(db.String(255), default=None)
    occupant_2 = db.Column(db.String(255), default=None)
    occupant_3 = db.Column(db.String(255), default=None)
    occupant_4 = db.Column(db.String(255), default=None)
    occupant_5 = db.Column(db.String(255), default=None)
    occupant_6 = db.Column(db.String(255), default=None)
    occupant_7 = db.Column(db.String(255), default=None)
    occupant_8 = db.Column(db.String(255), default=None)
    occupant_9 = db.Column(db.String(255), default=None)
    occupant_10 = db.Column(db.String(255), default=None)
    occupant_11 = db.Column(db.String(255), default=None)
    occupant_12 = db.Column(db.String(255), default=None)
    occupant_13 = db.Column(db.String(255), default=None)
    occupant_14 = db.Column(db.String(255), default=None)
    occupant_15 = db.Column(db.String(255), default=None)
    occupant_16 = db.Column(db.String(255), default=None)
    occupant_17 = db.Column(db.String(255), default=None)
    occupant_18 = db.Column(db.String(255), default=None)
    occupant_19 = db.Column(db.String(255), default=None)
    occupant_20 = db.Column(db.String(255), default=None)
    occupant_21 = db.Column(db.String(255), default=None)
    occupant_22 = db.Column(db.String(255), default=None)
    occupant_23 = db.Column(db.String(255), default=None)
    occupant_24 = db.Column(db.String(255), default=None)
    occupant_25 = db.Column(db.String(255), default=None)
    occupant_26 = db.Column(db.String(255), default=None)
    occupant_27 = db.Column(db.String(255), default=None)
    occupant_28 = db.Column(db.String(255), default=None)
    occupant_29 = db.Column(db.String(255), default=None)
    occupant_30 = db.Column(db.String(255), default=None)
