{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#APP - Import Dependencies\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from flask import Flask, jsonify\n",
    "import datetime as dt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")\n",
    "Base= automap_base()\n",
    "Base.prepare(engine, reflect= True)\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#flask setup\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#list Routes\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    \"\"\"List all available routes.\"\"\"\n",
    "    return (\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"/api/v1.0/start_date<br/>\"##these routes are for optional analysis\n",
    "        f\"/api/v1.0/start<br/>\"## \n",
    "        f\"/api/v1.0/end<br/>\"## thus there are no queries to create routes since \n",
    "                             ##I did not complete the optional Temp analysis\n",
    "    )\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precp():\n",
    "    precp = session.query(Measurement.date, Measurement.prcp).\\\n",
    "    filter(Measurement.date > last_yr).\\\n",
    "    order_by(Measurement.date).all()\n",
    "    \n",
    "preciptation = []\n",
    "for result in precp:\n",
    "        row = {\"date\":\"prcp\"}\n",
    "        row[\"date\"] = result[0]\n",
    "        row[\"prcp\"] = float(result[1])\n",
    "        precipitation.append(row)\n",
    "        \n",
    "return jsonify(precipitation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    active_stat= session.query(Measurement.station, func.count(Measurement.tobs)).group_by(Measurement.station).\\\n",
    "        order_by(func.count(Measurement.tobs).desc()).all()\n",
    "\n",
    "ls_stations = list(np.ravel(active_stat))\n",
    "return jsonify(ls_stations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "    temp_ob = session.query(Measurement.tobs, Measurement.station, Measurement.date).\\\n",
    "    filter(Measurement.station == low_temp).\\\n",
    "    filter(Measurement.date >= last_yr).\\\n",
    "    order_by(Measurement.date).all()\n",
    "    \n",
    "temperature=[]\n",
    "for result in temp_ob\n",
    "    temperature.append(result.temp)\n",
    "    \n",
    "return jsonify(temperature)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##these routes f\"/api/v1.0/start_date<br/>\"\n",
    "      #  f\"/api/v1.0/start<br/>\"\n",
    "       # f\"/api/v1.0/end<br/>\"\n",
    "    # were included in the optional temperature analysis \n",
    "    # thus I don't have any queries for them to create routes"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
