import os
import tempfile
import fondz
import unittest

from fondz.convert import convert_to_html, convert_dir
from fondz.create import init, add_bag

bag1 = os.path.join(os.path.dirname(__file__), 'data', 'bag1')
test_data = os.path.join(bag1, 'data')

class ConvertTest(unittest.TestCase):

    def test_wordperfect(self):
        f1 = os.path.join(test_data, 'wordperfect.wp')
        f2 = convert_to_html(f1)
        self.assertTrue(f2)
        self.assertTrue(os.path.isfile(f2))

    def test_word(self):
        f1  = os.path.join(test_data, 'word.doc')
        f2 = convert_to_html(f1)
        self.assertTrue(f2)
        self.assertTrue(os.path.isfile(f2))
        self.assertTrue(os.path.getsize(f2) > 0)

    def test_convert_dir(self):
        target_dir = tempfile.mkdtemp() 
        convert_dir(test_data, target_dir)
        files = os.listdir(target_dir)
        self.assertEqual(len(files), 3)
        self.assertTrue('word.doc.html' in files)
        self.assertTrue('wordperfect.wp.html' in files)
        self.assertTrue('subdir' in files)
        subdir = os.path.join(target_dir, 'subdir')
        files = os.listdir(subdir)
        self.assertEqual(len(files), 1)
        self.assertTrue('word.docx.html' in files)

    def test_convert(self):
        fondz_dir = tempfile.mkdtemp()
        init(fondz_dir)
        add_bag(fondz_dir, bag1)
        fondz.convert(fondz_dir)
        f = os.path.join(fondz_dir, 'derivatives', '1', 'word.doc.html')
        self.assertTrue(os.path.isfile(f))


