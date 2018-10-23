from tests.unit.unit_base_test import UnitBaseTest
from models.user import UserModel

class TestUserRegister(UnitBaseTest):
    def test_user_creation(self):
        user = UserModel('test_username', 'test_pass')

        self.assertEqual(user.password, 'test_pass')
        self.assertEqual(user.username, 'test_username')

