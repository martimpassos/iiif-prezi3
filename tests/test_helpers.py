import unittest
from iiif_prezi3 import AnnotationPage, Canvas


class CanvasHelpersTests(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(id='http://iiif.example.org/prezi/Canvas/0')

    def test_add_image(self):
        anno_page = self.canvas.add_image('http://iiif.example.org/prezi/Image/0', 'http://iiif.example.org/prezi/Annotation/0')
        self.assertTrue(isinstance(anno_page, AnnotationPage), '`add_image` should return an AnnotationPage')
        self.assertEqual(len(self.canvas.items), 1)
        self.assertEqual(anno_page.items[0].id, 'http://iiif.example.org/prezi/Annotation/0')
        # this seems wrong, shouldn't it be the id property?
        self.assertTrue(anno_page.items[0].body, 'http://iiif.example.org/prezi/Image/0')
