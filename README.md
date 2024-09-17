# Instructly - Online Quiz Management System (OQMS)

Instructly is an online platform designed to facilitate learning by providing instructors and students with tools to share resources, create and take quizzes, and track progress. The system allows for a seamless, interactive educational experience for both instructors and students.

## Table of Contents

- [Project Name](#project-name)
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Instructor Dashboard](#instructor-dashboard)
  - [Student Dashboard](#student-dashboard)
  - [Create Superuser & Admin Roles](#create-superuser--admin-roles)
- [Screenshot](#screenshot)
- [Testing](#testing)
- [Contributing](#contributing)
- [Licensing](#licensing)

## Project Name

***Instructly***

## Introduction

Instructly is an all-in-one learning platform that enables instructors to create quizzes and manage educational resources while allowing students to participate in quizzes and access these resources. This platform promotes both individual and collaborative learning.

### Live Site

[Instructly - Live Site](https://codepen.io/mumiakmitch/full/qBzLwdJ)

### Final Project Blog

[Blog Article](#)

### Author

[LinkedIn](https://www.linkedin.com/in/mitchel-mugono/)

## Installation

To get started with Instructly, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/instructly.git
```

2.Navigate into the project directory:

```bash
cd instructly
```

3.Install the necessary dependencies:

```bash
pipenv install
```

4.Apply the migrations:

```bash
python manage.py migrate
```

5.Create a superuser for the admin panel:

```bash
python manage.py createsuperuser
```

6.Start the development server:

```bash
python manage.py runserver
```

## Usage

### Instructor Dashboard

Instructors can:

- Create and manage educational resources.
- Design quizzes with questions and automatic grading.
- Track student activity, quiz scores, and submissions.
- Receive real-time notifications.

### Student Dashboard

Students can:

- Access learning resources such as documents and videos.
- Participate in quizzes and receive instant feedback on their performance.

### Create Superuser & Admin Roles

1. **Create a Superuser**  
   Run the following command to create a superuser for the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

   Use the superuser account to log in to the Django admin dashboard.

2. **Create Roles: Instructor and Student**  
   In the admin dashboard, create roles with appropriate permissions:
   - **Instructor**: Assign permissions to create quizzes, manage resources, and track student activity.
   - **Student**: Assign permissions to access learning resources and take quizzes.

## Screenshot

![Login](login.png)
![Register](register.png)
![Instructor Dashboard](instructor.png)
![Learner Dashboard](learner.png)

## Testing

Instructly includes a comprehensive testing suite with unit, integration, and end-to-end (E2E) tests to ensure platform reliability.

### Running Unit Tests

```bash
python manage.py test
```

### Running Integration Tests

```bash
python manage.py test
```

### Running E2E Tests with Selenium

Ensure you have Selenium installed:

```bash
pip install selenium
```

Then, run E2E tests:

```bash
python manage.py test --tag=selenium
```

## Contributing

We welcome contributions! Here's how you can get involved:

1. Fork the repository.
2. Create a new branch for your feature or bugfix: `git checkout -b your-branch-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to your branch: `git push origin your-branch-name`.
5. Create a pull request.

## Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
