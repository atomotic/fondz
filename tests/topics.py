import os
import json

from unittest import TestCase

import inventstory

test_data = os.path.join(os.path.dirname(__file__), 'data')
keats = os.path.join(test_data, 'keats')

class TopicTest(TestCase):
    
    def test_topics(self):
        topics = inventstory.mallet.topics(keats)
        self.assertEqual(len(topics), 10)
        self.assertEqual(len(topics[0]['words']), 15)

