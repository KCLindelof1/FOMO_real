from django.test import TestCase
from account import models as amod
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.contenttypes.models import ContentType


# Create your tests here.
class UserClassTestCase(TestCase):

    def setUp(self):
        self.u1 = amod.User()
        self.u1.first_name = 'Lisa'
        self.u1.last_name = 'Simpson'
        self.u1.email = 'lisa@simpsons.com'
        # u1.password = 'password' #This is wrong way to do it
        self.u1.set_password('password')
        # ... do all the others
        self.u1.save()

    def test_load_save_reg_user(self):
        '''Test creating, saving, and reloading a user'''
        # Comment this because we changed it to be in the SetUp
        # u1 = amod.User()
        # u1.first_name = 'Lisa'
        # u1.last_name = 'Simpson'
        # u1.email = 'lisa@simpsons.com'
        # #u1.password = 'password' #This is wrong way to do it
        # u1.set_password('password')
        # # ... do all the others
        # u1.save()

        #alternate way: u2 = amod.User.objects.get(id=u1.id)
        u2 = amod.User.objects.get(email='lisa@simpsons.com')
        self.asertEqual(self.u1.first_name, u2.first_name)
        self.asertEqual(self.u1.last_name, u2.last_name)
        self.asertEqual(self.u1.email, u2.email)
        self.asertEqual(self.u1.password, u2.password)
        self.assertTrue(u2.check_password('password'))

    def test_adding_groups(self):
        '''Test adding a few groups'''

    def test_something(self):
        '''New Stuff here'''

    def test_create_groups(self):
        g1 = Group()
        g1.name = 'Salespeople'
        g1.save()
        self.u1.groups.add(g1)
        self.u1.save()
        self.assertTrue(self.u1.groups.filter(name='SalesPeople')) # Test to see if this user belongs to a certain group
        # Alternate way to test
        # self.asertTrue(self.u1.groups.filter(name='SalesPeople').count() > 1)
        # self.asertTrue(self.u1.groups.get(id=g1.id))
        # self.asertTrue(self.u1.groups.filter(name='SalesPeople').exists() )
        g1.permissions.add(Permission.objects.get(id=4))
        for p in Permission.objects.all():
            print(p.codename)
            print(p.name)
            print(p.content_type)
            # This next line actually would give every permission in the system to the user.
            # self.u1.user_permissions.add(p)

        p = Permission()
        p.codename = 'change_product_price'
        p.name = 'Change the price of a product'
        p.content_type = ContentType.objects.get(id=1)

    def test_password_check(self):
        # Load a second User object with the attributes of the first object
        u2 = amod.User.objects.get(email='lisa@simpsons.com')
        # Check the 2 passwords
        self.assertTrue(self.u1.check_password('password'))
        self.assertTrue(u2.check_password('password'))
        # Change the second password
        u2.set_password('hello')
        # Recheck the 2 passwords
        self.assertTrue(self.u1.check_password('password'))
        self.assertTrue(u2.check_password('hello'))

    def test_regular_field_changes(self):
        # Load a second User object with the attributes of the first object
        u2 = amod.User.objects.get(email='lisa@simpsons.com')
        # Change the name attributes
        u2.first_name = 'Marge'
        u2.last_name = 'Not Simpson'
        # Test to ensure that the changes happened, but unchanged fields are still the same
        self.asertEqual(self.u1.first_name, u2.first_name)
        self.asertEqual(self.u1.last_name, u2.last_name)
        self.asertEqual(self.u1.email, u2.email)
        self.asertEqual(self.u1.password, u2.password)
        self.assertTrue(u2.check_password('password'))
