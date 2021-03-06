import os
import json
import fondz
import tempfile
import unittest

from fondz.create import init, add_bag

from os.path import join, isdir, isfile, islink, realpath

bag1 = os.path.join(os.path.dirname(__file__), 'data', 'bag1')
bag2 = os.path.join(os.path.dirname(__file__), 'data', 'bag1')

class CreateTests(unittest.TestCase):

    def test_init(self):
        d = tempfile.mkdtemp()
        init(d)
        self.assertTrue(isdir(join(d, "js")))
        self.assertTrue(isdir(join(d, "css")))
        self.assertTrue(isdir(join(d, "img")))
        self.assertTrue(isdir(join(d, "originals")))
        self.assertTrue(isdir(join(d, "derivatives")))


    def atest_add_bag(self):
        d = tempfile.mkdtemp()
        init(d)

        add_bag(d, bag1)
        p1 = join(d, "originals", "1")
        self.assertTrue(islink(p1))
        self.assertEqual(realpath(p1), bag1)

        add_bag(d, bag2)
        p2 = join(d, "originals", "2")
        self.assertTrue(islink(p2))
        self.assertEqual(realpath(p2), bag2)


    def atest_create(self):
        d = tempfile.mkdtemp()
        fondz.create(d, bag1)
        self.assertTrue(isdir(d))

        # derivatives there?
        self.assertTrue(isfile(join(d, "derivatives", "1", "word.doc.html")))
        self.assertTrue(isfile(join(d, "derivatives", "1", "wordperfect.wp.html")))
        self.assertTrue(isfile(join(d, "derivatives", "1", "subdir", "word.docx.html")))

        # topic models json is there?
        topics_file = join(d, "js", "topics.json")
        self.assertTrue(isfile(topics_file))
        self.assertTrue(isjson(topics_file))

        # file format json is there?
        formats_file = join(d, "js", "formats.json")
        self.assertTrue(isfile(formats_file))
        self.assertTrue(isjson(formats_file))

        # index there?
        index = join(d, "index.html")
        self.assertTrue(isfile(index))
        html = open(index).read()
        self.assertTrue('<!doctype html>' in html)


def isjson(filename):
    return json.loads(open(filename).read())
