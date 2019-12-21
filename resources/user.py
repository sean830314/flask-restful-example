from flask_restful import Resource, reqparse


class UserRegister(Resource):
    user_list = []
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field is required.', location='form')
    parser.add_argument('password', type=str, required=True, help='This field is required.', location='form')

    def get(self):
        return {'message': self.user_list}, 201

    def post(self):

        data = UserRegister.parser.parse_args()
        self.user_list.append({"username": data['username'], "password": data['password']})
        return {'message': 'User created successfully. username is {}, password is {}.'.format(data['username'], data['password'])}, 201

    def put(self):
        data = UserRegister.parser.parse_args()
        try:
            for user in self.user_list:
                if user['username'] == data['username']:
                    user['password'] = data['password']
            return {'message': 'User put successfully. username is {}, password is {}.'.format(data['username'], data['password'])}, 201
        except Exception as ex:
            return {'message': 'User put fail. error is {}.'.format(ex)}, 401

    def delete(self):
        data = UserRegister.parser.parse_args()
        try:
            self.user_list.remove({"username": data['username'], "password": data['password']})
            return {'message': 'User delete successfully. username is {}, password is {}.'.format(data['username'], data['password'])}, 201
        except Exception as ex:
            return {'message': 'User delete fail. error is {}.'.format(ex)}, 401