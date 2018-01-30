from django.test import TestCase
from account import models as amod

# Create your tests here.
class UserClassTestCase(TestCase):

    # def setUp(self):
    #     Animal.objects.create(name="lion", sound="roar")
    #     Animal.objects.create(name="cat", sound="meow")

    def test_load_save_reg_user(self):
        '''Test creating, saving, and reloading a user'''
        u1 = amod.User()
        u1.first_name = 'Lisa'
        u1.last_name = 'Simpson'
        u1.email = 'lisa@simpsons.com'
        #u1.password = 'password' #This is wrong way to do it
        u1.set_password('password')
        # ... do all the others
        u1.save()

        #alternate way: u2 = amod.User.objects.get(id=u1.id)
        u2 = amod.User.objects.get(email='lisa@simpsons.com')
        self.asertEqual(u1.first_name, u2.first_name)
        self.asertEqual(u1.last_name, u2.last_name)
        self.asertEqual(u1.email, u2.email)
        self.asertEqual(u1.password, u2.password)
        self.assertTrue(u2.check_password('password'))

    def test_adding_groups(self):
        '''Test adding a few groups'''
