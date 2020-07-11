from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User= get_user_model()
        user= User.objects.create_user(
            username='haiden',
            #email='mmariajessica@gmail.com',
            password='mktj2020'
        )
        self.assertEqual(user.username, 'haiden')
        #self.assertEqual(user.email,'')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User= get_user_model()
        admin_user= User.objects.create_superuser(
            username ='caqui',
            email='mmariajessica@gmail.com',
            password='mktj2020'
        )
        self.assertEqual(admin_user.username, 'caqui')
        #self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)