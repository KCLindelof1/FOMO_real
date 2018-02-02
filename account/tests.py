from django.test import TestCase
from account import models as amod
from django.contrib.auth.models import Group, Permission, ContentType
# from django.contrib.auth.contenttypes.models import ContentType


# Create your tests here.
class UserClassTest(TestCase):

    fixtures = [ 'data.yaml' ]

    def setUp(self):
        self.u1 = amod.User()
        self.u1.first_name = 'Lisa'
        self.u1.last_name = 'Simpson'
        self.u1.email = 'lisa@simpsons.com'
        # u1.password = 'password' #This is wrong way to do it
        self.u1.set_password('password')
        self.u1.birthdate = '2001-01-30'
        self.u1.address = '745 Evergreen Terrace'
        self.u1.city = 'Springfield'
        self.u1.state = 'IL'
        self.u1.zipcode = '12345'
        self.u1.save()

    # Create a user and save, then load again and compare
    def test_load_save_reg_user(self):
        '''Test creating, saving, and reloading a user'''
        # Load a user (copy of the setup user)
        u2 = amod.User.objects.get(email='lisa@simpsons.com')
        self.assertEqual(self.u1.first_name, u2.first_name)
        self.assertEqual(self.u1.last_name, u2.last_name)
        self.assertEqual(self.u1.email, u2.email)
        self.assertEqual(self.u1.password, u2.password)
        self.assertTrue(u2.check_password('password'))

    # Add groups to users and test some permissions
    def test_adding_groups_try_permissions(self):
        '''Test adding a few groups and test their permissions'''
        # Create a new group
        g1 = Group()
        g1.name = 'Salespeople'
        g1.save()

        # Add group to user
        self.u1.groups.add(g1)
        self.u1.save()

        # Test to make sure u1 is in group g1
        self.assertTrue(self.u1.groups.filter(name='Salespeople').exists())  # Test to see if this user belongs to a certain group (salespeople)

        # Create new permission
        p = Permission()
        p.codename = 'change_product_price'
        p.name = 'Change the price of a product'
        p.content_type = ContentType.objects.get_for_model(amod.User)
        p.save()

        # Add permission to group
        g1.permissions.add(p)

        # Test the permission
        self.assertTrue(self.u1.has_perm('account.change_product_price'))

    # Add permissions to users and test some permissions
    def test_permissions_check_permissions(self):
        '''Add permissions to users and test some permissions'''
        # Create new permission
        p = Permission()
        p.codename = 'test_permission'
        p.name = 'simply a test'
        p.content_type = ContentType.objects.get_for_model(amod.User)
        p.save()

        # Add permissions to u2
        self.u1.user_permissions.add(p)
        self.u1.save()

        # Check the permission
        self.assertTrue(self.u1.has_perm('account.test_permission'))

    # Test password with set_password() and check_password()
    def test_password_check(self):
        '''Test password with set_password() and check_password()'''
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
        self.assertNotEqual(self.u1.password, u2.password)

    # Test regular field changes (first name, last name, etc.)
    def test_regular_field_changes(self):
        '''Test regular field changes (first name, last name, etc.)'''
        # Load a second User object with the attributes of the first object
        u2 = amod.User.objects.get(email='lisa@simpsons.com')

        # Change the name attributes
        u2.first_name = 'Marge'
        u2.last_name = 'Not Simpson'

        # Test to ensure that the changes happened, but unchanged fields are still the same
        self.assertNotEqual(self.u1.first_name, u2.first_name)
        self.assertNotEqual(self.u1.last_name, u2.last_name)
        self.assertEqual(self.u1.email, u2.email)
        self.assertEqual(self.u1.password, u2.password)
