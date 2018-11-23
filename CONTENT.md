# Django App Creating Plan

1. Creating a skeleton website
2. Using models
3. Django admin site
4. Creating home page
5. Creating list and details views
6. Integrate sessions framework
7. User authentications and permissions
8. Creating Django forms
9. Testing web application
10. Deploying to production
11. Security audit of app



## 1. Creating a skeleton website

1.1. Prepare development environment

1.2. Creating the project

1.3. Creating the app

1.4. Registering app in settings.py

1.5. Setup TZ

1.6. Hooking up the URL mapper

1.7. Running database migrations

1.8. Testing the website framework

## 2. Using models

2.1. Data Models and Relationships Design

2.2. Defining the App Models (e.g. Author, Book, Genre, Language, BookInstance, etc.)

## 3. Django admin site

3.1. Registering models

3.2. Creating a superuser

3.3. Logging in and using the site

3.4. Advanced configuration (if it required)

3.4.1. Register a ModelAdmin class

3.4.2. Configure list views

3.4.3. Add list filters

3.4.4. Organise detail view layout

3.4.5. Controlling which fields are displayed and laid out

3.4.6. Sectioning the detail view

3.4.7. Inline editing of associated records

## 4. Creating home page

4.1. Defining the resource URLs

4.2. Creating the index page

4.2.1. View (function-based)

4.2.2. Template

4.2.3. The App Base template

4.2.4. The Index template

4.2.5. Linking to URLs

4.2.6. Configuring where to find the templates

## 5. Creating list and details views

5.1. App list page

5.1.1. URL mapping

5.1.2. View (class-based)

5.1.3. Creating the List View template

5.1.4. Update the base template

5.2. App detail page

5.2.1. URL mapping

5.2.2. View (class-based)

5.2.3. Creating the Detail View template

5.3. Pagination

5.3.1. Views

5.3.2. Templates

## 6. Integrate sessions framework

6.1. Enabling sessions

6.2. Getting visit counts (if required e.g.)

## 7. User authentications and permissions

7.1. Enabling authentication

7.2. Creating users and groups

7.3. Setting up authentication views

7.3.1. Project URLs mapping

7.3.2. Template directory

7.3.3. Login template

7.3.4. Logout template

7.3.5. Password reset templates

7.3.5.1. Password reset form

7.3.5.2. Password reset done

7.3.5.3. Password reset email

7.3.5.4. Password reset confirm

7.3.5.5. Password reset complete

7.4. Testing the new authentication pages

7.5. Testing against authenticated users

7.5.1. Testing in templates

7.6. Listing the current user's books(e.g.)

7.6.1. Models (add new field(s))

7.6.2. Admin (add new filed(s) into early registered model)

7.6.3. Loan a few books

7.6.4. Prepare "On loan" view

7.6.5. URL conf for on loan books

7.6.6. Template for on-loan books

7.6.7. Add the list to the sidebar

7.7. Permissions

7.7.1. Models

7.7.2. Templates

7.7.3. Views

7.7.4. Admin Site

## 8. Creating Django Forms

8.1. Declaring a Form

8.2. Validation

8.3. URL Configuration

8.4. View

8.5. The template

8.6. Testing the page

8.7. Generic editing views

8.7.1. Views

8.7.2. Templates

8.7.3. URL configurations

8.8. Permissions

8.8.1. Views

8.8.2. Templates

## 9. Testing web application

9.1. Create test structure

9.2. Add model tests

9.3. Form tests

9.4. Views

9.4.1. Views that are restricted to logged in users

9.4.2. Testing views with forms

9.4.3. Templates (if required)

## 10. Deploying to production

10.1. Choosing a hosting provider

10.2. Getting website ready to publish

10.3. Installing App on Heroku

10.3.1. Creating an application repository in Github

10.3.2. Update the app for Heroku

10.3.2.1. Procfile

10.3.2.2. Django-heroku

10.3.2.3. Serving static files in production

10.3.2.4. requirements.txt

10.3.2.5. runtime.txt

10.3.3. Save changes to Github and re-test

10.3.4. Create and upload the website

10.3.5. Managing addons

10.3.5.1. Sendgrid Heroku SMTP Relay configuration, etc.

10.3.6. Setting configuration variables

10.3.7. Debugging (if required)

10.3.8. Security settings

10.3.9. Deploy

## 11. Security Audit of App

11.1. Cross site scripting (XSS)

11.2. Cross site request forgery (CSRF) protection

11.3. Other protections

11.3.1. SQL injection protection

11.3.2. Clickjacking protection

11.3.3. Enforcing SSL/HTTPS

11.3.4. Host header validation

