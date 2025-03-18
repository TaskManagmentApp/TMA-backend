# Tasks Management APIs

## Description
This project provides a set of RESTful APIs for managing tasks efficiently. It allows users to create, update, delete, and retrieve tasks, supporting features like task prioritization, due dates, and status tracking.

## Features
- Create, read, update, and delete (CRUD) tasks.
- Assign priorities and due dates to tasks.
- Mark tasks as completed or pending.
- User authentication and authorization.
- API documentation using Swagger/OpenAPI.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/TaskManagmentApp/TMA-backend.git
   ```
2. Navigate to the project directory:
   ```sh
   cd tasks-management-api
   ```
3. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Start the API server:
   ```sh
   python app.py
   ```
2. Access the API endpoints using Postman or cURL.
3. API documentation is available at `/docs` (if Swagger is enabled).

## Configuration
- Environment variables should be set in a `.env` file.
- Database configuration should be updated in `config.py`.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Commit changes:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```sh
   git push origin feature-branch
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any issues or feature requests, please open an issue on GitHub or contact [anees.ali.xca@gmail.com].

