# Management command to import data into MongoDB database
from django.core.management.base import BaseCommand, CommandError
import csv
import sys
import argparse
from pymongo import MongoClient


class Command(BaseCommand):
    # Generic data upload into MongoDB using CSV as data origin.
    help = 'Data upload into MongoDB'

    def add_arguments(self, parser):
        # CSV file to get data from
        parser.add_argument('infile', nargs='?',
                            type=argparse.FileType('r'), default=sys.stdin
                            )

        # Set name of the collection items are uploaded to
        parser.add_argument('collection', nargs='?')

        # optional command to show all the uploaded ids
        parser.add_argument('--showids', action='store_true')

    def handle(self, *args, **options):
        server = 'localhost'
        port = 27017
        database = "marvel_restapi"

        collection = options["collection"]

        column_names = []
        items_to_insert = []

        with options['infile'] as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    for items in row:
                        column_names.append(items)
                else:
                    temp_dic = {}
                    n = len(column_names)
                    i = 0
                    while i < n:
                        temp_dic.update({
                            column_names[i]: row[i]
                        })
                        i += 1
                    items_to_insert.append(temp_dic)
                line_count += 1

        client = MongoClient(server, port)
        db = client[database]
        collection = db[collection]

        new_result = collection.insert_many(items_to_insert)
        if options['showids']:
            print('Multiple posts: {0}'.format(new_result.inserted_ids))
