from django.test import TestCase

# Create your tests here.


try:
    import elasticsearch
except ImportError as e:
    print('elasticsearch is not installed')
