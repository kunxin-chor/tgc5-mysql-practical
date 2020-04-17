from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os

from dotenv import load_dotenv
load_dotenv()

print(os.environ.get('DB_USER'))
print(os.environ.get('DB_PASSWORD'))