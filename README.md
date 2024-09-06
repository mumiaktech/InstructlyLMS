# Instructly

**Instructly** is a comprehensive online learning platform designed to help users upskill and grow in their careers. The platform offers a wide range of educational resources, quizzes, and interactive features to enhance the learning experience for both students and instructors.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [Instructor Dashboard](#instructor-dashboard)
  - [Student Dashboard](#student-dashboard)
  - [Quizzes and Resources](#quizzes-and-resources)
- [Testing](#testing)
  - [Unit Tests](#unit-tests)
  - [Integration Tests](#integration-tests)
  - [End-to-End (E2E) Tests](#end-to-end-e2e-tests)
- [Contributing](#contributing)

## Features

- **User Roles**: Separate roles for Instructors and Students, each with specific features.
- **Instructor Dashboard**: Manage resources, quizzes, view notifications, and track activity.
- **Student Dashboard**: Access quizzes, learning resources, profile settings, and view recent activity.
- **Quizzes**: Create, edit, and take quizzes with automatic scoring.
- **Resources**: Share and manage educational resources like documents, videos, and links.
- **Notifications**: Receive real-time notifications for important updates.
- **Reports and Support**: Submit reports and receive support from instructors.
- **Responsive Design**: Optimized for various devices using Bootstrap.

## Usage

### Instructor Dashboard

Instructors can:

- **Create and Manage Resources**: Upload documents, videos, course materials, and other learning content.
- **Create Quizzes**: Design quizzes with multiple questions and answers, including correct/incorrect answer tracking.
- **Track Student Activity**: View student progress, quiz scores, and submission reports.
- **Receive Notifications**: Get notified about new student activities, reports, and important updates.

### Student Dashboard

Students can:

- **Access Learning Resources**: Browse and view shared educational resources in various formats (videos, documents, interactive content).
- **Take Quizzes**: Participate in quizzes, view instant feedback and scores.

### Quizzes and Resources

- **Quiz Management**: Instructors can create quizzes. Students can take quizzes and view their scores immediately after submission.
- **Resource Management**: Instructors upload, categorize, and manage resources, which are easily accessible by students. Resources can include different formats, such as documents, videos, and interactive tools.

## Testing

Instructly includes a full testing suite with unit tests, integration tests, and end-to-end tests to ensure the platform’s reliability and functionality.

### Unit Tests

Unit tests are available for all core models, including `Resource`, `UserProfile`, `Report`, `Quiz`, `Question`, and others. These tests ensure that individual components and model behaviors work as expected.

To run unit tests, use:

```bash
python manage.py test
```

### Integration Tests

Integration tests ensure that different parts of the system work together. This includes testing how quizzes interact with questions, how resources are accessed by students, and how instructors manage content and notifications.

To run integration tests, use:

```bash
python manage.py test
```

### End-to-End (E2E) Tests

We use **Selenium** for E2E tests, simulating user interactions across the entire platform (e.g., logging in, creating quizzes, taking quizzes). These tests ensure that the entire flow works as expected from the user’s perspective.

To run end-to-end tests, ensure you have the necessary browser drivers (like **Chromedriver** for Chrome or **Geckodriver** for Firefox) installed, then run:

```bash
python manage.py test --tag=selenium
```

Make sure you have Selenium installed:

```bash
pip install selenium
```

## Contributing

We welcome contributions to Instructly! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

Please ensure your code adheres to the existing code style and includes relevant tests.
