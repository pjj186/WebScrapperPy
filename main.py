import os
import csv
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect
from remote import get_remoteok
from so import get_so
from wwr import get_wwr
from export import save_to_file
from flask import send_file


"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("RemoteJobs")

db = {}

@app.route("/")
def main():
  return render_template("index.html")


@app.route("/detail")
def detail():
  word = request.args.get("word")
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs :
      jobs = existingJobs
    else :
      jobs = get_remoteok(word) + get_so(word) + get_wwr(word)
      db[word] = jobs
  else :
    return redirect("/")
  return render_template("detail.html", searchingBy=word, resultsNum=len(jobs), jobs = jobs)


@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs, word)
    return send_file(f"{word}.csv")
  except:
    return redirect("/")




app.run(host="0.0.0.0")