Certainly! Here's a revised version of the README focusing on the AirBnB Clone v2 project without Fabric for web static deployment:

---

# AirBnB Clone v2: MySQL Integration

![AirBnB Clone](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## Table of Contents

- [Description](#description)
- [Purpose](#purpose)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [Environmental Variables](#environmental-variables)
- [Usage](#usage)
- [Testing](#testing)
- [Authors](#authors)
- [License](#license)

## Description

**hbnb** is a full-stack clone of the popular vacation rental platform AirBnB. This version, Phase 2, enhances the initial implementation by integrating a MySQL database for data storage.

### Phase 2 Objectives

1. **MySQL Database Integration**: Implement a MySQL database to store application data and utilize ORM (Object-Relational Mapping) to map Python classes to database tables.

## Purpose

The purpose of Phase 2 is to further develop skills in:
- Utilizing MySQL as a database backend with SQLAlchemy for ORM.

## Requirements

- Ubuntu 14.04 LTS
- Python 3.x
- SQLAlchemy 1.2.x
- MySQL 5.7
- PEP 8 and ShellCheck compliance for all scripts and code

## File Structure

- **console.py**: Command-line interpreter with enhanced functionality for creating objects.
- **setup_mysql_dev.sql**: Script to set up a MySQL development server.
- **setup_mysql_test.sql**: Script to set up a MySQL test server.

- **models/**: Directory containing Python classes for AirBnB objects with support for both FileStorage and DBStorage modes.
- **engine/**: Directory containing storage engine implementations.
  - **file_storage.py**: Class for serializing instances to JSON and deserializing from JSON.
  - **db_storage.py**: Class for interfacing with MySQL database using SQLAlchemy.

## Environmental Variables

- **HBNB_ENV**: Running environment ('dev' or 'test').
- **HBNB_MYSQL_USER**: MySQL username.
- **HBNB_MYSQL_PWD**: MySQL password.
- **HBNB_MYSQL_HOST**: MySQL hostname.
- **HBNB_MYSQL_DB**: MySQL database name.
- **HBNB_TYPE_STORAGE**: Type of storage used ('file' or 'db').

## Usage

1. **Setup MySQL**: Execute `setup_mysql_dev.sql` and `setup_mysql_test.sql` to prepare MySQL development and test servers.
2. **Configure Environment**: Set environmental variables to specify MySQL credentials and storage type.
3. **Run the Application**: Execute `console.py` to interact with the AirBnB clone, creating and managing objects stored in the MySQL database.

## Testing

- Unit tests are located in the **tests/** directory.
- Ensure all tests pass to confirm proper functionality of the application.

## Authors

@yonasghiwot |Github

@dagm24|Github
